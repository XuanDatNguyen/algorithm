
def solution(param, i):
    operator = ['+', '-', '']
    if i >= len(param):
        return
    for op in operator:
        param = param[:i] + op + param[i:]
        if eval(param) == 100:
            yield param
        for j in range(i + 2, len(param)):
            for sol in solution(param, j):
                yield sol
        param = param[:i] + param[i+1:]
my_set = set()
param = "123456789"
for idx in range(len(param)):
    for sol in solution(param, idx + 1):
        my_set.add(sol)
    
for item in my_set:
    print(item)