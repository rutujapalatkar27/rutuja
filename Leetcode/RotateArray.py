def rotate(self, nums, k):
    res=[]
    i=k
    while(i>0):
        res.append(nums[-i])
        i-=1
    while(i<len(nums)-k):
        res.append(nums[i])
        i+=1
    return res
print(rotate(rotate,[-1,-100,3,99],2))