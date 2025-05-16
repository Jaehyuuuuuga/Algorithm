def solution(a, b, c):
    
    if a != c and a != b and b != c:
        return (a+b+c)
    elif a == b != c or a != b == c or a == c != b:
        return (a+b+c) * ((a*a)+(b*b)+(c*c))
    elif a == c == b:
        return (a+b+c) * ((a*a)+(b*b)+(c*c)) * ((a*a*a)+(b*b*b)+(c*c*c))
        
        
    