from collections import deque

for i in range(int(input())):
    num = int(input())
    card = input().split()
    deq = deque()
    deq.append(card[0])
    start = card[0]
    
    for j in range(1, num):
        if start >= card[j]:
            deq.appendleft(card[j])
            start = card[j]
        else:
            deq.append(card[j])
    print(''.join(deq))