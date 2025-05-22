def solution(n_str):
    answer = []
    cnt = 0
    for i in list(n_str):
        if i != "0" and cnt == 0:
            answer.append(i)
            cnt +=1
        elif cnt == 1:
            answer.append(i)
    return ''.join(answer)
            
            
        
            
        
        