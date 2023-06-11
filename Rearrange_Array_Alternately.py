n=int(input())
for i in range(n):
    q=[]
    k=int(input())
    l=list(map(int,input().split()))
    if k%2==0:
        for i in range(k//2): 
            q.append(l[k-1-i])
            q.append(l[i])
        print(*q)
    else:
        for i in range(k//2): 
            q.append(l[k-1-i])
            q.append(l[i])
        q.append(l[(k//2)])
        print(*q)