n=int(input())
lis=list(map(int,input().split()))
k=0
for i in lis:
    s=0
    for j in lis:
        if(i==j):
            s+=1
    if s==1:
        k=k+1
        print(i,end=" ")
if k==0:
    print("-1")