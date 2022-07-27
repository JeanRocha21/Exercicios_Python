def contar_caracteres(s):
    '''
    Função que conta os caracteres de uma string

    >>> contar_caracteres('jean')
    a: 1
    e: 1
    j: 1
    n: 1

    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada

    '''

    caracteres_ordenados = sorted(s)

    caracteres_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_anterior:
            contagem += 1
        else:
            print(f'{caracteres_anterior}: {contagem}')
            caracteres_anterior = caracter
            contagem = 1

    print(f'{caracteres_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('Jean')
    print()
    contar_caracteres('banana')
