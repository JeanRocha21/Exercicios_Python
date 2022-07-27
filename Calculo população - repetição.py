'''
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
que calcule e escreva o número de anos necessários para que a população do
país A ultrapasse ou iguale a população do país B, mantidas as taxas de
crescimento.
'''

paisa = 80000
paisb = 200000
taxaa = 1.03
taxab = 1.015
anos = 0

while paisa < paisb:
    anos += 1
    paisa *= taxaa
    paisb *= taxab
    paisa = int(paisa)
    paisb = int(paisb)
print(f'População País A {paisa}')
print(f'População País B {paisb}')
print(anos)