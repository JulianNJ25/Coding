psw = input()
length = len(psw)
lowerCase = 0
upperCase = 0
digit = 0

if length >= 8 and length <= 12:
    for char in psw:
        if char.islower():
            lowerCase += 1
        if char.isupper():
            upperCase += 1
        if char.isdigit():
            digit += 1
    
if lowerCase >= 3 and upperCase >= 2 and digit >= 1:
    print("Valid")
else:
    print("Invalid")