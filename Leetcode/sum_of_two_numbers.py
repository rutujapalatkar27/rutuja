def getSum(self, a, b):
    a_=bin(a)
    b_=bin(b)
    if(len(a_)>len(b_)):
        a_=a_[2:]
        b_=b_[2:].zfill(len(a_)-2)
    else:
        a_=a_[2:].zfill(len(b_)-2)
        b_=b_[2:]
    a_=list(a_)
    b_=list(b_)
    carry=0
    sum=0
    for i, j  in zip(a_, b_):
        if i==j==0:
            sum=sum+carry
            carry=0
        elif i==j==1:
            sum=sum+carry
            carry=1
        elif 
    print(a_)
    print(b_)
    
print(getSum(getSum,3,8))


        

        