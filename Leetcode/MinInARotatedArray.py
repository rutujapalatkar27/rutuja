def findMin(self, nums):
    if(len(nums)==0):
        return []
    elif(len(nums)==1):
        return nums[0]
    if(nums[len(nums)-1]>nums[0]):
        return nums[0]
    else:
        l,r=0, len(nums)-1
        while(l<r):
            mid=(r+l)//2
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            elif(nums[mid]<nums[mid-1]):
                return nums[mid]
            elif(nums[mid]>nums[l]):
                    l=mid+1
            elif(nums[mid]<nums[l]):
                    r=mid-1
    return nums[mid]    
print(findMin(findMin,[4,5,1,2,3]))