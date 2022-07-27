"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.

"""
import math

def calculo (m2):
    calculo = int(m2)
    lata = 18
    galao = 3.6
    m2_porlitro = 6
    valor_lata = 80.00
    valor_galao = 25.00

    area = calculo / m2_porlitro
    lata_necessaria = area / lata
    galao_necessario = float(area) / galao
    disperdicio = float(area) / 21.6
    lata_disperdicio = disperdicio
    galao_disperdicio = disperdicio
    compra_lata = lata_necessaria * valor_lata
    compra_galao = galao_necessario * valor_galao
    compra_disperdiciolata = lata_disperdicio * valor_lata
    compra_disperdiciogalao = galao_disperdicio * valor_galao
    latasegaloes = compra_disperdiciogalao + compra_disperdiciolata

    print(f'Area total {calculo} m²')
    print(f'{area:.2f} litros necessários')
    print(f'Latas necessárias de 18 litros: {lata_necessaria:.2f}')
    print(f'Galões necessários de 3,6 litros: {galao_necessario:.2f}')
    print(f'Custos de compras de apenas latas: R${compra_lata:.2f}')
    print(f'Custos de compras de apenas galões: R${compra_galao:.2f}')
    print(f'Compra de latas e galões: R${latasegaloes:.2f}')


m2 = input('Metros Quadrados da area:')
calculo(m2)


