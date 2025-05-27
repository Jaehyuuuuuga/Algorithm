def solution(my_string, m, c):
    row = []
    result = ''
    
    for i in range(0, len(my_string), m):
        row.append(my_string[i:i+m])
    
    for r in row:
        result += r[c-1]
    
    return result