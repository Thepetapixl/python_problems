# You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional)
# . For each house, find the store closest to it.
# Return an integer array result where result[i] should denote the location of the store closest to the i-th house.
# If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.
#
# Example 1:
#
# Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
# Output: [5, 11, 16]
# Explanation:
# The closest store to the house at location 5 is the store at the same location.
# The closest store to the house at location 10 is the store at the location 11.
# The closest store to the house at location 17 is the store at the location 16.
# Example 2:
#
# Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
# Output: [2, 3, 2]

def closest_store(houses, stores):
    temp = abs(houses[0] - stores[0])
    result = []
    closest = stores[0]
    for house in houses:
        for store in stores:
            if abs(house - store) < temp:
                temp = abs(house - store)
                closest = store
            if abs(house - store) == temp:
                closest = min(closest, store)
        result.append(closest)
        temp = max(max(houses, stores))
    print(result)


houses = [4, 8, 1, 1]
stores = [5, 3, 1, 2, 6]
closest_store(houses, stores)
