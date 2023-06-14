m=input().split()
m=set(m)
n=int(input())
j=[]
for i in range(n):
    a=input().split()
    j.append(set(a))
for i in range(0,n):
    if j[i].issubset(m):
        if i<n-1:
            continue
        elif i==n-1:
            print("True")
    else:
        print("Fa
