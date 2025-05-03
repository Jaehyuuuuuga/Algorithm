def solution(num_list):
    
    add = 0
    multi = 1
    
    for i in num_list:
        add += i
        multi *= i
    
    return 1 if add**2 > multi else 0
    