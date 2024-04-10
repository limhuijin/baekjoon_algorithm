from collections import deque
n = int(input())
q = deque(enumerate(map(int,input().split())))
arr=[]

while q:
    index, num = q.popleft()
    arr.append(index + 1)
    
    if num > 0:
        q.rotate(-(num-1))
    elif num < 0:
        q.rotate(-num)
        
print(' '.join(map(str,arr)))

# 정수 n을 입력받는다
# 정수 2개씩 짝지어서 n길이의 데큐를 만들다
# 정수 배열을 하나 만든다
#     index num에 q의 0번째 값과 인덱스를 넣는다
#     답에 인덱스를 추가한다
#     만약 num가 0보다 크다면
#         시계 반대방향(-1은 터지는 풍선 포함)
#     만약 num이 0보다 작다면
#         시계 방향
# 답을 출력