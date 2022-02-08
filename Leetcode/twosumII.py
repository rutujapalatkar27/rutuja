def twoSum(self, numbers, target):
    res=[]
    i=0
    j=len(numbers)-1
    while(i<len(numbers) and j>0):
        if(numbers[i]+numbers[j]==target):
            res.append(i+1)
            res.append(j+1)
            break
        elif(numbers[i]+numbers[j]<target):
            i+=1
        elif(numbers[i]+numbers[j]>target):
            j-=1
    return res
print(twoSum(twoSum,[2,3,4],6))

#in this problem the list is already sorted.