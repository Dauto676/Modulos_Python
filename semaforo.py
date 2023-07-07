#pip install pywin32, pip install win32gui

import sys, os
import win32api, subprocess, win32event, winerror

executable_path = os.path.abspath(os.path.dirname(sys.argv[0]))

app_exe_path = os.path.join(executable_path, "app.exe")
# Define o nome do semáforo
SEMAPHORE_NAME = "Licenca.Exe"

# Cria um semáforo com valor inicial 1 (permitindo que um processo seja executado)
semaphore = win32event.CreateSemaphore(None, 1, 1, SEMAPHORE_NAME)

# Verifica se o semáforo já está sendo usado por outro processo
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    print("Outra instância do programa já está em execução.")
    # Sair aqui, se necessário
    exit()

else:
    # Executa o executável Flask em segundo plano
    process = subprocess.Popen([app_exe_path], 
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW)