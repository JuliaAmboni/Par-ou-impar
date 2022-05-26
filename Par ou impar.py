import random
print('Vamos jogar par ou impar!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
par = 'par'
impar = 'ímpar'
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
while True:
    valor = int(input('Escolha um valor: '))
    escolha = str(input('Escolha par ou impar: '))
    sorteio = random.choice(lista)
    resultado = (valor + sorteio)
    if resultado % 2 == 0:
        resultado = par
    else:
        resultado = impar

    if escolha == resultado:
        cont += 1
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você jogou {} e o computador jogou {}. DEU {}.'.format(valor, sorteio, resultado))
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    else:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você jogou {} e o computador jogou {}. DEU {}.\n'.format(valor, sorteio, resultado))
        print('GAME OVER !! Você venceu {} vezes.\n'.format(cont))
        break
