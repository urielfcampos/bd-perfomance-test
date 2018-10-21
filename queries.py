#coding: utf-8
import shelve

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
    :return: (tmp_fname, filt_reg)
    [filt_reg]: Array de registros filtrados
    """

    # Filtrar por itens no select
    sel_array = [(32, 40), (0, 1)]
    select = []  # Armazena strings de bits (cada dado), separadas por vírgula
    for reg in array_reg: select.append(','.join(map(str, filter_select(sel_array, reg))))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    print(select)
    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: dic[data] = 1 if data not in dic else dic[data] + 1

    # Preparar array de chaves e valor para retornar
    result = []
    for key in dic.keys(): result.append([key, dic[key]])
    dic.close()
    return result

# Testes:
print(querie_1(test_array, 'tmp.bin'))