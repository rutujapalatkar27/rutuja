def threeSumClosest(self, nums, target):
        res=nums[0]+nums[1]+nums[len(nums)-1]
        nums.sort()
        for i, a in enumerate(nums):
            l,r= i+1, len(nums)-1
            while(l<r): 
                curr_sum=nums[i]+nums[l]+nums[r]
                if(curr_sum < target):
                        l+=1
                else:
                        r-=1
                if(abs(target-curr_sum)<abs(target-res)):
                        res=curr_sum  
        return res
print(threeSumClosest(threeSumClosest, [-1,2,1,-4], 1))
                