n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
s1=[]
for i in a:
    if i not in b:
        s.append(i)
for j in b:
    if j not in a:
        s1.append(j)
s=s+s1
print(*s)

        
        