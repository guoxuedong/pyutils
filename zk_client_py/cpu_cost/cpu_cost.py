import random

if __name__ == "__main__":
    sum = 1.0
    while True:
        sum += random.randint(0, 100)
        sum -= random.randint(0, 100)

    print sum
