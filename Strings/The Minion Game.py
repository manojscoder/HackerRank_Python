def minion_game(string):
    vowels=['A','E','I','O','U']
    Stuart_points=0
    Kevin_points=0
    s=len(string)
    for i in range(0,s):
        if string[i] in vowels:
            Kevin_points+=s-i
        else:
            Stuart_points+=s-i
    if Stuart_points>Kevin_points:
        print("Stuart %d"%(Stuart_points))
    elif Stuart_points==Kevin_points:
        print("Draw")
    else:
        print("Kevin %d"%(Kevin_points))
string=input()
minion_game(string)

