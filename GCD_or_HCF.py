
def lcm(a,b):
    t=2
    res=1
    while True:
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            res=res*t
        else:
            t+=1
        if a<t or b<t:
            break
    return res
a,b=map(int,input().split())
print(lcm(a,b))
