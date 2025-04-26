def solution(rny_string):
    
    result = []
    a = list(rny_string)
    for i in range(len(a)):
        if a[i] == "m":
            result.append("rn")
        else:
            result.append(a[i])
        
    return "".join(result)
        
        
    
    
    
    
    
        # if i == 'm':
        #     # result.append("".join(dic['m']))
        # else:
        #     result.append(i)
        
