if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ma=-101
    ans=-101
    for i in arr:
        if ma<i:
            ma,ans=i,ma
        elif ma>i and i>ans:
            ans=i
    print(ans)
