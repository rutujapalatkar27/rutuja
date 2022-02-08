def search(self, nums, target):
    start=0
    if(len(nums)==0):
        return []
    elif(len(nums)==1):
        start=0
    if(nums[len(nums)-1]>nums[0]):
        start=0
    else:
        l,r=0, len(nums)-1
        while(l<r):
            mid=(r+l)//2
            if(nums[mid]>nums[mid+1]):
                start=mid+1
                break
            elif(nums[mid]<nums[mid-1]):
                start=mid
                break
            elif(nums[mid]>nums[l]):
                    l=mid+1
            elif(nums[mid]<nums[l]):
                    r=mid-1
    left=0
    right=len(nums)-1
#setting the boundaries for the left and right pointers according to the target 
#to ease out where exactly we have to move our search space
    if(target >= nums[start] and target <= nums[right]):
        left=start
    else:
        right=start 
    while(left<=right):
        mid=(right+left)//2
        if(target==nums[mid]):
            return mid    #from here we will get our answer
        elif(target<nums[mid]):
            right=mid-1
        else:
            left=mid+1
    return -1
print(search(search,[4,5,1,2,3],3))