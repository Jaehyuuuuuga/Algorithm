def solution(myString):
    answer = ''
    myString_low = myString.lower()
    for i in myString_low:
        if i == 'a':
            answer += 'A'
        else:
            answer += i
    return answer