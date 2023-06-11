n=int(input())
l=list(map(int,input().split()))
k=int(input())
p=[]
for i in range(n):
    if i+k<n:
        p.append(l[i])
        p.append(l[i+k])
print(*p)