if __name__ == '__main__':
    N = int(input())
    i=0
    nlist=[]
    while(i<N):
        a=list(input().split())
        if a[0]=="insert":
            nlist.insert(int(a[1]),int(a[2]))
        elif a[0]=="print":
            print(nlist)
        elif a[0]=="remove":
            nlist.remove(int(a[1]))
        elif a[0]=="append":
            nlist.append(int(a[1]))
        elif a[0]=="sort":
            nlist.sort()
        elif a[0]=="pop":
            nlist.pop()
        else:
            nlist.reverse()
        i+=1
