n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    o=list(map(int,input().split()))
    p=[]
    for i in l:
        if i not in p:
            p.append(i)
    for j in o:
        if j not in p:
            p.append(j)
    if(len(p)==k):
        print("YES")
    else:
        print("NO")