# Criar tabela de index
def create_index(array, gap=None):
  
  if(not gap): 
    gap = int(len(array)/(len(array)/1000))

  index = []
  i = 0
  while (i*gap<len(array)-1):
    index.append(array[i*gap])
    i+=1

  return index