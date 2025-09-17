@echo off
REM 以“无控制台”方式在后台运行热键监听器（Alt+F1 唤醒主界面，Alt+F2 退出监听器）

REM 优先使用 pythonw.exe，若未配置则退回到常规 python（窗口最小化）
where pythonw >nul 2>nul
if %errorlevel%==0 (
    start "" python hotkey_runner.py
) else (
    start /min "" python hotkey_runner.py
)

echo 已在后台启动热键监听器（Alt+F1 唤醒，Alt+Shift+F2 退出）。
exit /b 0
