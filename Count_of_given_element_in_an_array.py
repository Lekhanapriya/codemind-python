n=int(input())
a=list(map(int,input().split()))
c=0
m=int(input())
for i in a:
    if i==m:
        c+=1
print(c)
        