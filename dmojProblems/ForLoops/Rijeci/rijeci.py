buttonPress = int(input())
countA = 0
countB = 0
a = 1
b = 0
if buttonPress >= 1 and buttonPress <= 45:
    for count in range(buttonPress):
        countA = b
        countB = b + a
        a = countA
        b = countB
        

print(countA, " ", countB)
        