

# Complete the solve function below.
def solve(s):
    s=s.split(' ')
    for i in range(len(s)):
        s[i]=s[i].capitalize()+" "
    return "".join(s)
  
s=input()
print(solve(s))

