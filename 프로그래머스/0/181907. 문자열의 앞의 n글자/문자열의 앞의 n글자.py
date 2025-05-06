def solution(my_string, n):
    answer = ''
    cnt = 0
    for i in my_string:
        if cnt < n:
            answer +=i
            cnt +=1
        else:
            return answer
    return answer