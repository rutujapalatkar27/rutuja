import math
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        tot = n1 + n2
        mid = (tot)//2
        while mid>=0:
            if (nums1[0] if n1 else math.inf) > (nums2[0] if n2 else math.inf):
                res.append(nums2[0])
                nums2.pop(0)
                n2-=1
            else:
                res.append(nums1[0])
                nums1.pop(0)
                n1-=1
            mid -=1
        if (tot)%2:
            return res[-1]
        else:
            return (res[-1] + res[-2])/2
print(findMedianSortedArrays(findMedianSortedArrays,[1,2],[3,4]))