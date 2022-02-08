def strStr(self, haystack, needle):
    if(len(haystack) or len(needle))==0:
        return 0
    res=[]
    for i in range(0, len(haystack)-len(needle)+1):
        if(haystack[i:i+len(needle)]==needle):
            return i
    return -1
print(strStr(strStr,"hello","le"))
