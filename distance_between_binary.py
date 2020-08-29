# The distance between 2 binary strings is the sum of their lengths after removing the common prefix.
# For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.


def distance(str_a, str_b):
    max_length = len(max(str_a, str_b))
    new_a = ""
    new_b = ""
    i = 0
    for i in range(max_length):
        if str_a[i] == str_b[i]:
            i += 1
            continue
        else:
            break
    for j in range(i, max_length):
        new_a += str_a[j]
        new_b += str_b[j]
    print(len(new_a) + len(new_b))

str_a = "1011000"
str_b = "1011110"
distance(str_a, str_b)
