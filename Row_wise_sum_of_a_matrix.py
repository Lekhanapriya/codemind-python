r,c=map(int,input().split())
mat=[]
for i in range(r):
    b=list(map(int,input().split()))
    mat.append(b)
di=[]
for i in range(r):
    di.append(sum(mat[i]))
print(*di)