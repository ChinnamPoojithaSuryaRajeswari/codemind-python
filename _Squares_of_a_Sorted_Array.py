n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.append(i**2)
for j in sorted(k):
    print(j,end=" ")