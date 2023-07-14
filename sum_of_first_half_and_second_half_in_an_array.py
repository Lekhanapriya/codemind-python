n=int(input())
a=list(map(int,input().split()))
k=len(a)
s=0
v=0
for i in range(k//2):
    s+=a[i]
for j in range(k//2,k):
    v+=a[j]
print(s)
print(v)