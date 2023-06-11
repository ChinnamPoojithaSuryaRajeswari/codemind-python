n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    if i==0:
        print(i,end= " ")
        k=k+1
for i in range(n-k):
    print(1,end=" ")