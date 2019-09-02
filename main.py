import os
import sys
import json
from src import discipline_search as ds


def main():
    os.system('cls||clear')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Estrutura de Dados 2 - Métodos de Busca\n')
    print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
    print('Selecione uma opção: ' + '\n')
    print('[1] - Buscar Matérias')
    print('[2] - Buscar em um Array')
    print('[3] - Sair')
    print('')
    print('\033[1m'+'==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
    option = int(input('>>>'))

    while(option not in [1, 2, 3]):
        option = int(input("Insira uma opção válida: "))

    if(option == 1):
        discipline_menu()
    elif(option == 2):
        pass
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


if __name__ == '__main__':
    main()
