#coding: utf-8

import binary_algs as bn
import creating_db_values as creator

def main():
    print('** Bem vindo ao bd-performance-test **')
    while True:
        op = input('1. Popular PostgreSQL\n'
              '2. Popular base de dados binária\n'
              '3. Executar querie em base binária...\n'
              '0. Sair...\n'
                   '# Digite uma opção: ')
        if op == 1: pass  # substituir pelo algoritmo correto
        elif op == 2: creator.create_db_values()
        elif op == 3: pass  # substituir pelo algoritmo correto
        elif op == 0: exit(0); break
        else: print('Opção inválida\n')

if __name__ == '__main__': main()