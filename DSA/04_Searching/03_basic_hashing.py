# 3. Show the basic implementation of Hashing in python. 
def hash(data):
    counter = 1
    sum = 0
    for d in data:
        sum += counter * ord(d)
    return sum % 256

if __name__ == "__main__":
    items = ['foo', 'bar', 'bim', 'baz', 'quux', 'duux', 'gnn']
    for item in items:
        print("{}: {}".format(item, hash(item)))
