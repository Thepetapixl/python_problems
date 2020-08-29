lower_prime = []
upper_prime = []

def solve(arr):
    for num in arr:
        if prime(num):
            continue
        else:
            for i in range(num, i):
                pass

def prime(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

def lowerprime(n):
    new_prime = 0
    count = 0
    while new_prime <= n:
        for i in range(1, n):
            for j in range(1, i):
                if i % j == 0:
                    count += 1
            if count == 2:
                new_prime = j
            count = 0
    return new_prime


# test_cases = 4
arr = [8, 6, 9, 2, 5]
solve(arr)
