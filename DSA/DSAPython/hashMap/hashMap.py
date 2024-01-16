

class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):

        index = self._hash(key)

        bucket = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def print_map(self):
        print(self.hash_map)

    def get(self, key):

        index = self._hash(key)

        bucket = self.hash_map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v

        return None



hash_map = HashMap(size=10)
hash_map.insert("apple", 1)
hash_map.insert("banana", 2)
hash_map.insert("orange", 3)

hash_map.print_map()