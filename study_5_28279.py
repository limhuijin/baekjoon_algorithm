import sys
from collections import deque
n = int(input())

de = deque()
for i in range(n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    count = len(de)

    if num[0] == 1:
        de.appendleft(num[1])
    elif num[0] == 2:
        de.append(num[1])
    elif num[0] == 3:
        if count > 0:
            print(de.popleft())
        else:
            print(-1)
    elif num[0] == 4:
        if count > 0:
            print(de.pop())
        else:
            print(-1)
    elif num[0] == 5:
        print(count)
    elif num[0] == 6:
        if count == 0:
            print(1)
        else:
            print(0)
    elif num[0] == 7:
        if count > 0:
            print(de[0])
        else:
            print(-1)
    elif num[0] == 8:
        if count > 0:
            print(de[-1])
        else:
            print(-1)