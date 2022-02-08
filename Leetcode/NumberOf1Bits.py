def hammingWeight(self, n):
    count=0
    nums=list(str(n))
    for i in range(len(nums)):
        if(nums[i]=='1'):
            count+=1
    return count
print(hammingWeight(hammingWeight, "00000000000000000000000000001011"))