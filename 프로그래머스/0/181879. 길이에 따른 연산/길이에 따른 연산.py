def solution(num_list):
    a_result = 0
    b_result = 1
    c_result = 0
    if len(num_list) >= 11:
        for i in num_list:
            a_result += int(i)
        c_result = a_result
    else:
        for i in num_list:
            b_result *= int(i)
        c_result = b_result
    return c_result
    
        