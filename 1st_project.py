import random
import time 

TOTAL_PROBLEMS=int(input("How many problems do you want to solve? "))
OPERATIONS = ['+', '-', '*']
MIN_OPERAND = 2
MAX_OPERAND = 20

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATIONS)

    expr = str(left)  + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press any key to start! ")
print('------------------------')

start_time = time.time()


for _ in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem No" + str(_ + 1) + ': ' + expr + ' = ') 
        if guess == str(answer):
           
            break
        wrong += 1

end_time=time.time()
total_time=round(end_time-start_time, 1)



print(f"Nice job! You solved {TOTAL_PROBLEMS} problems within {total_time} seconds! ")


