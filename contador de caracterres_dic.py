def contar_caracteres(s):
    '''
    Função que conta os caracteres de uma string

    >>> contar_caracteres('jean')
    {'a': 1, 'e': 1, 'j': 1, 'n': 1}

    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    '''

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('jean'))
    print()
    print(contar_caracteres('banana'))

