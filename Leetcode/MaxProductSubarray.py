def maxProduct(self, nums):
#         maxx=nums[0]
#         for i in range(1,len(nums)):
#             nums[i]=max(nums[i], nums[i]*nums[i-1])
#             maxx=max(nums[i],maxx)
#         return maxx
# print(maxProduct(maxProduct,[-2,3,-4]))


    res=0
    cur_min=1
    cur_max=1
    for i in range(len(nums)):
        vals=(nums[i], nums[i]*cur_min , nums[i]*cur_max)
        cur_min=min(vals) 
        cur_max=max(vals)
        res=max(res, cur_max)
    return res
print(maxProduct(maxProduct,[-2,3,-4]))


def maxProduct(self, nums: list[int]):
    curMax, curMin = 1, 1
    res = nums[0]
    
    for n in nums:
        vals = (n, n * curMax, n * curMin)
        curMax, curMin = max(vals), min(vals)
        
        res = max(res, curMax)
        
    return res