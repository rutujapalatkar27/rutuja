def maxSubArray(self, nums):
#     for i in range(1, len(nums)):
#             if nums[i-1] > 0:
#                 nums[i] += nums[i-1]
#     return max(nums)
# print(maxSubArray(maxSubArray,[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#kadane's algorithm approach
    maxx=nums[0]
    for i in range(1,len(nums)):
        nums[i]=max(nums[i], nums[i]+nums[i-1])
        maxx=max(nums[i],maxx)
    return maxx
print(maxSubArray(maxSubArray,[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#brute force time complexity is O(n^3)
#     output=[]
#     for i in range(len(nums)):
#         for j in range(i,len(nums)):
#             Sum=0
#             for k in range(i, j+1):
#                 Sum=Sum+nums[k]
#             output.append(Sum)
#     return max(output)   
# print(maxSubArray(maxSubArray,[-2, 1, -3, 4, -1, 2, 1, -5, 4]))


    