from bitarray import bitarray

# Lista com os tamanhos de cada dado (em bits)
maxb_a = [1, 7, 10, 2, 12, 8, 12, 12]

l = [0, 90, 100, 3, 2000, 255, 100, 4090]


def bitline(l):
    """
    pt_br: Converte uma lista de dados em uma linha de 64-bits.
    en: Converts a data list to a 64-bit line.
    :param l: lista de dados / data list
    :return: string com 64 caracteres 0s e 1s.
    """
    global maxb_a
    li = list(zip(l, maxb_a))  # Lista de pares de l com maxb_a
    s = ''  # Iniciar string
    for d in li:
        b = bin(d[0])[2:]  # Obter o valor binário de cada número
        # Preenche com 0s os valores para o tamanho correto
        s += '0' * (d[1] - len(b)) + b
    return s


def cdataline(s):
    """
    cdataline = concrete data line
    :param s:
    :return:
    """
    global maxb_a

    # Iniciar os vetores com os limites
    zs_array = [0]
    for e in maxb_a:
        u = zs_array[-1]
        prox = u + e
        zs_array.append(prox)
    zs_cpy = zs_array[:]
    zs_array.pop(-1)  # [0, 1, 8, 18, 20, 32, 40, 52]
    zs_cpy.pop(0)  # [1, 8, 18, 20, 32, 40, 52, 64]

    # Gerar vetor de dados a partir da string de bits
    dataset = []
    for i in range(len(zs_array)):
        x = zs_array[i]  # limite inferior
        y = zs_cpy[i]  # limite superior
        dataset.append(int(s[x:y], 2))
    return dataset


def w_file(file, s_bits):
    """
    pt_br: Escreve uma string representando 64 bits em um arquivo
    en: Writes a 64-bit-like string to a file
    :param file: arquivo
    :param s_bits: string de bits
    """
    with open(file, 'wb') as f:
        bitarray(s_bits).tofile(f)


def r_file(file):
    """
    pt_br: Lê de arquivo e retorna a linha de bits correspondente
    :param file:
    :return:
    """
    a = bitarray()
    with open(file, 'rb') as f:
        a.fromfile(f)
        s = ''
        for d in a.tolist(): s += '0' if d is False else '1'
        return s

"""
# Testes:
s = bitline(l)
print(s)
w_file('bdb', s)
line = r_file('bdb')
print(cdataline(line))
"""
