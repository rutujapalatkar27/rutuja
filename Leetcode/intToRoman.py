def intToRoman(self, num):
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                (5, "V"), (4, "IV"), (1, "I")]
    roman_digits=[]
    for value, symbol in digits:
        if num==0:
            break
        if(value > num):
            continue
        else:
            count=num//value
            num=num-value*count
            roman_digits.append(symbol*count)
    return "".join(roman_digits)
print(intToRoman(intToRoman,100))