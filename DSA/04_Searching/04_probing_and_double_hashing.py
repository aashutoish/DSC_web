# 4. Write a program to show linear, quadratic probing and double hashing in python. 
class Hashing:
    def __init__(self, size):
        self.size = size

    def linear_probing(self, keys):
        table = [None] * self.size
        for key in keys:
            index = key % self.size
            for i in range(self.size):
                probe_idx = (index + i) % self.size
                if table[probe_idx] is None:
                    table[probe_idx] = key
                    break
        return table

    def quadratic_probing(self, keys):
        table = [None] * self.size
        for key in keys:
            hash_val = key % self.size
            for i in range(self.size):
                idx = (hash_val + i * i) % self.size
                if table[idx] is None:
                    table[idx] = key
                    break
        return table

    def double_hashing(self, keys):
        table = [None] * self.size

        def hash2(key):
            return 7 - (key % 7)  # secondary hash

        for key in keys:
            h1 = key % self.size
            step = hash2(key)
            for i in range(self.size):
                idx = (h1 + i * step) % self.size
                if table[idx] is None:
                    table[idx] = key
                    break
        return table


# Example Usage
if __name__ == "__main__":
    demo = Hashing(10)
    keys_linear = [12, 22, 32]   # collisions at index 2
    keys_quadratic = [15, 25, 35] # collisions at index 5
    keys_double = [10, 20, 30]    # collisions at index 0

    print("Linear Probing Example:")
    print("Keys:", keys_linear)
    print("Table:", demo.linear_probing(keys_linear))

    print("\nQuadratic Probing Example:")
    print("Keys:", keys_quadratic)
    print("Table:", demo.quadratic_probing(keys_quadratic))

    print("\nDouble Hashing Example:")
    print("Keys:", keys_double)
    print("Table:", demo.double_hashing(keys_double))
