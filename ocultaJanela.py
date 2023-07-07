#pip install pywin32, pip install win32gui
import sys, os
import win32con, win32gui

executable_path = os.path.abspath(os.path.dirname(sys.argv[0]))

window_exe_name= os.path.join(executable_path, "app.exe")

# Espera a janela da aplicação aparecer
hwnd = None
while hwnd == None:
    hwnd = win32gui.FindWindow(None, window_exe_name) #localiza a janela que deve esconder
win32gui.ShowWindow(hwnd, win32con.SW_HIDE) #Define a janela como escondida
