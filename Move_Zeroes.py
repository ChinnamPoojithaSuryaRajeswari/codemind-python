n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i!=0:
        print(i,end=" ")
        k=k+1
for j in range(len(l)-k):
    print(0,end=" ")