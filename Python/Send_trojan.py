from customtkinter import *
import pyautogui, keyboard

def flood():
    if msg.get() != '' and vezes.get() != '' and vezes.get != '0':
        while True:
            f2 = CTkLabel(master= janela, text='                    Aperte F2 para começar a flodar!            \n  ', text_color='green')
            f2.place(x=20, y=125)
            if keyboard.is_pressed('f2'):
                for c in range(0, int(vezes.get()) + 1):
                    pyautogui.write(f'{msg.get()} {c}')
                    pyautogui.press('enter')
                    if keyboard.is_pressed('esc'):
                        break
                break
    else:
        if msg.get() == '':
            try:
                error.destroy()
            except:
                error = CTkLabel(master=janela, text='Digite uma mensagem para começar a enviar!     \n ', text_color='red')
                error.place(x=30, y=125)
        if vezes.get() == '':
            try:
                error.destroy()
            except:
                error = CTkLabel(master=janela, text='Digite o número de vezes que a mensagem será\nenviada para começar a envia-las!', text_color='red')
                error.place(x=30, y=125)
        elif vezes.get() == '0':
            try:
                error.destroy()
            except:
                error = CTkLabel(master=janela, text='Não posso enviar um número 0 de vezes!', text_color='red')
                error.place(x=30, y=125)

janela = CTk()
janela.geometry("330x190")
janela.title('Send Trojan')
set_default_color_theme("dark-blue") 
textoDeOrientacao = CTkLabel(janela, text='Envie 1 mensagem varias vezes!')
textoDeOrientacao.pack(side=TOP)
msgLabel = CTkLabel(janela, text='Mensagem a ser enviada:')
msgLabel.place(x=5, y=50)
msg = CTkEntry(master=janela)
msg.place(x=180, y=50)
vezesLabel = CTkLabel(janela, text='Vezes que ela será enviada:')
vezesLabel.place(x=5, y=90)
vezes = CTkEntry(janela)
vezes.place(x=180, y=90)
confirmButtom = CTkButton(janela, text='Começar a enviar!', command=flood)
confirmButtom.pack(side=BOTTOM, pady=5)
janela.mainloop()