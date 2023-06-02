# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n=input().split()
arr=input().split()
A=set(input().split())
B=set(input().split())
Happiness=0
for i in arr:
    if i in A:
        Happiness+=1
    if i in B:
        Happiness-=1
print(Happiness)
