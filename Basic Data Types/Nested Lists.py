if __name__ == '__main__':
    nlist=[]
    n=[]
    small=1000
    ssmall=1000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score<small:
            small,ssmall=score,small
        elif  score>small and score<ssmall:
            ssmall=score
        nlist.append([name,score])
    for i in range(len(nlist)):
        if nlist[i][1]==ssmall:
            n.append(nlist[i][0])
    n.sort()
    for i in n:
        print(i)
