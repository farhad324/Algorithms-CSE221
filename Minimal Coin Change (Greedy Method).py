C=[1000, 500, 100, 50, 20, 10, 5, 2, 1]
remaining=93
count=0
coins=[]
for i in C:
    count = count + (remaining//i)
    coins+=[i]*(remaining//i)
    remaining = remaining - ((remaining//i)*i)
print('Minimal Number of Coins:',count)
print('Minimal Change',coins)

     