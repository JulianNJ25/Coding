montlyMegabytes = int(input())
months = int(input())
peroMegabytes = 0
peroSpent = 0

if peroMegabytes >= 0 and peroMegabytes <= 10000 and montlyMegabytes >= 1 and montlyMegabytes <= 100 and months >= 1 and months <= 100:
    for month in range(months):
        peroSpent = int(input())
        peroMegabytes = montlyMegabytes - peroSpent + peroMegabytes

print(peroMegabytes + montlyMegabytes)