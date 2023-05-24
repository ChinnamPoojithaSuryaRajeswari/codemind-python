n=input()
s=0
for i in n:
    if(n.count(i)==1):
        s=s+1
if(s==len(n)):
    print("True")
else:
    print("False")