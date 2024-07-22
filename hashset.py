class HashSet:
    def __init__(self, initialCapacity=4, loadFactor=0.75):
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

    def add(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k in bucket:
            if k == key:
                return
        bucket.append(key)
        self.size += 1
        if self.size / self.capacity > self.loadFactor:
            self.resize()

    def has(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k in bucket:
            if k == key:
                return True
        return False

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i, k in enumerate(bucket):
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
        return [k for bucket in self.buckets for k in bucket]

    def resize(self):
        oldBuckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for i in range(self.capacity)]
        self.size = 0
        for bucket in oldBuckets:
            for k in bucket:
                self.add(k)


def testHashset():
    test = HashSet()

    test.add("apple")
    test.add("banana")
    test.add("carrot")
    test.add("dog")
    test.add("elephant")
    test.add("frog")
    test.add("grape")
    test.add("hat")
    test.add("ice cream")
    test.add("jacket")
    test.add("kite")
    test.add("lion")

    print("HashSet after initial insertions:")
    print("Keys:", test.keys())

    test.add("moon")

    print("\nHashSet after exceeding load factor:")
    print("Keys:", test.keys())

    test.add("apple")
    test.add("banana")

    print("\nHashSet after attempting to add duplicate keys:")
    print("Keys:", test.keys())

    print("\nTesting other methods:")
    print("has('apple'):", test.has("apple"))
    print("remove('carrot'):", test.remove("carrot"))
    print("length:", test.length())
    print("clear:")
    test.clear()
    print("length after clear:", test.length())


testHashset()
