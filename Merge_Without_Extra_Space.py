n=int(input())
for i in range(n):
    k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    p=list(map(int,input().split()))
    print(*(sorted(l+p)))