n=int(input())
l=list(map(int,input().split()))
p=int(input())
li=list(map(int,input().split()))
k=0
for i in l:
    if i in li:
        k=k+1
if k==p:
    print(True)
else:
    print(False)