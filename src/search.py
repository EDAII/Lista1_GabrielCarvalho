# Busca sequêncial
def linear_search(array, num):
  for a in array:
    if(num == a): 
      return a
  
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
def indexed_search(array):
  pass

