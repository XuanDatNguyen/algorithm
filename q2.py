def solution(x, y):
    result = 0
    if x > y:
        return
    while(y > x):
        if(y % 2 != 0):
            y += 1
            result += 1
        y //= 2
        result += 1
        
    return result + x - y
 

 
print(solution(3, 5))