import pyautogui, keyboard

msg = input('Qual mensagem deseja enviar?: ')
quant = int(input('Quantas vezes deseja envia-la?: '))
print('Para começar a enviar, aperte a tecla F2 do seu teclado! (Pressione a tecla Esc para parar)')
while True:
    if keyboard.is_pressed('f2'):
        for c in range(0, quant + 1):
            pyautogui.write(f'{msg} {c}')
            pyautogui.press('enter')
            if keyboard.is_pressed('esc'):
                break
        break