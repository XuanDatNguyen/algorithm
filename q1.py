import random
def solution(param):
    global solved
    prev_solution = []
    opers = ['+', '-', '']
    expression = ('%s'.join(param) % (random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     )
             )
    if eval(expression) == 100:
        if expression not in prev_solution:
            solved += 1
            prev_solution.append(expression)
            print ("Solution:", expression, eval(expression))
    else:
        pass
    
solved = 0
while solved < 1000:
    solution('123456789')