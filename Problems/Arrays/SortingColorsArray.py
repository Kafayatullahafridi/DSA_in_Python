
##TC: O(n)
nums = [ 2,0,2,1,1,0]
def sortColors(nums):

  p0 = current = 0
  p2 = len(nums)-1

  while current <=p2:
    if nums[current]==0:
      nums[p0], nums[current] = nums[current],nums[0]
      p0 +=1
      current+=1
    elif nums[current]==2:
      nums[p2],nums[current]= nums[current],nums[p2]
      p2-=1
    else:  
     current+=1
  return nums









result = sortColors(nums)
print(result)