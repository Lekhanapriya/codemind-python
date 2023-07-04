s=input()
a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtstuvwxyz1234567 '
c=0
for i in s:
    if i not in a:
        c+=1
print(c)
        