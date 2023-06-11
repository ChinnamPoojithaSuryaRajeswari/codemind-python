n=int(input())
for i in range(n):
    k=int(input())
    lis=list(map(int,input().split()))
    for i in range(1,k+1):
        if i not in lis:
            print(i)