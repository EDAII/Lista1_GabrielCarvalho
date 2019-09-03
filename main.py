import os
import sys
import json
import numpy as np
import time
import matplotlib.pyplot as plt
from src import discipline_search as ds
from src import search

def main():
    os.system('cls||clear')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Métodos de Busca\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Selecione uma opção: ' + '\n')
    print('[1] - Buscar Matérias')
    print('[2] - Teste de Desempenho')
    print('[3] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    option = int(input('>>>'))

    while(option not in [1, 2, 3]):
        option = int(input("Insira uma opção válida: "))

    if(option == 1):
        discipline_menu()
    elif(option == 2):
        graph_menu()
    else:
        sys.exit()


def discipline_menu():

    os.system('cls||clear')

    with open('data/disciplines.json') as f:
        disciplines = json.load(f)

    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Métodos de Busca\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Selecione uma opção de busca: ' + '\n')
    print('[1] - Busca sequêncial')
    print('[2] - Busca binária')
    print('[3] - Busca interpolação')
    print('[4] - Buscar indexada')
    print('[5] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    option = int(input('>>>'))

    while(option not in [1, 2, 3, 4, 5]):
        option = int(input("Insira uma opção válida: "))

    if(option == 5):
        sys.exit()
    
    os.system('cls||clear')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print("Insiria o código da disciplina: ")
    code = int(input('>>>'))
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')

    if (option == 1):

        i = ds.linear_search(disciplines, code)
        if(i):
            print(i['code'], '-', i['name'])
            if(i['requirements']):
                print("Pré-Requisitos: ")
                for requirements in i['requirements']:
                    requirement = requirements.split(',')
                    for req in requirement:
                        r = ds.linear_search(disciplines, int(req))
                        if(r):
                            print('\t', r['code'], '-', r['name'])

            else:
                print("Matéria sem pré-requisitos\n")
        
        else:
            print("Matéria não encontrada\n")
        
        print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    

    elif (option == 2):

        i = ds.binary_search(disciplines, code)
        if(i):
            print(i['code'], '-', i['name'])
            if(i['requirements']):
                print("Pré-Requisitos: ")
                for requirements in i['requirements']:
                    requirement = requirements.split(',')
                    for req in requirement:
                        r = ds.binary_search(disciplines, int(req))
                        if(r):
                            print('\t', r['code'], '-', r['name'])

            else:
                print("Matéria sem pré-requisitos\n")
        
        else:
            print("Matéria não encontrada\n")
        
        print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')

    elif (option == 3):

        i = ds.interpolation_search(disciplines, code)
        if(i):
            print(i['code'], '-', i['name'])
            if(i['requirements']):
                print("Pré-Requisitos: ")
                for requirements in i['requirements']:
                    requirement = requirements.split(',')
                    for req in requirement:
                        r = ds.interpolation_search(disciplines, int(req))
                        if(r):
                            print('\t', r['code'], '-', r['name'])

            else:
                print("Matéria sem pré-requisitos\n")
        
        else:
            print("Matéria não encontrada\n")
        
        print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')

    elif (option == 4):

        a = ds.create_index(disciplines)
        i = ds.indexed_search(a, disciplines, code)

        if(i):
            print(i['code'], '-', i['name'])
            if(i['requirements']):
                print("Pré-Requisitos: ")
                for requirements in i['requirements']:
                    requirement = requirements.split(',')
                    for req in requirement:
                        r = ds.indexed_search(a, disciplines, int(req))
                        if(r):
                            print('\t', r['code'], '-', r['name'])
            else:
                print("Matéria sem pré-requisitos\n")
        else:
            print("Matéria não encontrada\n")
        
        print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
        
    else:
        sys.exit()
def print_search(i):
    if(i):
        print(i)
    else: 
        print('Não encontrado')

def graph_menu():

    os.system('cls||clear')

    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Métodos de Busca\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print("Teste de Desempenho\n")
    print("Escolha o tamanho do array: ")
    size = int(input('>>>'))
    array = list(np.arange(size))
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    print(array)
    print('')

    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    print('Insira o número do registro que deseja pesquisar: ')
    num = int(input('>>>'))
    print('\n', '\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')

    runtime = []
    searchs = ['Busca Linear', 'Busca Binária', 'Busca por Interpolação', 'Busca Indexada']

    start = time.time()
    i = search.linear_search(array, num)
    end = time.time()
    print_search(i)
    runtime.append(end - start)

    start = time.time()
    i = search.binary_search(array, num)
    end = time.time()
    print_search(i)
    runtime.append(end - start)
    
    
    start = time.time()
    i = search.interpolation_search(array, num)
    end = time.time()
    print_search(i)
    runtime.append(end - start)
    

    idx = search.create_index(array)
    start = time.time()
    i = search.indexed_search(idx, array, num)
    end = time.time()
    print_search(i)
    runtime.append(end - start)
    
    plt.figure(figsize=(15,5))
    plt.barh(searchs, runtime, color='red')
    plt.xlabel('Tempo de execução')
    plt.show()

if __name__ == '__main__':
    main()
