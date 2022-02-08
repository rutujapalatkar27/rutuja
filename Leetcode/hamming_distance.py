#class Solutions(object):
def hammingDistance(x, y):
        dist=0
        x_=bin(x)
        y_=bin(y)
        if(len(x_)>len(y_)):
            y_=y_[2:].zfill(len(x_)-2)
            x_=x_[2:]
        else:
            x_=x_[2:].zfill(len(y_)-2)
            y_=y_[2:]
        for i, j in zip(list(x_),list(y_)):
            if(i==j):
                continue
            else:
                dist+=1
        return dist
print(hammingDistance(14,4))