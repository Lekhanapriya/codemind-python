n=int(input())
l=list(map(int,input().split()))
even=0
odd=0
for i in range(n):
    if i%2==0:
        even+=l[i]
    if i%2!=0:
        odd+=l[i]
p=even-odd
if p==0:
    print("YES")
else:
    print("NO")