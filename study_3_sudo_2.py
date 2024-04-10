def solution(my_string):
    result = ""
    
    for i in my_string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    
    return result


'''
    result = list(null)
    
    for i to my_string
        if my_string[i] == isupper
            result += i.lower
        else
            result += i.upper

    return result

    파이썬의 경우 my_string.swapcase()
    대문자와 소문자를 서로 변경해주는 함수가 존재
'''