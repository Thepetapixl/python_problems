# stirng a and b contain many strings seperated by ,
# print no. of words in which frequency of smalled alphabet in string b is greater than
# string a
#
# Example:
# string a: abcd,aa,bd
# string b: aaa,aa
#
# output: [3,2]
# Explanation: all 3 words in string a have less frequency of their smallest alphabet than
# 1st word of string b so- [3]
# and 2 words have less frequency of their smallest alphabet than 2nd word of string b
# thus [3,2]

def solve():
    str_a = input("Enter string a: ").split(",")
    str_b = input("Enter string b: ").split(",")

    res_a = []
    answer = []
    count = 0

    for words in str_a:
        minfreq_a = words.count(min(words))
        res_a.append(minfreq_a)

    for words in str_b:
        minfreq_b = words.count(min(words))
        for small in res_a:
            if small < minfreq_b:
                count += 1
        answer.append(count)
        count = 0
    print(answer)


solve()
