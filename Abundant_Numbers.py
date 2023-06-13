n=int(input())
k=n
s=0
for i in range(1,(n//2)+1):
    if n%i==0:
        s=s+i
if s>k:
    print("True")
else:
    print("False")