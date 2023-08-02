n=int(input())
arr=list(map(int,input().split()))
k,m=map(int,input().split())
l=[]
for i in arr:
    if(i>=k and i<=m):
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l)