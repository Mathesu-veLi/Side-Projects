from tkinter import *
import tkinter.ttk as tkk
import tkinter.messagebox
import pyautogui, keyboard


bC = '#3f3f3f'



def flood():
    global f2
    if msg.get() != '' and vezes.get() != '' and vezes.get() != '0':
        try:
            f2.destroy()
            f2 = Label(master= janela, text='Aperte F2 para começar a flodar!', fg='green', bg=bC)
        except:
            f2 = Label(master= janela, text='Aperte F2 para começar a flodar!', fg='green', bg=bC)
        finally:
            f2.pack(side=BOTTOM)
        while True:
            if keyboard.is_pressed('f2'):
                for c in range(0, int(vezes.get()) + 1):
                    pyautogui.write(f'{msg.get()} {c}')
                    pyautogui.press('enter')
                    if keyboard.is_pressed('esc'):
                        break
                break
    else:
        if msg.get() == '' or msg.get() == None:
            tkinter.messagebox.showerror('Error!', 'Digite uma mensagem para começar a enviar!')
        if vezes.get() == '' or vezes.get() == None:
            tkinter.messagebox.showerror('Error!', 'Digite o número de vezes que a mensagem será enviada para começar a envia-las!')
        elif vezes.get() == '0':
            tkinter.messagebox.showerror('Error!', 'Não posso enviar um número 0 de vezes!')

janela = Tk()
janela.configure(background=bC)
janela.geometry("330x190")
janela.title('Send Trojan')
janela.resizable(width=False, height=False)
style = tkk.Style()
style.configure("Label", foreground="white", background=bC)
textoDeOrientacao = tkk.Label(janela, text='Envie 1 mensagem varias vezes!', style="Label")
textoDeOrientacao.pack(side=TOP, pady=5)
msgLabel = tkk.Label(janela, text='Mensagem a ser enviada:', style="Label")
msgLabel.place(x=5, y=50)
msg = Entry(master=janela, bg='#2f2f2f', fg='white')
msg.place(x=180, y=50)
msg.config(highlightbackground=bC)
vezesLabel = tkk.Label(janela, text='Vezes que ela será enviada:', style="Label")
vezesLabel.place(x=5, y=90)
vezes = Entry(janela, bg='#2f2f2f', fg='white')
vezes.place(x=180, y=90)
vezes.config(highlightbackground=bC)
confirmButtom = Button(janela, text='Começar a enviar!', bg='blue', fg='white', activebackground='#2f2f2f', activeforeground='#7FFFD4' , command=flood, borderwidth=5)
confirmButtom.pack(side=BOTTOM, pady=5)
janela.mainloop()