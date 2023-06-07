n=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in range(len(l)):
    if(i%2==0):
        s+=l[i]
    else:
        k+=l[i]
if((abs(s-k))%4==0):
    print("X")
else:
    print("Y")