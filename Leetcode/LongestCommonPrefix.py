def common_prefix(self, str1, str2):
    if(len(str2)<len(str1)): 
        common_prefix(common_prefix,str2,str1)
    size=len(str1)
    while(size>0):
        if(str1[0:size]==str2[0:size]):
            return str1[0:size]
        else:
            size-=1
    return []
def longestCommonPrefix(self, strs):
    strs.sort(key=len)
    temp_commom_prfix=strs[0]
    for i in range(1,len(strs)):
        str1=temp_commom_prfix
        str2=strs[i]
        size=len(temp_commom_prfix)
        while(size>0):
            if(str1[0:size]==str2[0:size]):
                temp_commom_prfix=str1[0:size]
                break
            else:
                size-=1
    return temp_commom_prfix

        #temp_commom_prfix=common_prefix(common_prefix, temp_commom_prfix, strs[i])
    #return temp_commom_prfix
print(longestCommonPrefix(longestCommonPrefix, ["reflower","flow","flight"]))
    

