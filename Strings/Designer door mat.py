size=list(map(int,input().split()))
for i in range(1,size[0],2):
    print('-'*((size[1]-i*3)//2)+(".|."*i)+'-'*((size[1]-i*3)//2))
print('-'*((size[1]-7)//2)+"WELCOME"+'-'*((size[1]-7)//2))
for i in range(size[0]-2,0,-2):
    print('-'*((size[1]-i*3)//2)+(".|."*i)+'-'*((size[1]-i*3)//2))
