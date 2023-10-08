import customtkinter as ctk
import tkinter as tk
import tkinter.filedialog as fd
import os

#Salvar a senha
def salvarsenha():
    #Mensagem de Erro ou Sucesso
    try:
        output
    except NameError:
        output_exists = False
    else:
        output_exists = True
    if output_exists == True:
        output.destroy()
    if emailfield.get() and sitefield.get() and senhafield.get() and pathfield.get() != '':
        #Salvar a senha (de verdade agora)
        completetxtcreate = os.path.join(pathfield.get(), sitefield.get() + '.txt')
        senha = open(completetxtcreate, "w+")
        senha.write(f"Email: {emailfield.get()}\n")
        senha.write(f"Senha: {senhafield.get()}") 
        output = ctk.CTkLabel(master=janela,
                               text="Senha salva com sucesso!",
                               width=300,
                               height=26,
                               text_color=("green"),
                               corner_radius=5)
    else:
        output = ctk.CTkLabel(master=janela,
                               text="Por favor, preencha todos os campos acima \nantes de clicar em 'Salvar Senha'!",
                               width=120,
                               height=25,
                               text_color=("red"),
                               corner_radius=5)
    output.place(x=180, y=260, anchor=tk.CENTER)
#Localizar diretorio
def locatepath():
    path = fd.askdirectory()
    pathfield.insert(0, path)
    savedirectorycomplete = os.path.join('C:/', 'lastdirectoryselected.txt')
    savedirectory = open(savedirectorycomplete, "w+")
    savedirectory.write(pathfield.get())
#Aparencia
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
#Criação de janela
janela = ctk.CTk()  
janela.geometry("360x320")
janela.title("Password Saver")
#Apresentação de Função do Aplicativo
label = ctk.CTkLabel(master=janela,
                     text="Digite abaixo o nome do site que queres salvar a senha, \no email cadastrado no mesmo e a senha para \nsalvar-la em um diretorio de sua escolha",
                     width=120,
                     height=25,
                     text_color=("white"),
                     corner_radius=8)
label.place(x=180, y=10, anchor=tk.N)
#Site
sitelabel = ctk.CTkLabel(master=janela,
                     text='Site:',
                     width=65,
                     height=40,
                     text_color=("white"),
                     corner_radius=0)
sitelabel.place(x=100, y=100, anchor=tk.CENTER)
sitefield = ctk.CTkEntry(master=janela,
                         placeholder_text="'Netflix'",
                         width=200,
                         height=40,
                         border_width=2,
                         corner_radius=10)
sitefield.place(x=232, y=100, anchor=tk.CENTER)

#E-mail
emaillabel = ctk.CTkLabel(master=janela,
                     text='E-mail:',
                     width=65,
                     height=40,
                     text_color=("white"),
                     corner_radius=0)
emaillabel.place(x=100, y=140, anchor=tk.CENTER)
emailfield = ctk.CTkEntry(master=janela,
                          placeholder_text="'mathesuvelizinho@gmail.com'",
                          width=200,
                          height=40,
                          border_width=2,
                          corner_radius=10)
emailfield.place(x=232, y=140, anchor=tk.CENTER)
#Senha
senhalabel = ctk.CTkLabel(master=janela,
                     text='Senha:',
                     width=65,
                     height=40,
                     text_color=("white"),
                     corner_radius=0)
senhalabel.place(x=100, y=180, anchor=tk.CENTER)
senhafield = ctk.CTkEntry(master=janela,
                          placeholder_text="'*******'",
                          width=200,
                          height=40,
                          border_width=2,
                          corner_radius=10)
senhafield.place(x=232, y=180, anchor=tk.CENTER)
#Local de salvamento
pathlabel = ctk.CTkLabel(master=janela, text='Local de salvamento:', width=65, height=40, text_color=("white"), corner_radius=0)
pathlabel.place(x=142, y=220, anchor=tk.CENTER)
pathfield = ctk.CTkEntry(master=janela, placeholder_text="'C:/Users/User_name/Documents/Passwords'", width=105, height=40, border_width=2, corner_radius=10)
pathfield.place(x=260, y=220, anchor=tk.CENTER)
pathlocatebutton = ctk.CTkButton(master=janela, width=30, height=30, border_width=0, corner_radius=4, text="...", fg_color=("white"), text_color=("black"), text_font=('Times New Roman', 12), command=locatepath)
pathlocatebutton.place(x=315, y=205)
if os.path.exists('C:/lastdirectoryselected.txt') == True:
    savedirectory = open('C:/lastdirectoryselected.txt', "r")
    lsavedirectory = savedirectory.readline()
    pathfield.insert(0, lsavedirectory)
#Botão para salvar senha
finallybutton = ctk.CTkButton(master=janela,
                              width=120,
                              height=32,
                              border_width=0,
                              corner_radius=8,
                              text="Salvar senha",
                              command=salvarsenha)
finallybutton.place(x=180, y=300, anchor=tk.CENTER)
janela.mainloop()