import random as rd
import time

numbers = [1,2,3,4,5,6,7]
time.time()

timers = list()
corr = 0
fail = 0

failures = list()

while True:
    num1 = rd.randint(1, 100)
    num2 = rd.randint(1, 100)
    t1   = time.time()
    inp  = input("{}. {} + {} = ".format(corr+fail+1, num1, num2))
    t2   = time.time()
    if inp.isalpha():
        break
    else:
        ans = int(inp)
    timers.append(t2 - t1)
    if ans == num1 + num2:
        corr += 1
        print("Correct answer in: ", timers[-1])
    else:
        fail += 1
        failures.append([corr+fail+1, num1, num2, num1+num2, ans])
        print("Wrong answer! Correct ans is: ", num1+num2)

print("\n\n--TEST DONE--\n\n")

for i in failures: print("{}. {} + {} = {}. but got {}".format(*i))
print("Accuracy: ", corr/(corr+fail)*100, "%")
print("Avg time: ", sum(timers)/len(timers), "s")

