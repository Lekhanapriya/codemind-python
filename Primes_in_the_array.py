def primes(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if primes(i):
        c+=1
print(c)