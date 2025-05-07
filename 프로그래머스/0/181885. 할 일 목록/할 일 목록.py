def solution(todo_list,finished):
    
    result = []
    cnt = 0
    
    for i in todo_list:
        if finished[cnt]:
            cnt+=1
        else:
            cnt+=1
            result.append(i)
    
    return result
            