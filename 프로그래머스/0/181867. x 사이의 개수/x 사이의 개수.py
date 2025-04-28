def solution(myString):
    # answer = []
    result_split = myString.split("x")
    result = []
    for i in result_split:
        result.append(len(i))
        
    return result
        
        

    