def threeSum(self, nums):
    threesum=[]
    nums.sort()
    for i, a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        sum=0-nums[i]
        while l < r:
            if(nums[l]+nums[r]==sum):
                threesum.append([nums[i],nums[l],nums[r]])
                while(l<r and nums[l]==nums[l+1]): 
                    l+=1
                while(l<r and nums[r]==nums[r-1]): 
                    r-=1
                l+=1
                r-=1
            elif(nums[l]+nums[r] >sum):
                r-=1
            else:
                l+=1
    return threesum
print(threeSum(threeSum,[-1,0,-1,2,-1,4]))
