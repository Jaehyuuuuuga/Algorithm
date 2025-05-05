def solution(numbers,n):
    add = 0
    
    for i in numbers:
        if add <= n:
            add += int(i)
        else:
            return add
    return add