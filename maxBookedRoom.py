# Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms, where + suggests room is booked, - room is freed. You have to find which room is booked maximum number of times.
#
# You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms can be booked and only booked rooms can be freeed. All rooms are initially free. Note that this does not mean that all rooms have to be free at the end. In case, 2 rooms have been booked the same number of times, return the lexographically smaller room.
#
# You may assume:
#
# N (length of input) is an integer within the range [1, 600]
# each element of array A is a string consisting of three characters: "+" or "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
# the sequence is correct. That is every booked room was previously free and every freed room was previously booked.
# Example:
#
# Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
# Output: "1A"
# Explanation: 1A as it has been booked 2 times.

from collections import defaultdict
data = ["+1A", "+3E", "-3E", "+4F", "+3E", "-3E"]

tracker = defaultdict(int)
max_booked = data[0][1]

for el in data:
    key = el[1:]
    if el[0] == '+':
        tracker[key] += 1
    if tracker[key] > tracker[max_booked]:
        max_booked = key
    elif tracker[key] == tracker[max_booked]:
        max_booked = min(key, max_booked)

print(max_booked)
