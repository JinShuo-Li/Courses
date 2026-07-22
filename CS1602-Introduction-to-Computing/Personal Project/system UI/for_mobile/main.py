import flet as ft
import requests
import feedparser
import json
import os
import threading
import time
from datetime import datetime

# --- 配置 ---
# 在手机上，文件路径通常由系统管理，这里只用简单的文件名
TODO_FILE = "todo.json"

def main(page: ft.Page):
    # 1. 页面基础设置 (手机适配)
    page.title = "个人中心"
    page.theme_mode = "dark" # 使用字符串 'dark' 
    page.padding = 10
    # 启用滚动，防止键盘弹出遮挡
    page.scroll = "auto" 

    # ==========================
    #       数据逻辑层
    # ==========================
    tasks = []

    def load_tasks():
        if os.path.exists(TODO_FILE):
            try:
                with open(TODO_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_tasks():
        try:
            with open(TODO_FILE, "w", encoding="utf-8") as f:
                json.dump(tasks, f, ensure_ascii=False, indent=4)
        except:
            pass # 手机文件权限严格，防止报错闪退

    tasks = load_tasks()

    # ==========================
    #       UI 组件层
    # ==========================

    # --- 1. 待办事项页面组件 ---
    # 使用 ListView 在手机上性能更好
    task_list_view = ft.Column(spacing=10, scroll="auto")

    def render_tasks():
        task_list_view.controls.clear()
        for i, task in enumerate(tasks):
            idx = i 
            
            # 任务行
            row = ft.Container(
                content=ft.Row(
                    [
                        ft.Checkbox(
                            label=task["text"], 
                            value=task["done"],
                            on_change=lambda e, i=idx: toggle_task_logic(i, e.control.value)
                        ),
                        ft.IconButton(
                            icon="delete_outline", # 字符串图标
                            icon_color="red",
                            on_click=lambda e, i=idx: delete_task_logic(i)
                        )
                    ],
                    alignment="spaceBetween" # 字符串对齐
                ),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.SURFACE_VARIANT
            )
            task_list_view.controls.append(row)
        
        page.update()

    def add_task_logic(e):
        if not new_task_input.value: return
        tasks.append({"text": new_task_input.value, "done": False})
        save_tasks()
        new_task_input.value = ""
        render_tasks()

    def toggle_task_logic(index, value):
        tasks[index]["done"] = value
        save_tasks()
        render_tasks()

    def delete_task_logic(index):
        del tasks[index]
        save_tasks()
        render_tasks()

    new_task_input = ft.TextField(hint_text="输入新任务...", expand=True)
    add_btn = ft.FloatingActionButton(icon="add", on_click=add_task_logic)

    # 待办页面容器
    view_todo = ft.Column(
        controls=[
            ft.Row([new_task_input, add_btn]),
            ft.Divider(),
            task_list_view
        ],
    )

    # --- 2. 简报页面组件 ---
    weather_title = ft.Text("获取天气中...", size=24, weight="bold", color="white")
    weather_subtitle = ft.Text("--", color="white70") # 使用 white70 这种安全色值
    news_list_view = ft.Column(spacing=10, scroll="auto")

    # 简报页面容器
    view_news = ft.Column(
        controls=[
            # 天气卡片
            ft.Container(
                content=ft.Column([weather_title, weather_subtitle]),
                padding=20,
                width=float("inf"),
                border_radius=15,
                # 使用原始坐标避免报错
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left if hasattr(ft.alignment, "top_left") else ft.Alignment(-1, -1),
                    end=ft.alignment.bottom_right if hasattr(ft.alignment, "bottom_right") else ft.Alignment(1, 1),
                    colors=["#1e3c72", "#2a5298"],
                )
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("全球要闻", size=18, weight="bold"),
            news_list_view
        ],
    )

    # ==========================
    #       后台线程层
    # ==========================
    def background_worker():
        render_tasks() 
        while True:
            # 1. 天气
            try:
                url = "https://api.open-meteo.com/v1/forecast?latitude=39.9042&longitude=116.4074&current_weather=true"
                res = requests.get(url, timeout=5).json()
                if "current_weather" in res:
                    w = res["current_weather"]
                    weather_title.value = f"北京 {w['temperature']}°C"
                    weather_subtitle.value = f"风速: {w['windspeed']} km/h | 更新: {datetime.now().strftime('%H:%M')}"
            except:
                weather_title.value = "无法连接天气服务"

            # 2. RSS
            try:
                # 增加 User-Agent 防止被某些网站拦截
                feed = feedparser.parse("http://www.people.com.cn/rss/world.xml")
                new_controls = []
                for entry in feed.entries[:10]:
                    new_controls.append(
                        ft.Container(
                            content=ft.Column([
                                ft.Text(entry.title, weight="bold", size=14),
                                ft.Text("人民网", size=10, color="grey"),
                                ft.Divider()
                            ]),
                            padding=5
                        )
                    )
                news_list_view.controls = new_controls
            except:
                pass
            
            try:
                page.update()
            except:
                break # 页面如果关闭则退出循环
            
            time.sleep(3600) 

    threading.Thread(target=background_worker, daemon=True).start()

    # ==========================
    #       导航逻辑
    # ==========================
    def on_nav_change(e):
        idx = e.control.selected_index
        page.clean() # 清除当前页面内容
        if idx == 0:
            page.add(view_todo)
        elif idx == 1:
            page.add(view_news)
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon="check_circle_outline", selected_icon="check_circle", label="待办"),
            ft.NavigationDestination(icon="article_outlined", selected_icon="article", label="简报"),
        ],
        on_change=on_nav_change,
        selected_index=0
    )

    # 初始加载
    page.add(view_todo)

if __name__ == "__main__":
    ft.app(target=main)