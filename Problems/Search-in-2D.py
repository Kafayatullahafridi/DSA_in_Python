##function def
def searchSortedMatrix(matrix,target):
   m =len(matrix)

  
   if m == 0:
     return False
   ##num of columns
   n  = len(matrix[0])
   left ,right = 0 ,m*n-1
   while left <=right:
      mid = left+(right-left)//2
      mid_element = matrix[mid//n][mid%n]
      if target == mid_element:
          return True
      elif target<mid_element:
         right =mid-1
      else:
         left = mid+1
   return False

###
matrix  =[[1,3,5,6],[10,11,16,20],[23,30,34,60]]

target = 100
result = searchSortedMatrix(matrix,target)
print(result)