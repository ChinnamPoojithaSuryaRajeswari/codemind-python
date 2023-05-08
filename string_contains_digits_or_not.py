n=int(input())
for j in range(n):
    k=input()
    c=0
    for i in k:
        if i.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")