n=int(input())
li=list(map(int,input().split()))
s=1
k=1
for i in li:
    c=0
    for j in range(1,i+1):
        if (i%j==0):
            c+=1
    if c==2:
        s*=i
    else:
        k*=i
print(abs(s-k))