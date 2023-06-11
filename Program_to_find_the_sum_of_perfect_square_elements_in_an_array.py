def sqr(n):
    k=(n**0.5)
    if (int(k)*int(k)==n):
        return 1
    else:
        return 0
m=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if sqr(i):
        s=s+i
print(s)