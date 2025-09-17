@echo off
setlocal

REM 使用 UTF-8 代码页，避免中文提示乱码
chcp 65001 >nul

set "SCRIPT=hotkey_runner.py"

REM 1) 若存在 uv，则优先使用 uv 虚拟环境运行（隐藏窗口）
where uv >nul 2>nul
if %errorlevel%==0 (
    powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -Command "Start-Process uv -ArgumentList 'run','python','%SCRIPT%' -WindowStyle Hidden"
    goto :done
)

REM 2) 常见 venv 目录：.venv / venv（优先 pythonw.exe）
if exist ".venv\Scripts\pythonw.exe" (
    start "" ".venv\Scripts\pythonw.exe" "%SCRIPT%"
    goto :done
)
if exist ".venv\Scripts\python.exe" (
    start /min "" ".venv\Scripts\python.exe" "%SCRIPT%"
    goto :done
)
if exist "venv\Scripts\pythonw.exe" (
    start "" "venv\Scripts\pythonw.exe" "%SCRIPT%"
    goto :done
)
if exist "venv\Scripts\python.exe" (
    start /min "" "venv\Scripts\python.exe" "%SCRIPT%"
    goto :done
)

REM 3) 若已激活 venv（VIRTUAL_ENV），尝试使用其中的 pythonw/python
if defined VIRTUAL_ENV (
    if exist "%VIRTUAL_ENV%\Scripts\pythonw.exe" (
        start "" "%VIRTUAL_ENV%\Scripts\pythonw.exe" "%SCRIPT%"
        goto :done
    )
    if exist "%VIRTUAL_ENV%\Scripts\python.exe" (
        start /min "" "%VIRTUAL_ENV%\Scripts\python.exe" "%SCRIPT%"
        goto :done
    )
)

REM 4) 兜底：系统 pythonw/python
where pythonw >nul 2>nul
if %errorlevel%==0 (
    start "" pythonw "%SCRIPT%"
    goto :done
)

start /min "" python "%SCRIPT%"

:done
echo 已在后台启动热键监听器（Alt+F1 唤醒，Alt+Shift+F2 退出）。
exit /b 0

