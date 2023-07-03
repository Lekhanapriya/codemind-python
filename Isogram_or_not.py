def isogram(n):
    return len(n)==len(set(n.lower()))
n=input()
print(isogram(n))