n=int(input())
a=0
b=1
l=[]
for i in range(n*n):
    c=a+b
    l.append(a)
    a=b
    b=c
if(n in l):
    print(True)
else:
    print(False)