# def twoSum(self, nums, target):
#     prevMap= {} #val: index
#     for i , a in enumerate(nums):
#         diff=target-a
#         if(diff in prevMap):
#             return [i, prevMap[diff]]
#         else:
#             prevMap[a]=i
# print(twoSum(twoSum,[3,2,4],6))


#another approach inspired by google interview video

def twoSum(self, nums, target):
    prevMap ={} #val:index
    for i , a in enumerate(nums):
        diff=target-a
        if (diff in nums[:i]):
            return [i, nums.index(target-a)]
        else:
            prevMap[diff]=i
    return []
print(twoSum(twoSum,[3,2,4],6))