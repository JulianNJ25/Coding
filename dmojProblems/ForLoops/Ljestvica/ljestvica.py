input = input()
countADE = 0
countCFG = 0
inMeasure = False

if len(input) >= 2 and len(input) <= 100:
    for note in input:
        if inMeasure == False:
            if note == 'A' or note == 'D' or note == 'E':
                countADE += 1
            elif note == 'C' or note == 'F' or note == 'G':
                countCFG += 1
            inMeasure = True
        else:
            if note == '|':
                inMeasure = False

        
    if countADE > countCFG:
        print("A-mol")
    elif countCFG > countADE:
        print("C-dur")
    else:
        print("A-mol" if input[-1] == 'A' else "C-dur")

