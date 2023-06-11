n=int(input())
li=list(map(int,input().split()))
for i in li:
    k=0
    for j in li:
        if i==j:
            k=k+1
    if k==2:
        print(i)
        break