##ternery search implelmentation 
##time complexity is O(log₃ n)



##function defination

def ternarySearch(left,right, target ,arr):
     
   while left<=right:
      mid1= left+(right -left)//3
      mid2 = right- (right-left)//3

      if  arr[mid1] == target:
         return mid1
      elif arr[mid2] ==  target:
         return mid2
      elif target <arr[mid1]:
          return ternarySearch(left,mid1-1,target,arr)
      elif target >arr[mid2]:
         return  ternarySearch(mid2+1,right,target,arr)
      else:
         return  ternarySearch(mid1+1 , mid2-1,target,arr)
   return -1
















arr = [1,2,3,4,5,6,7,8,9,10]
left =0
right =  len(arr)-1
target = 1000
##function calling
result =ternarySearch(left, right ,target, arr)
print ('Searching element is present at index', result)