from tkinter import *

janela = Tk()
janela.title('Send Trojan')

textoDeOrientacao = Label(janela, text='Envie 1 mensagem varias vezes!')
textoDeOrientacao.pack(side=TOP)
msgLabel = Label(janela, text='Mensagem a ser enviada')
msgLabel.pack(side=LEFT)
msg = Entry(master=janela)
msg.pack(side=RIGHT)
vezesLabel = Label(janela, text='Vezes que ela será enviada')
vezesLabel.pack(side=LEFT)
vezes = Entry(janela)
vezes.pack(side=RIGHT)
janela.mainloop()