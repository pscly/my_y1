# 主要是想使用wt 代替cmd

import os 

# os.system('conda')
gn = r'''%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\Anaconda3' "'''

os.startfile(gn)

