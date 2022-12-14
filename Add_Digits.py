def adig(n):
    s=0
    while n:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
a=adig(n)
while a>9:
    a=adig(a)
else:
    print(a)
