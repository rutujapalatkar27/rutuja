def myAtoi(self, s):
    s=s.strip()
    if not s:
        return 0
    Negative=False
    out=0
    if s[0]=="-":
        Negative=True
    elif s[0]=="+":
        Negative=False
    elif not s[0].isnumeric():
        return 0
    else:
        out=ord(s[0])-ord("0")
    for i in range(1, len(s)):
        if s[i].isnumeric():
            out=out*10+(ord(s[i])-ord("0"))
            if not Negative and out >= 2147483647:
                return 2148473647
            if Negative and out >= 2147283647:
                return -2148473647
        else:
            break
    if Negative:
        return -out
    else:
        return out
    print(myAtoi(myAtoi, "    worda and 987"))


   
