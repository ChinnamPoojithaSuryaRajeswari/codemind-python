c,d=map(int,input().split())
A1,A2,A3=map(int,input().split())
B1,B2,B3=map(int,input().split())
if A1+A2+A3>=150 and B1+B2+B3>=150:
    l=A1+A2+A3+B1+B2+B3+d
elif A1+A2+A3<150 and B1+B2+B3>=150:
    l=A1+A2+A3+B1+B2+B3+d+c
elif A1+A2+A3>=150 and B1+B2+B3<150:
    l=A1+A2+A3+B1+B2+B3+d+c
else:
    l=A1+A2+A3+B1+B2+B3+d+c+c
if l>=A1+A2+A3+B1+B2+B3+c+c:
    print("NO")
else:
    print("YES")