#python program to print prime numbers from 1 to 100
for i in range(1,101):
    f=0 
    for j in range (2,i):
        if i%j==0:
            f+=1
    if (i>1 and f ==0):
        print(i)
