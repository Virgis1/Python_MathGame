import random
import time

OPERATORS = ["+", "-", "*"]
MIN = 2
MAX = 12
TOTAL_TASKS = 10

def generate_task():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    operator = random.choice(OPERATORS)

    if operator == "-":
        if num2 > num1:
            task = str(num2) + " " + operator + " " + str(num1)
            answer = eval(task)
            return task, answer
        else:
            return None
    else:
        task = str(num1) + " " + operator + " " + str(num2)
        answer = eval(task)
        return task, answer

start_time = time.time()
print("You have to solve 10 tasks correctly and you will know the completion time")

for i in range(TOTAL_TASKS):
    task_info = generate_task()
    while task_info is None:
        task_info = generate_task()
    task, answer = task_info
    guess = input("Task #" + str(i+1) + ": " + task + " = ")
    while guess != str(answer):
        guess = input("Incorrect. Try again: ")

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("You finished in", total_time, "seconds!")