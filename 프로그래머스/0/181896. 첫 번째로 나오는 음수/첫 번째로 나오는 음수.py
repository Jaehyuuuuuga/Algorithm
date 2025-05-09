def solution(num_list):
    answer = 0
    
    for i in num_list:
        if int(i) < 0:
            return num_list.index(i)
            break
    
    return -1
