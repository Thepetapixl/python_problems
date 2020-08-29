# prints even numbers using
# lambda, filter and map functions


nums = input()

a = list(filter(lambda x: x % 2 == 0, map(int, nums.split(' '))))

print(a)
