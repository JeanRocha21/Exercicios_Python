'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e
quatro notas de 1.

'''

valor_do_saque = int(input('Valor do saque: R$ '))

nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0
if valor_do_saque < 10:
    print('Saques a partir de R$10,00')
if valor_do_saque > 600:
    print('Saques até R$600,00')

valor, valor_do_saque = divmod(valor_do_saque, 100)
if valor == 1:
    nota_100 += 1
elif valor > 1:
    nota_100 += valor

valor2, valor_do_saque = divmod(valor_do_saque, 10)

if valor2 >= 5:
    nota_50 = 1
    nota_10 += valor2 - 5
elif valor2 < 5:
    nota_10 += valor2

if valor_do_saque >= 5:
    nota_5 += 1
    nota_1 += valor_do_saque - 5
elif valor_do_saque < 5:
    nota_1 += valor_do_saque

print(f' Notas de R$100,00: {nota_100}')
print(f' Notas de R$50,00: {nota_50}')
print(f' Notas de R$10,00: {nota_10}')
print(f' Notas de R$5,00: {nota_5}')
print(f' Notas de R$1,00: {nota_1}')
