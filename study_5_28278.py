import sys
from collections import deque
n = int(input())
queue = deque([])

for i in range(n):
    num = sys.stdin.readline().split()
    if num[0] == '1':
        queue.append(int(num[1]))
    elif num[0] == '2':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif num[0] == '3':
        print(len(queue))
    elif num[0] == '4':
        if queue:
            print(0)
        else:
            print(1)
    elif num[0] == '5':
        if queue:
            print(queue[-1])
        else:
            print(-1)