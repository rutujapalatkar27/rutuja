def maxArea(self, height):
        i=0 
        j=len(height)-1
        maxarea=[]
        while(i<j):
            maxarea.append((j-i)*min(height[i],height[j]))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return max(maxarea)
print(maxArea(maxArea,[1,8,6,2,5,4,8,3,7]))