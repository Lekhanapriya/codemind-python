n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(len(l)):
    if(l[i]%2==0):
        e+=1
    if(l[i]%2!=0):
        o+=1
print(e,o,end="")