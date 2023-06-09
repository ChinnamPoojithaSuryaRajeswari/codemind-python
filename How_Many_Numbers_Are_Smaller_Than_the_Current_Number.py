n=int(input())
li=list(map(int,input().split()))
for i in li:
    l=0
    for j in li:
        if i>j:
            l=l+1
    print(l,end=" ")