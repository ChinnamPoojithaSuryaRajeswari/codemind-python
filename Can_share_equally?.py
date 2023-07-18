m,p=map(int,input().split())
if ((m+(2*p))%2==0):
    if(m==0 and p%2!=0):
        print("NO")
    else:
        print("YES")
else:
    print("NO")