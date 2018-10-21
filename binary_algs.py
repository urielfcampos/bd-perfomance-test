from bitarray import bitarray
import shelve
import threading
# Lista com os tamanhos de cada dado (em bits)
maxb_a = [1, 7, 10, 2, 12, 8, 12, 12]

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
        b = bin(d[0])[2:]  # Obter o valor binario de cada numero
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
    with open(file, 'ab') as f:
       bitarray(s_bits).tofile(f)


def r_file(start, stop, file):
    """
    pt_br: Lê arquivo e retorna a linha de bits correspondente,
    no intervalo provido [start, stop[, com start e stop
    em registros de 8 bytes.
    :param file: arquivo a ser lido
    :param start: ponto do início de leitura
    :param stop: ponto de fim
    :return:
    """
    with open(file, 'rb') as f:
        s_array = []
        f.seek(start, 0)
        bts = f.read(8)
        currnt_position = start
        while bts and currnt_position < stop:
            a = bitarray()
            a.frombytes(bts)
            s = a.to01()
            s_array.append(s)
            #for d in a.tolist(): s += '0' if d is False else '1'
            f.seek(0, 1)
            bts = f.read(8)

            currnt_position = f.tell()
            if len(s_array)==10000:
                write_temp(s_array)
                s_array.clear()

def write_temp(s_array):
    threadName=threading.currentThread().getName()
    with shelve.open(f'tmp_cda{threadName}', "c")as f:
        for x in range(len(s_array)//10):
            f[str(hash(s_array[x]))] = s_array[x]
            f[str(hash(s_array[x+1]))] = s_array[x+1]
            f[str(hash(s_array[x+2]))] = s_array[x+2]
            f[str(hash(s_array[x+3]))] = s_array[x+3]
            f[str(hash(s_array[x+4]))] = s_array[x+4]
            f[str(hash(s_array[x+5]))] = s_array[x+5]
            f[str(hash(s_array[x+6]))] = s_array[x+6]
            f[str(hash(s_array[x+7]))] = s_array[x+7]
            f[str(hash(s_array[x+8]))] = s_array[x+8]
            f[str(hash(s_array[x+9]))] = s_array[x+9]
        f.close()





# # Testes:
r_file(1000, 1024, "bdb.bin")
# for l in lines: print(cdataline(l))
#lines = r_file("bdb.bin")
#print(lines)
#for l in lines: print(cdataline(l))
# s = bitline(l)
# print(s)
# w_file('bdb', s)
# line = r_file('bdb')
# print(cdataline(line[0]))