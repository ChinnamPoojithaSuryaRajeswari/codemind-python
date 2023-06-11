m=int(input())
li=list(map(int,input().split()))
l=list(map(int,input().split()))
j=0
for i in range(len(li)):
        print(li[i]+l[j],end=" ")
        j=j+1