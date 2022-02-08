def adder(numX, numY):
    start=1
    count=0
    while(start<numX):
        if sum([int(i) for i in list(str(start))]) == numY:
            count+=1
        start+=1
    return count
print(adder(20, 5))

#mod approach


        