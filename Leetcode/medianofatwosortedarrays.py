# def findMedianSortedArrays(self, nums1, nums2):
#     add=0
#     nums3=nums1+nums2
#     num3=sorted(nums3)
#     le=len(nums3)//2
#     if(le%2==0):
#         for i in range(le-1, le+1):
#             add=add+nums3[i]
#         mean=add/2
#     else:
#         mean=num3[le]
#     return mean

    
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    nums3 = nums1+nums2
    nums3.sort()
    m = len(nums1)
    n = len(nums2)
    if (m+n)%2 == 1:
        return nums3[(m+n)//2]
    else:
        return (nums3[(m+n)//2-1]+nums3[(m+n)//2])/2
print(findMedianSortedArrays(findMedianSortedArrays, [1,2],[3,4]))

