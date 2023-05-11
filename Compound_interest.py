def c_i(p,r,t):
    a=p*(pow((1+(r/100)),t))
    c=a-p
    return a
p,r,t=map(int,input().split())
cp=c_i(p,r,t)
print("%.2f" %cp)