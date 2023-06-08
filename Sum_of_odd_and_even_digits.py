n=int(input())
li=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if(i%2==0):
        s+=li[i]
    else:
        k+=li[i]
if (abs(s-k)==0):
    print("YES")
else:
    print("NO")