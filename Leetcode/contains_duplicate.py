# def containsDuplicate(self, nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if(nums[j]==nums[i]):
#                 return True
#     return False
# print(containsDuplicate(containsDuplicate,[1,2,5,5]))


#hashmap
def containsDuplicate(self, nums):
    if len(nums)==len(set(nums)):
        return False
    else:
        return True
print(containsDuplicate(containsDuplicate,[1,2,3,6,5]))

#or
# def containsDuplicate(self, nums):
#     return len(nums)!=len(set(nums))

