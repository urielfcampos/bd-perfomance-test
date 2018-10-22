#coding: utf-8
import shelve

# Dicionário de condições
_cmps = {
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '=': lambda a, b: a == b,
    '>=': lambda a, b: a >= b,
    '>': lambda a, b: a > b,
}

test_array = [
 '0101110001110000011100000110000011010001000000000011000000001010',
 '0101001010111110000110001010110001101011000000000101000000000010',
 '0000010011011001011101111010111110100110000000001110000000001110',
 '0100101110011110101010011001101100101001000000001101000000000101',
 '0010000001011010010110011001010110001101000000001000000000001010',
 '0100111100101110011000010010101001010010000000000110000000001101',
 '0111111001100001100011101011110101111100000000001100000000001001',
 '1010110101000010111111101100110001110010000000001001000000000110',
 '1111110110110111001010111100001001000001000000001001000000000110',
 '1000100000011000100011001001100011010010000000000010000000001110',
 '0001010110010000001001011110110110000100000000000111000000000001',
 '1011111000110111011001001101110101101101000000001100000000000110',
 '1111111011111111011011010111101011110111000000001101000000000100',
 '1110011000001111000001000100101001010111000000000100000000000111']

"""
1 bit sexo, 7-bits idade, 10-bits renda, 2-bits escolaridade, 
12 -bits idioma, 8-bits país, 24-bits localizador

Array de marcação de bits iniciais do atributos listados acima:
[0, 1, 8, 18, 20, 32, 40, 52, 64]
"""

def filter_select(sel_array, reg):
    """
    Filtra o select dado uma lista de intervalos de bits
    :param sel_array:
    :return: lista de dados convertidos para decimal
    """
    strings = []
    for item in sel_array: strings.append(int(reg[item[0]:item[1]], 2))
    return strings

def querie_1(array_reg, tmp_fname):
    """
    Executa primeira querie / Executes first querie
    :param array_reg: lista de strings de bits.
    :param tmp_fname: nome do arquivo temporário
    """
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: dic[data] = 1 if data not in dic else dic[data] + 1
    dic.close()

def querie_2(array_reg, tmp_fname):
    """
    Executa primeira querie / Executes first querie
    :param array_reg: lista de strings de bits.
    :param tmp_fname: nome do arquivo temporário
    """
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1), (1, 8)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: dic[data] = 1 if data not in dic else dic[data] + 1
    for key in dic.keys(): print(key, '-', dic[key])
    dic.close()

def querie_3_4(array_reg, choice, tmp_fname):
    """
    Executa primeira querie / Executes first querie
    :param array_reg: lista de strings de bits.
    :param tmp_fname: nome do arquivo temporário
    :param choice: 'salario' ou 'idade'
    """
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1), (8, 18)] if choice is 'salario' else [(32, 40), (0, 1), (1, 8)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    # Calcular média do salário ou idade
    sum = 0
    for data in select: sum += int(data[-1])
    # for key in dic.keys(): print(key, '-', dic[key])
    # print('Media:', sum / len(dic.keys()))
    dic.close()

def querie_5(array_reg, tmp_fname, condition):
    """
    Executa primeira querie / Executes first querie
    :param array_reg: lista de strings de bits.
    :param tmp_fname: nome do arquivo temporário
    :param condition: (lista) condition = [(lo, hi), '<|<=|=|>=|>', number]
    onde:
        *lo = limite inferior. hi = limite superior;
        *(lo, hi) = um intervalo de bits | [lo, hi[;
        *'<|<=|=|>=|>': Uma das opções entre aspas (exemplo: '<')
        *number = inteiro qualquer
    """
    cmp = _cmps[condition[1]]
    lo = condition[0][0]; hi = condition[0][1]
    n = condition[2]

    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg:
        if cmp(int(reg[lo:hi] ,2), n):
            select.append(','.join(map(str, filter_select(sel_array, reg))))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: dic[data] = 1 if data not in dic else dic[data] + 1
    for key in dic.keys(): print(key, '-', dic[key])
    dic.close()

# Testes:
querie_5(test_array, 'tmp1.bin', [(32, 40), '>', 15])