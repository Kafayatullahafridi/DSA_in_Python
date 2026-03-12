
##sorted array is must in binary search
##binary search time complexity is  O(logn)

def binarySearch(arr,i,j,x):
 while i<=j:
   mid = i+(j-1)//2
   if arr[mid]== x :
    return mid
   elif arr[mid] <x:   
   ## return binarySearch(arr, mid+1,j,x)
     i = mid+1
   else:
     ##return binarySearch(arr, mid-1,j,x)
     j=mid-1
 return -1




arr = [2,6,7,8,9,89,90]

x= 89
i=0
j=len(arr)-1



result = binarySearch(arr,i,j,x)

print('search is',result)