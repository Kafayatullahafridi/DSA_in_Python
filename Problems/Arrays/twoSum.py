


"""
brute force approch 
TC: O(n^2)
target  = 10

arr = [4,2,5,2,4,6,3,2]
n = len(arr)
def twoSum(arr,target):
 
 for i in range(n):
   for j in range(i+1,n):
      if arr[i] + arr[j] == target:
           return [i, j]
 return [] 
   

result =  twoSum(arr,target)
print(result)  


"""  


##hash map approch
##TC:O(n)
target  = 10


arr = [4,2,5,2,4,6,3,2]
seen ={}
def twoSumOptimize(arr, target):
 for i , value in  enumerate(arr):
    number = target-value
    if number in seen:
        return [seen[number],i]
    seen[value] =i
 return []
