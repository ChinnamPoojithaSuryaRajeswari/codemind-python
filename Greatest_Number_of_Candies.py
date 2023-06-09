n=int(input())
li=list(map(int,input().split()))
k=int(input())
l=0
for i in li:
    if i>l:
        l=i
for i in li:
    if i+k>=l:
        print("True",end=" ")
    else:
        print("False",end=" ")