t = int(input())
for tc in range(t):
    n = int(input())
 
    pascal = [[1]*i for i in range(1, n+1)]
    # print(pascal)
    for k in range(2, n):
        for g in range(1, k):
            pascal[k][g] = pascal[k-1][g-1]+pascal[k-1][g]
 
    # print(pascal)
    print(f'#{tc+1}')
    for j in pascal:
        print(*j)