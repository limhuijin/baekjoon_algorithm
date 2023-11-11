from collections import deque

t = int(input().strip()) 
for i in range(t):
    n, m = map(int, input().strip())
    arr = deque(map(int,input().strip().split())) 
    count = 0
    while arr:
        if arr[0] == max(arr):
            count += 1
            if m == 0:
                print(count)
                break
            else:
                arr.popleft()
                m -= 1
        else:
            arr.rotate(-1) # 맨뒤로가
            m = (m - 1) % len(arr) 
   
            
# t 입력

# for i in length(t)
#     int n, m 입력
#     int deque arr 입력
#     count = 0
#     while arr
#         if arr[0] == max(arr)
#             count++
#             if m == 0
#                 print(count)
#                 break
#             else
#                 arr.pop(0)
#                 m--
#         else
#             arr.append(arr[0])
#             arr.pop(0)   
#             m = (m - 1) % len(arr)
                