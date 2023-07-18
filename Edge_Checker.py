m,n=map(int,input().split())
if m==n-1:
    print("Yes")
elif m==n+1:
    print("Yes")
elif m-1==n%10:
    print("Yes")
elif m%10==n-1:
    print("Yes")
else:
    print("No")