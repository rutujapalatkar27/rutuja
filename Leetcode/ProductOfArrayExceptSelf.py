# import numpy
# def productExceptSelf(self, nums):
#     res=[]
#     for i in range(0, len(nums)):
#         res.append(numpy.prod(nums[:i]+nums[i+1:len(nums)]))
#     return res
# print(productExceptSelf(productExceptSelf,[1,2,3,4]))
            
        

# def productExceptSelf(self, nums):
#         p = 1
#         n = len(nums)
#         output = []
#         for i in range(0,n):
#             output.append(p)
#             p = p * nums[i]
#         p = 1
#         for i in range(n-1,-1,-1):
#             output[i] = output[i] * p
#             p = p * nums[i]
#         return output
# print(productExceptSelf(productExceptSelf,[1,2,3,4]))


def productExceptSelf(self, nums): #[1,2,3,4]
    res=[1]*(len(nums)) #res=[1,1,1,1,1]
    prefix=1
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i]
    postfix=1
    for i in range(len(nums)-1,-1,-1):
        res[i]*=postfix
        postfix*=nums[i]
    return res
print(productExceptSelf(productExceptSelf,[1,2,3,4]))

   
    




