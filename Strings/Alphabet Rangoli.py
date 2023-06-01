def print_rangoli(n):
    temp_size=i=n
    flag1=flag2=0
    s=""
    while(i>0 and i<n+1):
        if(flag1==0):
            while(temp_size!=n+1):
                if(i==temp_size or flag2==1):
                    s=s+chr(temp_size+96)+'-'
                    temp_size+=1
                    flag2=1
                else:
                    s=s+chr(temp_size+96)+'-'
                    temp_size-=1
            i-=1
            temp_size=n
            flag2=0
            print(s[0:len(s)-1].center(n*4-3,'-'))
            s=""
        else:
            while(temp_size!=n+1):
                if(i==temp_size or flag2==1):
                    s=s+chr(temp_size+96)+'-'
                    temp_size+=1
                    flag2=1
                else:
                    s=s+chr(temp_size+96)+'-'
                    temp_size-=1
            i+=1
            temp_size=n
            flag2=0
            print(s[0:len(s)-1].center(n*4-3,'-'))
            s=""
        if(i==0):
            flag1=1
            i+=2
