# 1. Write a program to show the implementation of sequential Search.

def find_first(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def find_last(data, target):
    for index in range(len(data) - 1, -1, -1):
        if data[index] == target:
            return index
    return -1


def find_all(data, target):
    return [i for i, value in enumerate(data) if value == target]


if __name__ == "__main__":
    elements = [10, 23, 70, 45, 70, 11, 70, 15]

    print("Data:", elements)
    print("First 70 index:", find_first(elements, 70))
    print("Last 70 index:", find_last(elements, 70))
    print("All 70 indices:", find_all(elements, 70))
