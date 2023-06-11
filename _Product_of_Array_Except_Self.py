n=int(input())
li=list(map(int,input().split()))
for i in range(0,n):
    s=1
    for j in range(len(li)):
        if i!=j:
            s=s*li[j]
    print(s,end=" ")