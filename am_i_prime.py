import random as rd

primes = [2,   3,  5,  7, 11,\
          13, 17, 19, 23, 29,\
          31, 37, 41, 43, 47,\
          53, 59, 61, 67, 71,\
          73, 79, 83, 89, 97]

score = 0
round = 0
failures = list()

while True:
    num = rd.randint(1, 100)
    ans = input("{}. Is {} prime(y/n/q): ".format(round+1, num))
    if ans.lower() == "q":
        break
    elif ans.lower() == "y" and num in primes:
        score += 1
        print("Correct answer")
    elif ans.lower() == "n" and num not in primes:
        score += 1
        print("Correct answer")
    else:
        failures.append([round+1, num, num in primes, ans])
        print("Wrong/Invalid answer")
    round += 1

print("\n\n--TEST DONE--\n\n")
for i in failures: print("{}. {} is {}. but got {}".format(*i))
print("Accuracy: ", score/round*100, "%")