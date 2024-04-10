n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

result = []
num = 0

for i in range(n):
    num += k - 1
    if num >= len(arr):
        num = num % len(arr)
        
    result.append(str(arr.pop(num)))
    
print("<", ", ".join(result)[:],">", sep='')


# 정수 n과 k를 입력받는다
# 1부터 n+1까지의 배열을 만든다(arr)
# 빈 배열을 만든다(result)
# 정수형 변수를 0으로 선언, 초기화한다(num)

# for 0부터 n까지
#     num에 k-1을 더한다
#     만약 num이 arr의 길이보다 같거나 크다면
#         num은 arr 길이 - num
    
#     result에 arr의 num번째 수를 추가한다
#     arr의 num번째 수를 삭제한다.


# result를 출력한다