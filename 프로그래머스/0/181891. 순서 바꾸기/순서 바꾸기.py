def solution(num_list, n):
    first_ans = []
    sec_ans = []
    
    cnt = 0
    
    for i in range(len(num_list)):
        if cnt < n:
            cnt +=1
            first_ans.append(num_list[i])
        else:
            sec_ans.append(num_list[i])
    return sec_ans+first_ans