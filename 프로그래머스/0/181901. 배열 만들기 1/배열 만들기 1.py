def solution(n, k):
    
#     result = []
    
#     for i in range(1,n+1):
        
#         if i % k == 0:
#             result.append(i)
#     return result

    return [i for i in range(k,n+1,k)]
        
        