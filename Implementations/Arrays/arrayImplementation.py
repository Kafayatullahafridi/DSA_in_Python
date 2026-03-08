
#make an array

arr = [ 1,4,5,2,7,3,88,22]
## random access
#print(arr[2])
## suppose we have to find specifc number in an array
x =88

##making a func to find an element index, we are doing linear search
def linearSearch(arr,x):
  
    for i in range(len(arr)):
        if arr[i] ==x:
            return i
    return -1

result  = linearSearch(arr,x)
print("ur number is ",result)

## we use one for loop which will traverse through whole array so time complexity is O(n), space comp is O(1)

## insertion in array , list .insert(index, element)
arr.insert(0,33)
##remove element by mention that
arr.remove(88)
##in both add and remove the time complexity will remain O(n)
##list.count , will count frequency of an element 
##remove by index list.pop(index)
arr.pop(0)
## sort an array  list.sort()
arr.sort()
## finding index of an element  arr.index(element)
print(arr.index(22))
##extending array 
arr.extend([4,2,4,2,4])
##to reverse
arr.reverse()
print(arr)