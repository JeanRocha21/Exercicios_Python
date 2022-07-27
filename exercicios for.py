'''

Faça um programa que leia 5 números e informe a soma e a média dos números.

'''
soma = float(input('Digite um número'))
for n in range(2, 6):
    soma += float(input('Digite um número'))
    media = soma / n
    print(soma)
    print(media)