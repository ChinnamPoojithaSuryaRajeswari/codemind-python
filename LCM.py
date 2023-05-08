m,n=map(int,input().split())
for i in range(1,(n*m)+1):
    if i%m==0 and i%n==0:
        print(i)
        break
    