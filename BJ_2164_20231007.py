from collections import deque

n = int(input())

deque = deque([i for i in range(1, n+1)])

for i in range(n - 1):
    deque.popleft()
    num = deque.popleft()
    deque.append(num)
    
print(deque[0], sep='')

# 정수 n을 입력받는다
# 1부터 n까지의 값을 가지는 큐를 생성한다

# for 1부터 n-1까지
#     0번 인덱스를 pop한다
#     0번 인덱스의 값을 저장한 후 appennd 한다

# deque[0]을 출력한다
