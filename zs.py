#!/usr/bin/python

for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print("%d == %d *%d"%(num,i,j))
            break
    else:
        print("%d是一个质数"%num)
a=5
if a==5:
    print("hello 5")