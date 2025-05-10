def solution(my_string, is_prefix):
    
    ans =  list(my_string)
    cnt = ""
    for i in ans:
        cnt += i
        if cnt == is_prefix:
            return 1
    return 0

    # return int(my_string.startswith(is_prefix))
        
    
    
    
    