# Busca sequêncial de matéria pelo código
def linear_search(disciplines, x):
  for discipline in disciplines:
    if(int(discipline["code"]) == x): 
      return discipline
  
  return False 

# Busca binária de matéria pelo código
def binary_search(array, num):
  low = 0
  high = len(array) - 1
  while(high >= low):
    mid = int((high + low )/2)

    if(int(array[mid]['code']) > num):
      high -=1
    elif(int(array[mid]['code'])< num):
      low += 1
    else:
      return array[mid]
  return False

# Busca binária de matéria pelo código e retorna o indice 
def binary_search_idx(array, num):
  low = 0
  high = len(array) - 1
  while(high >= low):
    mid = int((high + low )/2)

    if(int(array[mid]['code']) > num):
      high -=1
    elif(int(array[mid]['code'])< num):
      low += 1
    else:
      return mid
  return False

# Busca por interpolação
def interpolation_search(array, num):
  low = 0
  high = len(array) - 1
  while (low <= high and num >= int(array[low]['code']) and num <= int(array[high]['code'])):
    mid = low + int(((float(high - low) / (int(array[high]['code']) - int(array[low]['code']))) * (num - int(array[low]['code']))))
    if (int(array[mid]['code']) == num):
        return array[mid]
    if (int(array[mid]['code']) < num):
        low = mid + 1
    else:
        high = mid - 1
  return False

# Busca indexada
def indexed_search(idx, array, num):
  low = 0
  for i in range (0, len(idx)):
    if(num == idx[i][0]):
      return array[idx[i][1]]
    elif(idx[i][0] > num):
      for x in range(low, idx[i][1]):
        if(num == int(array[x]['code'])):
          return array[x]
    elif(num > idx[-1][0]):
      for x in range(idx[-1][1], len(array)):
        if(num == int(array[x]['code'])):
          return array[x]
    low = idx[i][1]

  return False

# Criar tabela de index
def create_index(array, gap=None):
  
  if(not gap): 
    gap = int(len(array)/(len(array)/1000))

  index = []
  i = 1
  while (i*gap<len(array)-1):
    j = []
    j.append(int(array[i*gap]['code']))
    j.append(binary_search_idx(array, int(array[i*gap]['code'])))
    index.append(j)
    i+=1

  return index