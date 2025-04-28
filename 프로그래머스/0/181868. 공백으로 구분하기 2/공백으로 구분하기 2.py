def solution(my_string):

    result = my_string.split(" ")
    aa = []
    for i in result:
        if i not in "":
            aa.append(i)
        
    return aa