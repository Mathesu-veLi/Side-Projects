from random import randint

num = randint(1, 10)
menos = randint(1, num) #numero menor que num
dica2 = num - menos

if num >= 5:
    dica1 = 'igual ou maior'
else:
    dica1 = 'menor'

print('O computador escolheu um número de 1 a 10.')
print(f'O número que ele escolheu é {dica1} que 5 e esse número menos {menos} é igual {dica2}')
resp = int(input('Qual o número que o computador escolheu?: '))

if resp == num:
    print('Parabéns, você acertou!')
else:
    print(f'Você errou! O número era {num}. Tente novamente! ')
