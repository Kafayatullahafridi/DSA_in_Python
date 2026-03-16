##Selection Sort implementation
def selectionSort(arr):
  n= len(arr)
  for i in range(n):
    min_idx= i
    for j in range(i+1,n):
      if arr[j]<arr[min_idx]:
        min_idx =j
      
    arr[i],arr[min_idx] = arr[min_idx],arr[i]

  return arr





arr = [ 50,18,34,45,23,78,98,23]
##function callig
result = selectionSort(arr)
print(result)

