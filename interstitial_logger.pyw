import keyboard
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

# 在此修改你希望保存日志的本地绝对路径
LOG_FILE_PATH = r"D:\26SPRING\Project2-注意力跟踪\log\log.txt"
def log_entry():
    # 初始化主窗口并隐藏
    root = tk.Tk()
    root.withdraw()
    
    # 强制输入框置顶，避免被当前工作窗口遮挡
    root.attributes('-topmost', True) 
    
    # 呼出输入框
    user_input = simpledialog.askstring(
        title="间隙日志", 
        prompt="[刚才在做什么] + [触发转移的原因/情绪] -> [接下来准备转向哪里]", 
        parent=root
    )
    
    # 写入文件逻辑
    if user_input:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {user_input}\n")
            
    root.destroy()

# 绑定全局快捷键 Ctrl + Alt + J
keyboard.add_hotkey('ctrl+alt+j', log_entry)

# 挂起进程，保持后台监听
keyboard.wait()