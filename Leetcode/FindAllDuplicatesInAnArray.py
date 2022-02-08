def findDuplicates(self, nums):
    mylist=[]
    nums.sort()
    for i in range(len(nums)-1):
        if(nums[i]<nums[i+1]):
            continue
        else:
            mylist.append(nums[i])  
    return mylist
print(findDuplicates(findDuplicates,[1]))
