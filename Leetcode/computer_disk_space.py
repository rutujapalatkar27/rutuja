def segment(x, space):
    res=[]
    for i in range(0, len(space)-x+1):
        temp=[]
        temp=space[i:i+x]
        res.append(min(temp))
    return max(res)
print(segment(2,[8,4,4,6]))
