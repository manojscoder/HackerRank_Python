n=int(input())
for i in range(n):
    a=int(input())
    c=input().split()
    c=set(c)
    b=int(input())
    d=input().split()
    d=set(d)
    if c.issubset(d):
        print("True")
    else:
        print("False")
    
