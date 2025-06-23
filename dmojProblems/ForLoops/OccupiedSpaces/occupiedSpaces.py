parkingSpaces = int(input())
firstDay = input()
secondDay = input()

occupied = 0

for i in range(len(secondDay)):
    if secondDay[i] == 'C' and firstDay[i] == 'C':
        occupied = occupied + 1

print(occupied)


