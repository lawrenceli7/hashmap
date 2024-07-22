class HashMap:
    def __init__(self, initialCapacity=4, loadFactor=0.74):
        self.capacity = initialCapacity
        self.loadFactor = loadFactor
        self.size = 0
        self.buckets = [[] for i in range(initialCapacity)]

    def hash(self, key):
        hashCode = 0
        primeNumber = 31
        for char in key:
            hashCode = (primeNumber * hashCode + ord(char)) % self.capacity
        return hashCode

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.loadFactor:
            self.resize()

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def has(self, key):
        return self.get(key) is not None

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def length(self):
        return self.size

    def clear(self):
        self.buckets = [[] for i in range(self.capacity)]
        self.size = 0

    def keys(self):
        return [k for bucket in self.buckets for k, v in bucket]

    def values(self):
        return [v for bucket in self.buckets for k, v in bucket]

    def entries(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def resize(self):
        oldBuckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for i in range(self.capacity)]
        self.size = 0
        for bucket in oldBuckets:
            for k, v in bucket:
                self.set(k, v)


def testHashmap():
    test = HashMap()

    test.set("apple", "red")
    test.set("banana", "yellow")
    test.set("carrot", "orange")
    test.set("dog", "brown")
    test.set("elephant", "gray")
    test.set("frog", "green")
    test.set("grape", "purple")
    test.set("hat", "black")
    test.set("ice cream", "white")
    test.set("jacket", "blue")
    test.set("kite", "pink")
    test.set("lion", "golden")

    print("HashMap after initial insertions:")
    print("Entries:", test.entries())

    test.set("moon", "silver")

    print("\nHashMap after exceeding load factor:")
    print("Entries:", test.entries())

    test.set("apple", "green")
    test.set("banana", "blue")

    print("\nHashMap after overwriting values:")
    print("Entries:", test.entries())

    print("\nTesting other methods:")
    print("get('apple'):", test.get("apple"))
    print("has('banana'):", test.has("banana"))
    print("remove('carrot'):", test.remove("carrot"))
    print("length:", test.length())
    print("keys:", test.keys())
    print("values:", test.values())
    print("clear:")
    test.clear()
    print("length after clear:", test.length())


testHashmap()
