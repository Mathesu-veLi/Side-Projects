print('Você acorda em uma sala esquisita e não lembra de nada ... ', end='')
input('')
print('Até que você percebe uma vovó sentada em um dos cantos da sala ... ', end='')
input('')
print('V (Vovó): -Bom dia criança. Qual seu nome?')
nome = input('Digite seu nome: ')
print(f'V: -Ah, então você é o {nome} não é? ... ', end='')
input('')
print(f'V: -Sabia que você é bastante famoso? ... ', end='')
input('')
print(f'V: -O grande Aventureiro da Espada Noturna ... ', end='')
input('')
print(f'V: -Desculpe a pergunta meu bem, mas você é menino ou menina?')
while True:
    gen = input('Digite M para masculino e F para feminino: \033[m').strip().upper()
    if gen in 'MF':
        if gen in 'M':
            print('Então acertei, ainda bem ... ', end='')
            input('')
        else:
            print('Então permita-me corrigir meu erro ... ', end='')
            input('')
            print('A grande Aventureira da Espada Noturna ... ', end='')
            input('')
            print('Melhor agora, não? ... ', end='')
            input('')
        break
    else:
        print('\033[31m', end='')
input('')
