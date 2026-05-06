# 2. Write the implementation of Binary Search in Python.  
class BinarySearch:

    @staticmethod
    def find_first(sorted_data, target):
        low, high = 0, len(sorted_data) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if sorted_data[mid] == target:
                result = mid
                high = mid - 1      # continue searching left
            elif sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    @staticmethod
    def find_last(sorted_data, target):
        low, high = 0, len(sorted_data) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if sorted_data[mid] == target:
                result = mid
                low = mid + 1       # continue searching right
            elif sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    @classmethod
    def find_all(cls, sorted_data, target):
        first = cls.find_first(sorted_data, target)
        if first == -1:
            return []

        last = cls.find_last(sorted_data, target)
        return list(range(first, last + 1))


# Example Usage
if __name__ == "__main__":
    sorted_elements = [10, 11, 15, 23, 23, 23, 45, 70]

    print(f"Sorted Data: {sorted_elements}")
    print(f"First 23: Index {BinarySearch.find_first(sorted_elements, 23)}")
    print(f"Last 23:  Index {BinarySearch.find_last(sorted_elements, 23)}")
    print(f"All 23s:  Indices {BinarySearch.find_all(sorted_elements, 23)}")
