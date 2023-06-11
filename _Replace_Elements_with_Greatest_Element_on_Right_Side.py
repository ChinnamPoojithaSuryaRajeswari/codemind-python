n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    o=0
    for j in range(i+1,len(l)):
        if l[j]>o:
            o=l[j]
    if(o==0):
        print(-1,end=" ")
    else:
        print(o,end=" ")