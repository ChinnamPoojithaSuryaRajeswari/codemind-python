n=int(input())
arr=list(map(int,input().split()))
k,m=map(int,input().split())
l=[]
li=[]
for i in arr:
    if(i>=k and i<=m):
        l.append(i)
    else:
        li.append(i)
if len(li)==0:
    print("-1")
else:
    print(min(li))