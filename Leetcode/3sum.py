def threeSum(self, nums):
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[j]+nums[k]+nums[i]==0 and i!=j and j!=k and k!=i):
                        triplet=[nums[i],nums[j],nums[k]]
                        triplet.sort()
                        if triplet not in res:
                            res.append(triplet)
        return res
print(threeSum(threeSum,[-3,-3,1,2,3,4]))