M=int(input())
set1=set(map(int,input().split()))
for i in range(int(input())):
    lst=input().split()
    num=list(map(int,input().split()))
    if lst[0]=="intersection_update":
        set1.intersection_update(num)
    elif lst[0]=="update":
        set1.update(num)
    elif lst[0]=="difference_update":
        set1.difference_update(num)
    else:
        set1.symmetric_difference_update(num)
print(sum(set1))
