import random
import time


def common_search(some_list, target):
    for i in range(len(some_list)):
        if some_list[i] == target:
            return i
    return -1


def binary_search(some_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(some_list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if some_list[midpoint] == target:
        return midpoint
    elif target < some_list[midpoint]:
        return binary_search(some_list, target, low, midpoint - 1)
    else:
        return binary_search(some_list, target, midpoint + 1, high)


if __name__ == '__main__':
    # l = [1, 3, 4, 5, 6, 7, 8]
    # target = 7
    # print(common_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        common_search(sorted_list, target)
    end = time.time()
    print("Common search time: ", (end - start) / length, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, " seconds")
