n = int(input())

for i in range(n):
    stk = []
    str = input()
    isV = True
    
    for j in str:
        if j == '(':
            stk.append(1)
        elif j == ')':
            if stk:
                stk.pop()
            elif not stk:
                isV = False
                break
    
    if not stk and isV:
        print('YES')
    else:
        print('NO')