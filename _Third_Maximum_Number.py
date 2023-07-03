n=int(input())
l=list(map(int,input().split()))
a=set(l)
a=sorted(a)
if(len(a)>=3):
    print(a[-3])
else:
    print(max(a))