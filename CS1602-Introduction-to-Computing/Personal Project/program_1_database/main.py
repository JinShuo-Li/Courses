import os
import sys
import shutil
import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Any
import logging
import socket
import getpass
import uuid
from dataclasses import dataclass, asdict
from enum import Enum
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import tkinter.scrolledtext as scrolledtext
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk
import threading
import webbrowser

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_manager.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FileType(Enum):
    DOCUMENT = "文档"
    IMAGE = "图片"
    AUDIO = "音频"
    VIDEO = "视频"
    ARCHIVE = "压缩包"
    CODE = "代码"
    EXECUTABLE = "可执行文件"
    OTHER = "其他"

@dataclass
class FileRecord:
    """文件记录数据类"""
    id: str
    original_name: str
    stored_name: str
    file_path: str
    file_type: str
    size: int
    hash_md5: str
    description: str
    tags: List[str]
    created_at: datetime
    modified_at: datetime
    ip_address: str
    gps_location: str
    import_user: str
    folder_path: str
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        data = asdict(self)
        data['created_at'] = data['created_at'].isoformat()
        data['modified_at'] = data['modified_at'].isoformat()
        data['tags'] = json.dumps(data['tags'])
        return data

class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self, db_path: str = "file_manager.db"):
        self.db_path = db_path
        self.init_database()
        
    def init_database(self):
        """初始化数据库表"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 文件记录表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS files (
                    id TEXT PRIMARY KEY,
                    original_name TEXT NOT NULL,
                    stored_name TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    file_type TEXT NOT NULL,
                    size INTEGER NOT NULL,
                    hash_md5 TEXT NOT NULL UNIQUE,
                    description TEXT,
                    tags TEXT DEFAULT '[]',
                    created_at TIMESTAMP NOT NULL,
                    modified_at TIMESTAMP NOT NULL,
                    ip_address TEXT,
                    gps_location TEXT,
                    import_user TEXT,
                    folder_path TEXT
                )
            ''')
            
            # 操作记录表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS operations (
                    id TEXT PRIMARY KEY,
                    file_id TEXT,
                    operation_type TEXT NOT NULL,
                    operation_time TIMESTAMP NOT NULL,
                    user_name TEXT,
                    ip_address TEXT,
                    details TEXT,
                    FOREIGN KEY (file_id) REFERENCES files (id)
                )
            ''')
            
            # 文件夹结构表
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS folders (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    path TEXT UNIQUE NOT NULL,
                    parent_id TEXT,
                    created_at TIMESTAMP NOT NULL,
                    FOREIGN KEY (parent_id) REFERENCES folders (id)
                )
            ''')
            
            # 创建索引以提高搜索性能
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_tags ON files(tags)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_created ON files(created_at)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_files_type ON files(file_type)')
            
            conn.commit()
            logger.info("数据库初始化完成")
    
    def add_file_record(self, record: FileRecord) -> bool:
        """添加文件记录"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                data = record.to_dict()
                cursor.execute('''
                    INSERT INTO files VALUES (
                        :id, :original_name, :stored_name, :file_path, :file_type,
                        :size, :hash_md5, :description, :tags, :created_at,
                        :modified_at, :ip_address, :gps_location, :import_user, :folder_path
                    )
                ''', data)
                
                # 记录操作
                cursor.execute('''
                    INSERT INTO operations VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    str(uuid.uuid4()),
                    record.id,
                    'IMPORT',
                    datetime.now().isoformat(),
                    record.import_user,
                    record.ip_address,
                    f'导入文件: {record.original_name}'
                ))
                
                conn.commit()
                logger.info(f"文件记录添加成功: {record.original_name}")
                return True
        except sqlite3.Error as e:
            logger.error(f"添加文件记录失败: {e}")
            return False
    
    def search_files(self, keyword: str = None, 
                     start_date: str = None, 
                     end_date: str = None,
                     tags: List[str] = None,
                     file_type: str = None) -> List[Dict]:
        """搜索文件"""
        query = "SELECT * FROM files WHERE 1=1"
        params = []
        
        if keyword:
            query += " AND (original_name LIKE ? OR description LIKE ?)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        if start_date:
            query += " AND created_at >= ?"
            params.append(start_date)
        
        if end_date:
            query += " AND created_at <= ?"
            params.append(end_date)
        
        if tags:
            for tag in tags:
                query += " AND tags LIKE ?"
                params.append(f'%{tag}%')
        
        if file_type:
            query += " AND file_type = ?"
            params.append(file_type)
        
        query += " ORDER BY created_at DESC"
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                # 转换Row对象为字典
                results = []
                for row in rows:
                    result = dict(row)
                    result['tags'] = json.loads(result['tags'])
                    results.append(result)
                
                return results
        except sqlite3.Error as e:
            logger.error(f"搜索文件失败: {e}")
            return []
    
    def get_all_tags(self) -> List[str]:
        """获取所有标签"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT tags FROM files")
                rows = cursor.fetchall()
                
                tags_set = set()
                for row in rows:
                    if row[0]:
                        try:
                            file_tags = json.loads(row[0])
                            tags_set.update(file_tags)
                        except:
                            pass
                
                return sorted(list(tags_set))
        except sqlite3.Error as e:
            logger.error(f"获取标签失败: {e}")
            return []
    
    def get_operation_logs(self, limit: int = 100) -> List[Dict]:
        """获取操作日志"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT o.*, f.original_name 
                    FROM operations o
                    LEFT JOIN files f ON o.file_id = f.id
                    ORDER BY o.operation_time DESC
                    LIMIT ?
                ''', (limit,))
                
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"获取操作日志失败: {e}")
            return []

class FileManager:
    """文件管理器"""
    
    def __init__(self, storage_root: str = "storage"):
        self.storage_root = Path(storage_root)
        self.storage_root.mkdir(exist_ok=True)
        
        self.db = DatabaseManager()
        self.current_user = getpass.getuser()
        
    def get_file_type(self, file_path: str) -> str:
        """根据扩展名判断文件类型"""
        ext = Path(file_path).suffix.lower()
        
        type_map = {
            '.txt': FileType.DOCUMENT.value,
            '.pdf': FileType.DOCUMENT.value,
            '.doc': FileType.DOCUMENT.value,
            '.docx': FileType.DOCUMENT.value,
            '.jpg': FileType.IMAGE.value,
            '.jpeg': FileType.IMAGE.value,
            '.png': FileType.IMAGE.value,
            '.gif': FileType.IMAGE.value,
            '.bmp': FileType.IMAGE.value,
            '.mp3': FileType.AUDIO.value,
            '.wav': FileType.AUDIO.value,
            '.flac': FileType.AUDIO.value,
            '.mp4': FileType.VIDEO.value,
            '.avi': FileType.VIDEO.value,
            '.mov': FileType.VIDEO.value,
            '.zip': FileType.ARCHIVE.value,
            '.rar': FileType.ARCHIVE.value,
            '.7z': FileType.ARCHIVE.value,
            '.tar': FileType.ARCHIVE.value,
            '.gz': FileType.ARCHIVE.value,
            '.py': FileType.CODE.value,
            '.js': FileType.CODE.value,
            '.java': FileType.CODE.value,
            '.cpp': FileType.CODE.value,
            '.exe': FileType.EXECUTABLE.value,
            '.msi': FileType.EXECUTABLE.value,
        }
        
        return type_map.get(ext, FileType.OTHER.value)
    
    def calculate_file_hash(self, file_path: str) -> str:
        """计算文件MD5哈希值"""
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            logger.error(f"计算文件哈希失败 {file_path}: {e}")
            return ""
    
    def get_ip_address(self) -> str:
        """获取IP地址"""
        try:
            # 获取本机IP
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except:
            return "未知"
    
    def import_file(self, source_path: str, tags: List[str], 
                   description: str = "", folder: str = "") -> Tuple[bool, str]:
        """导入文件"""
        try:
            source_path = Path(source_path)
            if not source_path.exists():
                return False, "源文件不存在"
            
            # 计算文件哈希
            file_hash = self.calculate_file_hash(str(source_path))
            if not file_hash:
                return False, "计算文件哈希失败"
            
            # 检查是否已存在相同文件
            with sqlite3.connect(self.db.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM files WHERE hash_md5 = ?", (file_hash,))
                if cursor.fetchone():
                    return False, "文件已存在（重复文件）"
            
            # 确定存储路径
            file_type = self.get_file_type(str(source_path))
            type_folder = self.storage_root / file_type
            if folder:
                type_folder = type_folder / folder
            type_folder.mkdir(parents=True, exist_ok=True)
            
            # 生成唯一文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_name = f"{timestamp}_{source_path.name}"
            dest_path = type_folder / unique_name
            
            # 复制文件
            shutil.copy2(source_path, dest_path)
            
            # 创建文件记录
            file_record = FileRecord(
                id=str(uuid.uuid4()),
                original_name=source_path.name,
                stored_name=unique_name,
                file_path=str(dest_path),
                file_type=file_type,
                size=source_path.stat().st_size,
                hash_md5=file_hash,
                description=description,
                tags=tags,
                created_at=datetime.now(),
                modified_at=datetime.fromtimestamp(source_path.stat().st_mtime),
                ip_address=self.get_ip_address(),
                gps_location="",  # 可扩展GPS功能
                import_user=self.current_user,
                folder_path=folder
            )
            
            # 保存到数据库
            if self.db.add_file_record(file_record):
                return True, f"文件导入成功: {source_path.name}"
            else:
                # 如果数据库保存失败，删除已复制的文件
                dest_path.unlink(missing_ok=True)
                return False, "数据库保存失败"
                
        except Exception as e:
            logger.error(f"导入文件失败 {source_path}: {e}")
            return False, f"导入失败: {str(e)}"
    
    def search(self, **kwargs) -> List[Dict]:
        """搜索文件"""
        return self.db.search_files(**kwargs)
    
    def get_file_info(self, file_id: str) -> Optional[Dict]:
        """获取文件详细信息"""
        try:
            with sqlite3.connect(self.db.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM files WHERE id = ?", (file_id,))
                row = cursor.fetchone()
                if row:
                    result = dict(row)
                    result['tags'] = json.loads(result['tags'])
                    return result
                return None
        except sqlite3.Error as e:
            logger.error(f"获取文件信息失败: {e}")
            return None

class FileManagerGUI:
    """文件管理器GUI"""
    
    def __init__(self):
        self.manager = FileManager()
        self.setup_gui()
        self.load_tags()
        self.refresh_file_list()
        
    def setup_gui(self):
        """设置GUI界面"""
        self.root = TkinterDnD.Tk()
        self.root.title("智能文件管理系统")
        self.root.geometry("1200x800")
        
        # 设置图标
        try:
            self.root.iconbitmap(default='icon.ico')
        except:
            pass
        
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        
        # 创建菜单栏
        self.setup_menu()
        
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧面板 - 文件夹树
        left_panel = ttk.Frame(main_frame, width=200)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        
        # 文件夹树
        ttk.Label(left_panel, text="文件夹结构").pack(anchor=tk.W, pady=(0, 5))
        self.tree = ttk.Treeview(left_panel)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 中间面板 - 文件列表
        center_panel = ttk.Frame(main_frame)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 搜索框
        search_frame = ttk.Frame(center_panel)
        search_frame.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(search_frame, text="搜索:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<Return>', lambda e: self.refresh_file_list())
        
        ttk.Button(search_frame, text="搜索", 
                  command=self.refresh_file_list).pack(side=tk.LEFT, padx=2)
        ttk.Button(search_frame, text="高级搜索", 
                  command=self.show_advanced_search).pack(side=tk.LEFT, padx=2)
        ttk.Button(search_frame, text="重置", 
                  command=self.reset_search).pack(side=tk.LEFT, padx=2)
        
        # 文件列表
        columns = ("ID", "文件名", "类型", "大小", "标签", "创建时间", "导入者")
        self.file_list = ttk.Treeview(center_panel, columns=columns, show='headings')
        
        # 设置列标题
        for col in columns:
            self.file_list.heading(col, text=col)
            self.file_list.column(col, width=100)
        
        # 调整列宽
        self.file_list.column("文件名", width=200)
        self.file_list.column("标签", width=150)
        self.file_list.column("ID", width=50, stretch=False)
        
        # 滚动条
        scrollbar = ttk.Scrollbar(center_panel, orient=tk.VERTICAL, 
                                 command=self.file_list.yview)
        self.file_list.configure(yscrollcommand=scrollbar.set)
        
        self.file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 绑定双击事件
        self.file_list.bind('<Double-Button-1>', self.on_file_double_click)
        
        # 右侧面板 - 操作按钮
        right_panel = ttk.Frame(main_frame, width=200)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
        
        # 操作按钮
        ttk.Label(right_panel, text="操作", font=('Arial', 10, 'bold')).pack(pady=(0, 10))
        
        button_frame = ttk.Frame(right_panel)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="导入文件", 
                  command=self.import_files_dialog).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="刷新列表", 
                  command=self.refresh_file_list).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="查看详情", 
                  command=self.show_file_details).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="打开文件", 
                  command=self.open_file).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="操作日志", 
                  command=self.show_operation_logs).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="导出选中", 
                  command=self.export_selected).pack(fill=tk.X, pady=2)
        ttk.Button(button_frame, text="删除选中", 
                  command=self.delete_selected).pack(fill=tk.X, pady=2)
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 启用拖放功能
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.on_drop)
        
    def setup_menu(self):
        """设置菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="导入文件", command=self.import_files_dialog)
        file_menu.add_command(label="批量导入", command=self.batch_import)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 编辑菜单
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="编辑", menu=edit_menu)
        edit_menu.add_command(label="修改标签", command=self.edit_tags)
        edit_menu.add_command(label="修改描述", command=self.edit_description)
        edit_menu.add_separator()
        edit_menu.add_command(label="备份数据库", command=self.backup_database)
        
        # 查看菜单
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="查看", menu=view_menu)
        view_menu.add_command(label="刷新", command=self.refresh_file_list)
        view_menu.add_command(label="统计信息", command=self.show_stats)
        
        # 工具菜单
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="工具", menu=tools_menu)
        tools_menu.add_command(label="批量重命名", command=self.batch_rename)
        tools_menu.add_command(label="重复文件检查", command=self.check_duplicates)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self.show_help)
        help_menu.add_command(label="关于", command=self.show_about)
    
    def on_drop(self, event):
        """处理拖放事件"""
        files = self.root.tk.splitlist(event.data)
        for file_path in files:
            self.import_file_dialog(file_path)
    
    def import_files_dialog(self):
        """导入文件对话框"""
        files = filedialog.askopenfilenames(
            title="选择要导入的文件",
            filetypes=[
                ("所有文件", "*.*"),
                ("文档文件", "*.txt *.pdf *.doc *.docx"),
                ("图片文件", "*.jpg *.jpeg *.png *.gif *.bmp"),
                ("视频文件", "*.mp4 *.avi *.mov"),
                ("音频文件", "*.mp3 *.wav *.flac")
            ]
        )
        
        for file_path in files:
            self.import_file_dialog(file_path)
    
    def import_file_dialog(self, file_path: str):
        """单个文件导入对话框"""
        dialog = tk.Toplevel(self.root)
        dialog.title("导入文件")
        dialog.geometry("500x550")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 文件信息
        file_info = Path(file_path)
        ttk.Label(dialog, text=f"文件: {file_info.name}").pack(pady=5)
        ttk.Label(dialog, text=f"大小: {self.format_size(file_info.stat().st_size)}").pack(pady=5)
        
        # 描述
        ttk.Label(dialog, text="描述:").pack(pady=(10, 0), anchor=tk.W, padx=20)
        description_text = tk.Text(dialog, height=4, width=50)
        description_text.pack(padx=20, pady=(0, 10))
        
        # 标签
        ttk.Label(dialog, text="标签 (用逗号分隔):").pack(pady=(10, 0), anchor=tk.W, padx=20)
        tags_entry = ttk.Entry(dialog, width=50)
        tags_entry.pack(padx=20, pady=(0, 10))
        
        # 常用标签
        ttk.Label(dialog, text="常用标签:").pack(pady=(5, 0), anchor=tk.W, padx=20)
        tags_frame = ttk.Frame(dialog)
        tags_frame.pack(padx=20, pady=(0, 10), fill=tk.X)
        
        common_tags = ["重要", "工作", "个人", "临时", "归档", "项目"]
        for tag in common_tags:
            btn = ttk.Button(tags_frame, text=tag, width=8,
                           command=lambda t=tag: tags_entry.insert(tk.END, f"{t}, "))
            btn.pack(side=tk.LEFT, padx=2)
        
        # 文件夹
        ttk.Label(dialog, text="文件夹:").pack(pady=(10, 0), anchor=tk.W, padx=20)
        folder_entry = ttk.Entry(dialog, width=50)
        folder_entry.pack(padx=20, pady=(0, 20))
        
        def do_import():
            description = description_text.get("1.0", tk.END).strip()
            tags = [tag.strip() for tag in tags_entry.get().split(",") if tag.strip()]
            folder = folder_entry.get().strip()
            
            success, message = self.manager.import_file(
                file_path, tags, description, folder
            )
            
            if success:
                messagebox.showinfo("成功", message)
                self.refresh_file_list()
                dialog.destroy()
            else:
                messagebox.showerror("失败", message)
        
        # 按钮
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=20)
        
        def do_import():
            description = description_text.get("1.0", tk.END).strip()
            tags = [tag.strip() for tag in tags_entry.get().split(",") if tag.strip()]
            folder = folder_entry.get().strip()
        
            success, message = self.manager.import_file(
                file_path, tags, description, folder
            )
        
            if success:
                messagebox.showinfo("成功", message)
                self.refresh_file_list()
                dialog.destroy()
            else:
                messagebox.showerror("失败", message)

        ttk.Button(button_frame, text="导入", command=do_import).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="取消", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
        
        # 自动填充文件名为描述
        description_text.insert("1.0", file_info.stem)
    
    def refresh_file_list(self, search_keyword: str = None):
        """刷新文件列表"""
        # 清空列表
        for item in self.file_list.get_children():
            self.file_list.delete(item)
        
        # 获取搜索参数
        search_params = {}
        keyword = self.search_var.get().strip()
        if keyword:
            search_params['keyword'] = keyword
        
        # 执行搜索
        files = self.manager.search(**search_params)
        
        # 填充列表
        for file_info in files:
            tags = ", ".join(file_info.get('tags', []))
            size = self.format_size(file_info.get('size', 0))
            created_at = datetime.fromisoformat(file_info['created_at']).strftime("%Y-%m-%d %H:%M")
            
            self.file_list.insert("", tk.END, values=(
                file_info['id'][:8],
                file_info['original_name'],
                file_info['file_type'],
                size,
                tags,
                created_at,
                file_info['import_user']
            ), tags=(file_info['id'],))
        
        self.status_var.set(f"找到 {len(files)} 个文件")
    
    def show_advanced_search(self):
        """显示高级搜索对话框"""
        dialog = tk.Toplevel(self.root)
        dialog.title("高级搜索")
        dialog.geometry("400x500")
        
        ttk.Label(dialog, text="关键字:").pack(pady=(10, 0), anchor=tk.W, padx=20)
        keyword_entry = ttk.Entry(dialog, width=40)
        keyword_entry.pack(padx=20, pady=(0, 10))
        
        ttk.Label(dialog, text="标签:").pack(pady=(10, 0), anchor=tk.W, padx=20)
        tags_entry = ttk.Entry(dialog, width=40)
        tags_entry.pack(padx=20, pady=(0, 10))
        
        ttk.Label(dialog, text="文件类型:").pack(pady=(10, 0), anchor=tk.W, padx=20)
        type_combo = ttk.Combobox(dialog, values=[t.value for t in FileType], width=37)
        type_combo.pack(padx=20, pady=(0, 10))
        
        ttk.Label(dialog, text="开始日期 (YYYY-MM-DD):").pack(pady=(10, 0), anchor=tk.W, padx=20)
        start_date_entry = ttk.Entry(dialog, width=40)
        start_date_entry.pack(padx=20, pady=(0, 10))
        
        ttk.Label(dialog, text="结束日期 (YYYY-MM-DD):").pack(pady=(10, 0), anchor=tk.W, padx=20)
        end_date_entry = ttk.Entry(dialog, width=40)
        end_date_entry.pack(padx=20, pady=(0, 20))
        
        def do_search():
            search_params = {}
            
            keyword = keyword_entry.get().strip()
            if keyword:
                search_params['keyword'] = keyword
            
            tags = tags_entry.get().strip()
            if tags:
                search_params['tags'] = [tag.strip() for tag in tags.split(",")]
            
            file_type = type_combo.get().strip()
            if file_type:
                search_params['file_type'] = file_type
            
            start_date = start_date_entry.get().strip()
            if start_date:
                search_params['start_date'] = start_date
            
            end_date = end_date_entry.get().strip()
            if end_date:
                search_params['end_date'] = end_date
            
            # 执行搜索
            files = self.manager.search(**search_params)
            
            # 清空并刷新列表
            for item in self.file_list.get_children():
                self.file_list.delete(item)
            
            for file_info in files:
                tags_str = ", ".join(file_info.get('tags', []))
                size = self.format_size(file_info.get('size', 0))
                created_at = datetime.fromisoformat(file_info['created_at']).strftime("%Y-%m-%d %H:%M")
                
                self.file_list.insert("", tk.END, values=(
                    file_info['id'][:8],
                    file_info['original_name'],
                    file_info['file_type'],
                    size,
                    tags_str,
                    created_at,
                    file_info['import_user']
                ), tags=(file_info['id'],))
            
            self.status_var.set(f"找到 {len(files)} 个文件")
            dialog.destroy()
        
        ttk.Button(dialog, text="搜索", command=do_search).pack(pady=10)
    
    def show_file_details(self):
        """显示文件详情"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择一个文件")
            return
        
        file_id = self.file_list.item(selection[0])['tags'][0]
        file_info = self.manager.get_file_info(file_id)
        
        if not file_info:
            messagebox.showerror("错误", "无法获取文件信息")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("文件详情")
        dialog.geometry("600x500")
        
        # 创建滚动区域
        canvas = tk.Canvas(dialog)
        scrollbar = ttk.Scrollbar(dialog, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # 文件信息
        info_text = f"""
文件名称: {file_info['original_name']}
存储名称: {file_info['stored_name']}
文件类型: {file_info['file_type']}
文件大小: {self.format_size(file_info['size'])}
MD5哈希: {file_info['hash_md5']}
存储路径: {file_info['file_path']}
文件夹: {file_info['folder_path'] or '根目录'}

描述: {file_info['description'] or '无'}

标签: {', '.join(file_info['tags'])}

创建时间: {file_info['created_at']}
修改时间: {file_info['modified_at']}
导入用户: {file_info['import_user']}
IP地址: {file_info['ip_address']}
GPS位置: {file_info['gps_location'] or '未记录'}
        """
        
        text_widget = scrolledtext.ScrolledText(scrollable_frame, width=70, height=20)
        text_widget.insert(tk.END, info_text.strip())
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # 按钮
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=(0, 20))
        
        ttk.Button(button_frame, text="打开文件", 
                  command=lambda: self.open_specific_file(file_info['file_path'])).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="打开所在文件夹", 
                  command=lambda: self.open_file_location(file_info['file_path'])).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="复制路径", 
                  command=lambda: self.root.clipboard_clear() or 
                                 self.root.clipboard_append(file_info['file_path'])).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="关闭", 
                  command=dialog.destroy).pack(side=tk.LEFT, padx=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def on_file_double_click(self, event):
        """处理文件列表的双击事件"""
        self.show_file_details()

    def show_operation_logs(self):
        """显示操作日志"""
        logs = self.manager.db.get_operation_logs(100)
        
        dialog = tk.Toplevel(self.root)
        dialog.title("操作日志")
        dialog.geometry("800x600")
        
        # 创建文本区域
        text_widget = scrolledtext.ScrolledText(dialog, width=100, height=30)
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # 添加日志内容
        for log in logs:
            time_str = datetime.fromisoformat(log['operation_time']).strftime("%Y-%m-%d %H:%M:%S")
            log_text = f"[{time_str}] {log['user_name']} - {log['operation_type']}\n"
            log_text += f"    文件: {log.get('original_name', 'N/A')}\n"
            log_text += f"    详情: {log['details']}\n"
            log_text += f"    IP: {log['ip_address']}\n"
            log_text += "-" * 80 + "\n"
            
            text_widget.insert(tk.END, log_text)
        
        text_widget.config(state=tk.DISABLED)
    
    def open_file(self):
        """打开选中的文件"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择一个文件")
            return
        
        file_id = self.file_list.item(selection[0])['tags'][0]
        file_info = self.manager.get_file_info(file_id)
        
        if file_info:
            self.open_specific_file(file_info['file_path'])
    
    def open_specific_file(self, file_path: str):
        """打开指定文件"""
        try:
            if sys.platform == "win32":
                os.startfile(file_path)
            elif sys.platform == "darwin":
                os.system(f"open '{file_path}'")
            else:
                os.system(f"xdg-open '{file_path}'")
        except Exception as e:
            messagebox.showerror("错误", f"无法打开文件: {e}")
    
    def open_file_location(self, file_path: str):
        """打开文件所在文件夹"""
        try:
            folder_path = os.path.dirname(file_path)
            if sys.platform == "win32":
                os.startfile(folder_path)
            elif sys.platform == "darwin":
                os.system(f"open '{folder_path}'")
            else:
                os.system(f"xdg-open '{folder_path}'")
        except Exception as e:
            messagebox.showerror("错误", f"无法打开文件夹: {e}")
    
    def export_selected(self):
        """导出选中的文件"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择要导出的文件")
            return
        
        dest_folder = filedialog.askdirectory(title="选择导出目录")
        if not dest_folder:
            return
        
        for item in selection:
            file_id = self.file_list.item(item)['tags'][0]
            file_info = self.manager.get_file_info(file_id)
            
            if file_info:
                src_path = file_info['file_path']
                dest_path = os.path.join(dest_folder, file_info['original_name'])
                
                try:
                    shutil.copy2(src_path, dest_path)
                except Exception as e:
                    messagebox.showerror("错误", f"导出失败: {e}")
        
        messagebox.showinfo("成功", f"已导出 {len(selection)} 个文件")
    
    def delete_selected(self):
        """删除选中的文件"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择要删除的文件")
            return
        
        if not messagebox.askyesno("确认", f"确定要删除选中的 {len(selection)} 个文件吗？"):
            return
        
        for item in selection:
            file_id = self.file_list.item(item)['tags'][0]
            file_info = self.manager.get_file_info(file_id)
            
            if file_info:
                try:
                    # 删除文件
                    os.remove(file_info['file_path'])
                    
                    # 从数据库删除记录
                    with sqlite3.connect(self.manager.db.db_path) as conn:
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM files WHERE id = ?", (file_id,))
                        
                        # 记录删除操作
                        cursor.execute('''
                            INSERT INTO operations VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', (
                            str(uuid.uuid4()),
                            file_id,
                            'DELETE',
                            datetime.now().isoformat(),
                            getpass.getuser(),
                            self.manager.get_ip_address(),
                            f'删除文件: {file_info["original_name"]}'
                        ))
                        
                        conn.commit()
                    
                except Exception as e:
                    logger.error(f"删除文件失败: {e}")
        
        self.refresh_file_list()
        messagebox.showinfo("成功", f"已删除 {len(selection)} 个文件")
    
    def load_tags(self):
        """加载所有标签"""
        # 这里可以添加标签管理功能
        pass
    
    def reset_search(self):
        """重置搜索"""
        self.search_var.set("")
        self.refresh_file_list()
    
    def format_size(self, size_bytes: int) -> str:
        """格式化文件大小"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} PB"
    
    def batch_import(self):
        """批量导入文件"""
        folder = filedialog.askdirectory(title="选择要导入的文件夹")
        if not folder:
            return
        
        # 这里可以实现批量导入逻辑
        # 遍历文件夹中的所有文件，为每个文件弹出导入对话框
        pass
    
    def edit_tags(self):
        """编辑标签"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择一个文件")
            return
        
        file_id = self.file_list.item(selection[0])['tags'][0]
        file_info = self.manager.get_file_info(file_id)
        
        if not file_info:
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("编辑标签")
        dialog.geometry("400x300")
        
        ttk.Label(dialog, text="当前标签:").pack(pady=(20, 5), anchor=tk.W, padx=20)
        tags_entry = ttk.Entry(dialog, width=40)
        tags_entry.insert(0, ', '.join(file_info.get('tags', [])))
        tags_entry.pack(padx=20, pady=(0, 20))
        
        def save_tags():
            new_tags = [tag.strip() for tag in tags_entry.get().split(",") if tag.strip()]
            
            try:
                with sqlite3.connect(self.manager.db.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE files SET tags = ? WHERE id = ?", 
                                 (json.dumps(new_tags), file_id))
                    
                    # 记录操作
                    cursor.execute('''
                        INSERT INTO operations VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        str(uuid.uuid4()),
                        file_id,
                        'UPDATE_TAGS',
                        datetime.now().isoformat(),
                        getpass.getuser(),
                        self.manager.get_ip_address(),
                        f'更新标签: {file_info["original_name"]}'
                    ))
                    
                    conn.commit()
                
                messagebox.showinfo("成功", "标签更新成功")
                self.refresh_file_list()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("错误", f"更新失败: {e}")
        
        ttk.Button(dialog, text="保存", command=save_tags).pack(pady=20)
    
    def edit_description(self):
        """编辑文件描述"""
        selection = self.file_list.selection()
        if not selection:
            messagebox.showwarning("警告", "请先选择一个文件")
            return
    
        file_id = self.file_list.item(selection[0])['tags'][0]
        file_info = self.manager.get_file_info(file_id)
    
        if not file_info:
            return
    
        dialog = tk.Toplevel(self.root)
        dialog.title("编辑描述")
        dialog.geometry("500x300")
    
        ttk.Label(dialog, text="当前描述:").pack(pady=(20, 5), anchor=tk.W, padx=20)
    
        description_text = tk.Text(dialog, height=8, width=50)
        description_text.pack(padx=20, pady=(0, 10), fill=tk.BOTH, expand=True)
        description_text.insert("1.0", file_info.get('description', ''))
    
        def save_description():
            new_description = description_text.get("1.0", tk.END).strip()

            try:
                with sqlite3.connect(self.manager.db.db_path) as conn:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE files SET description = ? WHERE id = ?", 
                                 (new_description, file_id))
                
                    # 记录操作
                    cursor.execute('''
                        INSERT INTO operations VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        str(uuid.uuid4()),
                        file_id,
                        'UPDATE_DESCRIPTION',
                        datetime.now().isoformat(),
                        getpass.getuser(),
                        self.manager.get_ip_address(),
                        f'更新描述: {file_info["original_name"]}'
                    ))
                
                    conn.commit()
            
                messagebox.showinfo("成功", "描述更新成功")
                dialog.destroy()
            
            except Exception as e:
                messagebox.showerror("错误", f"更新失败: {e}")
    
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=20)
    
        ttk.Button(button_frame, text="保存", command=save_description).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="取消", command=dialog.destroy).pack(side=tk.LEFT, padx=10)

    def batch_rename(self):
        """批量重命名文件（待实现）"""
        messagebox.showinfo("提示", "批量重命名功能正在开发中，敬请期待！")

    def backup_database(self):
        """备份数据库"""
        backup_path = filedialog.asksaveasfilename(
            title="选择备份位置",
            defaultextension=".db",
            filetypes=[("数据库文件", "*.db"), ("所有文件", "*.*")]
        )
        
        if backup_path:
            try:
                shutil.copy2(self.manager.db.db_path, backup_path)
                messagebox.showinfo("成功", f"数据库已备份到: {backup_path}")
            except Exception as e:
                messagebox.showerror("错误", f"备份失败: {e}")
    
    def show_stats(self):
        """显示统计信息"""
        try:
            with sqlite3.connect(self.manager.db.db_path) as conn:
                cursor = conn.cursor()
                
                # 获取统计信息
                cursor.execute("SELECT COUNT(*) FROM files")
                total_files = cursor.fetchone()[0]
                
                cursor.execute("SELECT SUM(size) FROM files")
                total_size = cursor.fetchone()[0] or 0
                
                cursor.execute("SELECT file_type, COUNT(*) FROM files GROUP BY file_type")
                type_stats = cursor.fetchall()
                
                cursor.execute("SELECT COUNT(DISTINCT import_user) FROM files")
                total_users = cursor.fetchone()[0]
                
                # 显示统计信息
                stats_text = f"""
文件管理系统统计
================

文件总数: {total_files}
总大小: {self.format_size(total_size)}
用户数: {total_users}

按类型分布:
"""
                for file_type, count in type_stats:
                    stats_text += f"  {file_type}: {count} 个文件\n"
                
                stats_dialog = tk.Toplevel(self.root)
                stats_dialog.title("统计信息")
                stats_dialog.geometry("400x300")
                
                text_widget = scrolledtext.ScrolledText(stats_dialog, width=50, height=20)
                text_widget.insert(tk.END, stats_text.strip())
                text_widget.config(state=tk.DISABLED)
                text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
                
        except Exception as e:
            messagebox.showerror("错误", f"获取统计信息失败: {e}")
    
    def check_duplicates(self):
        """检查重复文件"""
        try:
            with sqlite3.connect(self.manager.db.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT hash_md5, GROUP_CONCAT(original_name, ', '), COUNT(*)
                    FROM files
                    GROUP BY hash_md5
                    HAVING COUNT(*) > 1
                ''')
                duplicates = cursor.fetchall()
                
                if not duplicates:
                    messagebox.showinfo("结果", "没有找到重复文件")
                    return
                
                # 显示重复文件
                dup_text = f"找到 {len(duplicates)} 组重复文件:\n\n"
                for hash_md5, files, count in duplicates:
                    dup_text += f"哈希: {hash_md5[:8]}...\n"
                    dup_text += f"重复数: {count}\n"
                    dup_text += f"文件: {files}\n"
                    dup_text += "-" * 50 + "\n"
                
                dup_dialog = tk.Toplevel(self.root)
                dup_dialog.title("重复文件检查")
                dup_dialog.geometry("600x500")
                
                text_widget = scrolledtext.ScrolledText(dup_dialog, width=80, height=30)
                text_widget.insert(tk.END, dup_text.strip())
                text_widget.config(state=tk.DISABLED)
                text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
                
        except Exception as e:
            messagebox.showerror("错误", f"检查重复文件失败: {e}")
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """
文件管理系统使用说明
===================

1. 导入文件
   - 拖放文件到窗口
   - 点击"导入文件"按钮
   - 输入描述和标签

2. 搜索文件
   - 在搜索框输入关键字
   - 使用"高级搜索"进行多条件搜索
   - 双击文件查看详情

3. 文件操作
   - 选择文件后点击对应按钮
   - 支持打开、导出、删除
   - 可以修改标签和描述

4. 数据管理
   - 所有数据自动保存
   - 支持数据库备份
   - 查看操作日志

5. 注意事项
   - 系统会自动去重（基于MD5哈希）
   - 文件按类型自动分类存储
   - 关闭程序后数据不会丢失
"""
        
        help_dialog = tk.Toplevel(self.root)
        help_dialog.title("使用说明")
        help_dialog.geometry("500x600")
        
        text_widget = scrolledtext.ScrolledText(help_dialog, width=60, height=40)
        text_widget.insert(tk.END, help_text.strip())
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    def show_about(self):
        """显示关于信息"""
        about_text = """
智能文件管理系统
版本: 1.0.0
作者: 李谨硕

功能特性:
- 拖放文件导入
- 自动分类存储
- 元数据记录
- 多种搜索方式
- 标签管理
- 操作日志
- 文件去重
- 数据持久化

技术支持: 请参考使用说明
"""
        messagebox.showinfo("关于", about_text.strip())
    
    def run(self):
        """运行GUI"""
        self.root.mainloop()

def main():
    """主函数"""
    try:
        # 检查必要的依赖
        try:
            import tkinterdnd2
        except ImportError:
            print("请先安装tkinterdnd2: pip install tkinterdnd2")
            return
        
        # 创建存储目录
        Path("storage").mkdir(exist_ok=True)
        
        # 启动应用程序
        app = FileManagerGUI()
        app.run()
        
    except Exception as e:
        logger.error(f"应用程序运行出错: {e}", exc_info=True)
        messagebox.showerror("错误", f"程序运行出错: {str(e)}")

if __name__ == "__main__":
    main()