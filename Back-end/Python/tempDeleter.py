import os, shutil, platform, win32com.client, pythoncom, tkinter, tkinter.filedialog
from tkinter.tix import Tree
import customtkinter as ctk

dir = os.path.expanduser('~').replace("\\", "/")+'/AppData/Local/Temp'
dir2 = "C:\Windows\Temp"
shutil.rmtree(dir, ignore_errors=True)
shutil.rmtree(dir2, ignore_errors=True)

def startup():
    startuppath = os.path.expanduser('~').replace("\\", "/")+r"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    path = os.path.join(startuppath, "Temp deleter.lnk")
    target = rf"{tkinter.filedialog.askopenfilename(title='Selecione o arquivo do Temp deleter')}"
    print(target)
    
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = target
    shortcut.save()
    quit()
file = os.path.exists(os.path.expanduser('~').replace("\\", "/")+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Temp deleter.lnk")
if file == False:
    window = ctk.CTk()
    window.title("Temp Deleter")
    window.geometry("300x100")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    label = ctk.CTkLabel(master=window,
                        text=f"Deseja iniciar 'Temp Deleter' \nautomaticamente ao inicializar o {platform.system()}?",
                        width=100,
                        height=30,
                        corner_radius=8,
                        text_color=("black"))
    label.place(x=150, y= 20, anchor=ctk.CENTER)
    button = ctk.CTkButton(master=window,
                        text="Sim",
                        fg_color="#1fd655",
                        width=100,
                            height=32,
                            command=startup,
                        text_color=("black"))
    button.place(x=80, y=70, anchor=ctk.CENTER)
    button1 = ctk.CTkButton(master=window,
                            text='Não',
                            fg_color="#f20d0d",
                            width=100,
                            height=32,
                            text_color=("black"),
                            command=quit)
    button1.place(x=220, y=70, anchor=ctk.CENTER)
    window.mainloop()
