n=input()
l=list(map(int,input().split()))
c=0
b=set(l)
for i in b:
    if i%2!=0:
        c+=1
print(c)