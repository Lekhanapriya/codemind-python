n=int(input())
a=list(map(int,input().split()))
c=0
s=sum(a)//n
for i in a:
    if i<=s:
        c=c+1
print(c)
