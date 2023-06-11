n=int(input())
l=list(map(int,input().split()))
p=0
for i in l:
    k=0
    for j in l:
        if i==j:
            k=k+1
    if k>p:
        p=k
        o=i
    elif k==p:
        p=k
        if o>i:
            o=i
print(o)