ballPosition = 1
ballSwap = input()
maxSwaps = 50

if len(ballSwap) <= maxSwaps:
    for swap in ballSwap:
        if swap == 'A' and ballPosition == 1:
            ballPosition = 2
        elif swap == 'A' and ballPosition == 2:
            ballPosition = 1
        elif swap == 'B' and ballPosition == 2:
            ballPosition = 3
        elif swap == 'B' and ballPosition == 3:
            ballPosition = 2
        elif swap == 'C' and ballPosition == 1:
            ballPosition = 3
        elif swap == 'C' and ballPosition == 3:
            ballPosition = 1
else:
    exit()
print(ballPosition)