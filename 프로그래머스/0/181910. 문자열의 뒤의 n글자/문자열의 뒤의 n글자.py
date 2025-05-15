def solution(my_string, n):
    list(my_string)
    answer = []
    for i in my_string[len(my_string) - n::]:
        answer.append(i)
    
    return "".join(answer)