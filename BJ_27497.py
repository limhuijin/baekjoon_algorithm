from collections import deque
import sys

deq = deque()
stack = []

for _ in range(int(input())):
    arr = sys.stdin.readline()
    
    if arr[0] == '1':
        deq.append(arr[2])
        stack.append(1)
    elif arr[0] == '2':
        deq.appendleft(arr[2])
        stack.append(2)
    elif arr[0] == '3':
        if not deq:
            continue
        elif stack[-1] == 1:
            deq.pop()
            stack.pop()
        elif stack[-1] == 2:
            deq.popleft()
            stack.pop()

if not deq:
    print('0')
else:
    print(''.join(deq))