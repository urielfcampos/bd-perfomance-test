#coding: utf-8
import shelve

def querie_1(array_reg, tmp_fname):
    """
    Executa primeira querie / Executes first querie
    :param array_reg: array de registros de dados legíveis.
    :param tmp_fname: nome do arquivo temporário
    :return: (tmp_fname, filt_reg)
    [filt_reg]: Array de registros filtrados
    """

    # Filtrar por itens no select
    sel_array = [5, 0]
    select = []
    for reg in array_reg: select.append(','.join(map(str, [reg[j] for j in sel_array])))
    dic = shelve.open(tmp_fname)  # Associar dicionário a arquivo na memória

    """ Salvar os resultados na querie
    salvar contador do registro como 1 se ainda não existe no dicionário,
    caso contrário, salve como valor anterior + 1. """
    for data in select: print(data); dic[data] = 1 if data not in dic else dic[data] + 1

    # Preparar array de chaves e valor para retornar
    result = []
    for key in dic.keys(): result.append([key, dic[key]])
    dic.close()
    return result

array = [
[0, 92, 449, 3, 96, 209, 3, 10],
[0, 82, 760, 1, 2220, 107, 5, 2],
[0, 4, 869, 3, 1967, 166, 14, 14],
[0, 75, 634, 2, 2459, 41, 13, 5],
[0, 32, 361, 1, 2453, 141, 8, 10],
[0, 79, 185, 2, 298, 82, 6, 13],
[0, 126, 390, 0, 3773, 124, 12, 9],
[1, 45, 267, 3, 3788, 114, 9, 6],
[1, 125, 732, 2, 3010, 65, 9, 6],
[1, 8, 98, 0, 3224, 210, 2, 14],
[0, 21, 576, 2, 1517, 132, 7, 1],
[1, 62, 221, 2, 1245, 109, 12, 6],
[1, 126, 1021, 2, 3450, 247, 13, 4],
[1, 102, 60, 0, 1098, 87, 4, 7],
[1, 2, 1009, 1, 546, 253, 14, 0],
[1, 84, 672, 0, 1605, 143, 12, 9],
[1, 4, 184, 1, 4091, 252, 3, 4],
[0, 112, 944, 3, 2179, 250, 11, 2],
[1, 6, 160, 1, 3364, 146, 12, 12],
[0, 75, 972, 0, 2470, 79, 13, 8],
[1, 114, 363, 2, 2080, 28, 0, 12],
[0, 80, 459, 0, 3003, 122, 0, 1],
[0, 99, 695, 3, 1219, 78, 6, 2],
[0, 124, 479, 3, 4002, 153, 14, 4],
]

print(querie_1(array, 'tmp.bin'))