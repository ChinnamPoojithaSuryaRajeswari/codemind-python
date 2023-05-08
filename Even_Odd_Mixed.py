n=input()
c=0
co=0
for i in n:
    if int(i)%2==0:
        c+=1
    else:
        co+=1
if c>0 and co>0:
    print("Mixed")
elif c>0 and co==0:
    print("Even")
else:
    print("Odd")