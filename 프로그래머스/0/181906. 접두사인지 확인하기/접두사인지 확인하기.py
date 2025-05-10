def solution(my_string, is_prefix):
    
    ans =  list(my_string)
    cnt = ""
    for i in ans:
        cnt += i
        if cnt == is_prefix:
            return 1
    return 0
        
    
    
    
    