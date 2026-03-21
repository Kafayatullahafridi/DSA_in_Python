from collections import Counter

 ##TC:O(n)
nums = [2,2,1,1,1,2,2]

def majorityElement(nums):
    counts = Counter(nums)
    print (counts)

    return max(counts.keys(),key = counts.get)


result = majorityElement(nums)
print(result)