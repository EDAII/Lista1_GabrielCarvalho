import sys
sys.path.append('./src')
import discipline_search as ds
import json


with open('data/d.json') as f:
  disciplines = json.load(f)

print("Insiria o código da disciplina: ")
code = int(input())

i = ds.binary_search(disciplines, code)
print(i['code'], '-', i['name'])

if(i['requirements']):
  print("Pré-Requisitos: ")
  for requirements in i['requirements']:
    requirement = requirements.split(',')
    for req in requirement:
      r = ds.binary_search(disciplines, int(req))
      print('\t', r['code'], '-', r['name'])

else:
  print("Matéria sem pré-requisitos")
