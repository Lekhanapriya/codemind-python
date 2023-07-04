n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=0
for i in l:
    if i<a or i>b:
       l1+=i
print(l1)