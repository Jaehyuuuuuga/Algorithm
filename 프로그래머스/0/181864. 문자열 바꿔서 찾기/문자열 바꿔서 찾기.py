def solution(myString, pat):
    
    
    reverse = ''
    for i in myString:
        if i == 'A':
            reverse += 'B'
        elif i == 'B':
            reverse += 'A'
    
    if pat in reverse:
        return 1
    else:
        return 0
    
    
        
