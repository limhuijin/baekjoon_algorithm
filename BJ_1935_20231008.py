n = int(input())
word = input()                
num_lst = [0]*n				 

for i in range(n):
    num_lst[i] = int(input())

stack = []                 

for i in word :					
    if 'A' <= i <= 'Z' :		
        stack.append(num_lst[ord(i)-ord('A')])
    else :						
        str2 = stack.pop()		
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])			

# (n), (후위 표기식), (피연산자의 값) 선언, 값 입력
# 답 제출용 스택 선언

# for i in word
#     word[i]의 값이 A ~ Z 사이라면
#         num_list[x](x = A = 0, B = 1...)의 값을 
#         답 제출용 스택에 추가
#     아니라면
#         답 제출용 스택의 인덱스 0, 1번 숫자를 뽑아옴
        
#         만약 i가 +라면
#             답 제출용 스택에 두 숫자의 합을 추가
#         만약 i가 -라면
#             답 제출용 스택에 두 숫자의 뺌을 추가
#         만약 i가 x라면
#             답 제출용 스택에 두 숫자의 곱을 추가
#         만약 i가 /라면
#             답 제출용 스택에 두 숫자의 나눔을 추가

# 스택을 출력한다.