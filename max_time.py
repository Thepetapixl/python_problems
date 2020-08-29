# You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.
#
# Example 1:
#
# Input: "?4:5?"
# Output: "14:59"
# Example 2:
#
# Input: "23:5?"
# Output: "23:59"
# Example 3:
#
# Input: "2?:22"
# Output: "23:22"
# Example 4:
#
# Input: "0?:??"
# Output: "09:59"
# Example 5:
#
# Input: "??:??"
# Output: "23:59"

def settime():
    time = input("Enter time: ")
    new_time = ""
    if time[0] == '?':
        if time[1] == '?' or int(time[1]) < 4:
            new_time += '2'
        else:
            new_time += '1'
    else:
        new_time = time[0]

    if time[1] == '?':
        if time[0] == '?' or time[0] == '2':
            new_time += '3'
        else:
            new_time += '9'
    else:
        new_time += time[1]

    new_time += ':'

    if time[3] == '?':
        new_time += '5'
    else:
        new_time += time[3]

    if time[4] == '?':
        new_time += '9'
    else:
        new_time += time[4]
    print(new_time)


settime()
