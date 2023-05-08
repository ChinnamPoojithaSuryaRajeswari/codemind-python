n=int(input())
for i in range(n):
    k=int(input())
    s=1
    for j in range(1,k+1):
        s=s*j
    if (s==0):
        print("1")
    else:
        print(s)