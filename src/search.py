# Busca sequêncial
def linear_search(array, num):
  for a in array:
    if(num == a): 
      return array.index(a)
  
  return False 

# Busca sequêncial com sentinela (Insere o registro no final)
def sentinel_search(array, num):
   i = 0
   while(array[i] != num):
      i+=1
      if(i > len(array)-1):
        array.append(num)
        print("O Registro foi inserido no final dos registros") 
        return i
   return False

# Busca binária
def binary_search(array, num):
  low = 0
  high = len(array) - 1
  while(high >= low):
    mid = int((high + low )/2)

    if(array[mid] > num):
      high -=1
    elif(array[mid]< num):
      low += 1
    else:
      return mid
  return False

# Busca por interpolação
def interpolation_search(array, num):
  low = 0
  high = len(array) - 1
  while low <= high and num >= array[low] and num <= array[high]:
    mid = low + int(
        ((float(high - low) / (array[high] - array[low])) * (num - array[low])))
    if (array[mid] == num):
        return mid
    if (array[mid] < num):
        low = mid + 1
    else:
        high = mid - 1
  return False

# Busca indexada
def indexed_search(idx, array, num):
  low = 0
  for i in range (0, len(idx)):
    if(num == idx[i][0]):
      return idx[i][1]
    elif(idx[i][0] > num):
      for x in range(low, idx[i][1]):
        if(num == array[x]):
          return x
    elif(num > idx[-1][0]):
      for x in range(idx[-1][1], len(array)):
        if(num == array[x]):
          return x
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
    j.append(array[i*gap])
    j.append(array.index(array[i*gap]))
    index.append(j)
    i+=1

  return index