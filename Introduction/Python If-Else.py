n = int(input().strip())
if n%2!=0 or (n%2==0 and (n>=6 and n<=20)):
    print("Weird")
else:
    print("Not Weird")
