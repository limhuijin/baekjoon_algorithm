n = int(input())
stack, result, find = [], [], True
no = 1

for i in range(n):
    num = int(input())
    
    while no <= num:
        stack.append(no)
        result.append('+')
        no += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        find = False
        
if not find:
    print('NO')
else:
    for i in result:
        print(i)
        
        
# n = input
# stack = [], result = [], find = True
# no = 1

# for i in range(1, n)
#     num = input
#     while no <= num:
#         stack.append(no)
#         result.append('+')
#         no += 1
        
#     if stack[-1] == num:
#         stack.pop()
#         result.append('-')
#     else:
#         find = False
        
# if not find:
#     print('NO')
# else:
#     for i in result:
#         print(i)