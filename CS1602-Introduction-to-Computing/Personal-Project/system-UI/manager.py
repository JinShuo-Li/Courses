import customtkinter as ctk
import psutil
import threading
import time
import requests
import json
import os
import feedparser  # <--- 新增库，请确保已安装 (pip install feedparser)
from datetime import datetime

# --- 配置 ---
ctk.set_appearance_mode("Dark")  # 模式: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # 主题

# 字体配置
FONT_HEADER = ("Roboto Medium", 20)
FONT_NORMAL = ("Roboto", 14)
FONT_SMALL = ("Roboto", 12)

# 文件保存路径
TODO_FILE = "todo_list.json"

class ModernDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 窗口基础设置
        self.title("Personal Command Center")
        self.geometry("1000x700")
        
        # 配置主窗口网格权重
        self.grid_columnconfigure(1, weight=1) # 右侧区域自动伸缩
        self.grid_rowconfigure(0, weight=1)    # 垂直方向自动伸缩

        # === 左侧面板：待办事项 (To-Do List) ===
        self.left_frame = ctk.CTkFrame(self, width=300, corner_radius=15)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.left_frame.grid_rowconfigure(2, weight=1) # 让列表区域可伸缩

        # 标题
        self.todo_label = ctk.CTkLabel(self.left_frame, text="待办事项 / Tasks", font=FONT_HEADER)
        self.todo_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # 输入框和添加按钮
        self.todo_entry = ctk.CTkEntry(self.left_frame, placeholder_text="添加新任务 (回车)...", font=FONT_NORMAL)
        self.todo_entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
        self.todo_entry.bind("<Return>", lambda event: self.add_task()) # 回车添加

        # 滚动列表区域
        self.scrollable_frame = ctk.CTkScrollableFrame(self.left_frame, label_text="任务列表")
        self.scrollable_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # 待办事项数据存储
        self.tasks = []
        self.load_tasks()

        # === 右侧面板：Dashboard ===
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent") # 透明背景
        self.right_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
        self.right_frame.grid_columnconfigure(0, weight=1)
        # 配置右侧行权重，让新闻区域（第2行）占据多余空间
        self.right_frame.grid_rowconfigure(2, weight=1) 

        # 1. 系统状态 (System Stats)
        self.stats_frame = ctk.CTkFrame(self.right_frame, corner_radius=15)
        self.stats_frame.grid(row=0, column=0, padx=0, pady=(0, 10), sticky="ew")
        self.create_stats_widgets()

        # 2. 天气模块 (Weather)
        self.weather_frame = ctk.CTkFrame(self.right_frame, corner_radius=15)
        self.weather_frame.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="ew")
        self.create_weather_widgets()

        # 3. 新闻模块 (News)
        self.news_frame = ctk.CTkFrame(self.right_frame, corner_radius=15)
        self.news_frame.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        self.create_news_widgets()

        # === 启动后台线程 ===
        self.running = True
        # 启动系统监控线程
        self.monitor_thread = threading.Thread(target=self.update_system_stats)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        # 启动API数据获取（天气和新闻）
        self.api_thread = threading.Thread(target=self.fetch_api_data)
        self.api_thread.daemon = True
        self.api_thread.start()

    # ---------------- UI 构建辅助函数 ----------------

    def create_stats_widgets(self):
        self.stats_frame.grid_columnconfigure((1, 3), weight=1)
        
        # CPU
        self.cpu_label = ctk.CTkLabel(self.stats_frame, text="CPU: 0%", font=FONT_SMALL)
        self.cpu_label.grid(row=0, column=0, padx=15, pady=15)
        self.cpu_bar = ctk.CTkProgressBar(self.stats_frame)
        self.cpu_bar.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="ew")
        self.cpu_bar.set(0)

        # RAM
        self.ram_label = ctk.CTkLabel(self.stats_frame, text="RAM: 0%", font=FONT_SMALL)
        self.ram_label.grid(row=0, column=2, padx=15, pady=15)
        self.ram_bar = ctk.CTkProgressBar(self.stats_frame, progress_color="#3B8ED0") # 不同颜色
        self.ram_bar.grid(row=0, column=3, padx=(0, 15), pady=15, sticky="ew")
        self.ram_bar.set(0)

    def create_weather_widgets(self):
        # 使用 pack 布局
        self.weather_title = ctk.CTkLabel(self.weather_frame, text="正在获取天气...", font=FONT_HEADER)
        self.weather_title.pack(anchor="w", padx=20, pady=(15, 5))
        
        self.weather_detail = ctk.CTkLabel(self.weather_frame, text="--", font=FONT_NORMAL, text_color="gray")
        self.weather_detail.pack(anchor="w", padx=20, pady=(0, 15))

    def create_news_widgets(self):
        # 标题
        title = ctk.CTkLabel(self.news_frame, text="每日简报 / Daily Briefing", font=FONT_HEADER)
        title.pack(anchor="w", padx=20, pady=15)
        
        # 文本框
        self.news_text_box = ctk.CTkTextbox(self.news_frame, font=FONT_NORMAL)
        self.news_text_box.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        
        self.news_text_box.insert("0.0", "正在加载 RSS 新闻源...\n")
        self.news_text_box.configure(state="disabled") # 只读

    # ---------------- 逻辑功能：To-Do List ----------------

    def add_task(self):
        task_text = self.todo_entry.get()
        if task_text:
            self.tasks.append({"text": task_text, "done": False})
            self.refresh_task_list()
            self.todo_entry.delete(0, "end")
            self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.refresh_task_list()
        self.save_tasks()

    def toggle_task(self, index, var):
        self.tasks[index]["done"] = bool(var.get())
        self.refresh_task_list() # 刷新以更新颜色
        self.save_tasks()

    def refresh_task_list(self):
        # 清空当前显示
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # 重建列表
        for i, task in enumerate(self.tasks):
            # 复选框
            check_var = ctk.IntVar(value=1 if task["done"] else 0)
            
            # 颜色修复：根据完成状态切换灰色或自适应黑白
            text_color = "gray" if task["done"] else ("black", "white")
            
            checkbox = ctk.CTkCheckBox(
                self.scrollable_frame, 
                text=task["text"], 
                variable=check_var,
                font=FONT_NORMAL,
                text_color=text_color,  
                command=lambda idx=i, v=check_var: self.toggle_task(idx, v)
            )
            checkbox.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            
            # 删除按钮
            del_btn = ctk.CTkButton(
                self.scrollable_frame, 
                text="✕", 
                width=30, 
                height=24,
                fg_color="#C0392B", 
                hover_color="#E74C3C",
                command=lambda idx=i: self.delete_task(idx)
            )
            del_btn.grid(row=i, column=1, padx=10, pady=5)

    def save_tasks(self):
        try:
            with open(TODO_FILE, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存失败: {e}")

    def load_tasks(self):
        if os.path.exists(TODO_FILE):
            try:
                with open(TODO_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
                self.refresh_task_list()
            except:
                self.tasks = []

    # ---------------- 后台逻辑：监控与API ----------------

    def update_system_stats(self):
        while self.running:
            try:
                cpu = psutil.cpu_percent(interval=1)
                ram = psutil.virtual_memory().percent
                
                # 只有当窗口还在运行时才更新
                if self.winfo_exists():
                    self.after(0, self._update_stats_ui, cpu, ram)
            except Exception as e:
                print(f"Stats Error: {e}")
                break

    def _update_stats_ui(self, cpu, ram):
        try:
            self.cpu_label.configure(text=f"CPU: {cpu}%")
            self.cpu_bar.set(cpu / 100)
            self.ram_label.configure(text=f"RAM: {ram}%")
            self.ram_bar.set(ram / 100)
        except:
            pass

    def fetch_api_data(self):
        """获取天气和 RSS 新闻"""
        
        # 1. 获取天气 (Open-Meteo)
        try:
            # 默认上海坐标 (Lat: 31.3332, Lon: 121.5355)
            lat, lon = 31.3332, 121.5355 
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if "current_weather" in data:
                temp = data["current_weather"]["temperature"]
                wind = data["current_weather"]["windspeed"]
                weather_code = data["current_weather"]["weathercode"]
                
                status = "晴朗"
                if weather_code > 3: status = "多云/阴"
                if weather_code > 50: status = "有雨"
                if weather_code > 70: status = "有雪"

                weather_str = f"上海: {status} {temp}°C"
                detail_str = f"风速: {wind} km/h | 更新: {datetime.now().strftime('%H:%M')}"
                
                if self.winfo_exists():
                    self.after(0, lambda: self.weather_title.configure(text=weather_str))
                    self.after(0, lambda: self.weather_detail.configure(text=detail_str))
        except Exception as e:
            if self.winfo_exists():
                self.after(0, lambda: self.weather_title.configure(text="天气获取超时"))
                print(f"Weather Error: {e}")

        # 2. 获取新闻 (RSS - 方案二)
        try:
            # RSS源地址：人民网-国际要闻
            # 你也可以换成:
            # 百度热搜: https://rss.hub.app/baidu/top
            # 财新网: http://www.caixin.com/rss/finance.xml
            rss_url = "http://www.people.com.cn/rss/world.xml"
            
            # 使用 feedparser 解析
            feed = feedparser.parse(rss_url)
            
            articles_list = []
            
            if feed.entries:
                # 只获取前 10 条
                for entry in feed.entries[:10]:
                    title = entry.title
                    # 尝试清理标题中的多余空白
                    title = title.strip()
                    # 来源名称
                    source = "人民网" 
                    articles_list.append(f"• [{source}] {title}")
            else:
                articles_list.append("RSS 源暂时无法连接或无内容。")
            
            news_content = "\n\n".join(articles_list)
        
        except Exception as e:
            print(f"RSS Error: {e}")
            news_content = f"RSS 解析失败: {str(e)}\n请检查网络连接。"

        if self.winfo_exists():
            self.after(0, self._update_news_ui, news_content)

    def _update_news_ui(self, content):
        try:
            self.news_text_box.configure(state="normal")
            self.news_text_box.delete("0.0", "end")
            self.news_text_box.insert("0.0", content)
            self.news_text_box.configure(state="disabled")
        except:
            pass

    def on_closing(self):
        self.running = False
        self.destroy()

if __name__ == "__main__":
    app = ModernDashboard()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()