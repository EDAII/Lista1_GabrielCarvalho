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

# Busca por interpolação
def interpolation_search(array, num):
  low = 0
  high = len(array) - 1
  while (low <= high and num >= int(array[low]['code']) and num <= int(array[high]['code'])):
    mid = low + int(
        ((float(high - low) / (int(array[high]['code']) - int(array[low]['code']))) * (num - int(array[low]['code']))))
    if (int(array[mid]['code']) == num):
        return array[mid]
    if (int(array[mid]['code']) < num):
        low = mid + 1
    else:
        high = mid - 1
  return False