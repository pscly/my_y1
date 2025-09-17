# coding: utf-8
"""
热键后台监听器

功能：
- 后台常驻监听全局热键；按 Alt+F1 唤起主界面（新控制台启动 浏览器.py）
- 按 Alt+Shift+F2 退出监听器

使用建议：
- 使用 pythonw.exe 启动本脚本可实现“无控制台”后台运行
"""

import sys
import subprocess
from pathlib import Path

import win32api
import win32con
import win32gui


class HotkeyListener:
    """基于 Win32 全局热键的监听器"""

    def __init__(self):
        self.ui_proc = None  # 保存主界面子进程句柄

        # 注册窗口类并创建隐藏窗口，用于接收 WM_HOTKEY 消息
        message_map = {
            win32con.WM_HOTKEY: self.on_hotkey,
            win32con.WM_DESTROY: self.on_destroy,
        }

        wc = win32gui.WNDCLASS()
        wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "my_y1_hotkey_listener"
        wc.lpfnWndProc = message_map

        self.classAtom = win32gui.RegisterClass(wc)
        self.hwnd = win32gui.CreateWindowEx(
            0,
            self.classAtom,
            "my_y1_hotkey_listener",
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            wc.hInstance,
            None,
        )

        # 注册全局热键：Alt+F1（唤醒），Alt+Shift+F2（退出）
        self.HOTKEY_SHOW_ID = 1
        self.HOTKEY_EXIT_ID = 2
        win32gui.RegisterHotKey(self.hwnd, self.HOTKEY_SHOW_ID, win32con.MOD_ALT, win32con.VK_F1)
        win32gui.RegisterHotKey(
            self.hwnd, self.HOTKEY_EXIT_ID, win32con.MOD_ALT | win32con.MOD_SHIFT, win32con.VK_F2
        )

    def on_hotkey(self, hwnd, msg, wparam, lparam):
        """处理热键事件"""
        if wparam == self.HOTKEY_SHOW_ID:
            self.launch_ui()
        elif wparam == self.HOTKEY_EXIT_ID:
            # 退出监听器
            win32gui.DestroyWindow(self.hwnd)
        return 0

    def on_destroy(self, hwnd, msg, wparam, lparam):
        """清理热键并退出消息循环"""
        try:
            win32gui.UnregisterHotKey(self.hwnd, self.HOTKEY_SHOW_ID)
        except Exception:
            ...
        try:
            win32gui.UnregisterHotKey(self.hwnd, self.HOTKEY_EXIT_ID)
        except Exception:
            ...
        win32gui.PostQuitMessage(0)
        return 0

    def launch_ui(self):
        """如果主界面未运行，则新开控制台运行 浏览器.py"""
        # 若已存在且仍在运行，则不重复打开
        if self.ui_proc is not None and self.ui_proc.poll() is None:
            return

        repo_root = Path(__file__).resolve().parent
        target = str(repo_root / "浏览器.py")

        # 在新控制台中启动主界面
        CREATE_NEW_CONSOLE = 0x00000010
        self.ui_proc = subprocess.Popen(
            [sys.executable, target], cwd=str(repo_root), creationflags=CREATE_NEW_CONSOLE
        )


def main():
    listener = HotkeyListener()
    # 消息循环（隐藏窗口，不会显示界面）
    win32gui.PumpMessages()


if __name__ == "__main__":
    main()
