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
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))

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
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1), (1, 8)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))

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
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória
    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1), (8, 18)] if choice is 'salario' else [(32, 40), (0, 1), (1, 8)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))

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
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória
    cmp = _cmps[condition[1]]
    lo = condition[0][0]; hi = condition[0][1]
    n = condition[2]

    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg:
        if cmp(int(reg[lo:hi] ,2), n):
            select.append(','.join(map(str, filter_select(sel_array, reg))))

    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: dic[data] = 1 if data not in dic else dic[data] + 1
    for key in dic.keys(): print(key, '-', dic[key])
    dic.close()

# Testes:

#querie_5(test_array, 'tmp.bin', [(32, 40), '>', 15])
