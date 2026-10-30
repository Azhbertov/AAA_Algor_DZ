# https://contest.yandex.ru/contest/102171/run-report/169892803/
def hash_poly(s, m, p=31):
    h = 0
    power = 1
    for ch in s:
        h = (h + ord(ch) * power) % m
        power = (power * p) % m
    return h


class ChainedHashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _h(self, key):
        return hash_poly(key, self.capacity)

    def _rehash(self):
        old = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)

    def put(self, key, value):
        i = self._h(key)
        bucket = self.buckets[i]
        for j, (k, _) in enumerate(bucket):
            if k == key:
                bucket[j] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > 0.7:
            self._rehash()

    def get(self, key):
        i = self._h(key)
        for k, v in self.buckets[i]:
            if k == key:
                return v
        return None

    def remove(self, key):
        i = self._h(key)
        bucket = self.buckets[i]
        for j, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(j)
                self.size -= 1
                return v
        return None


Q = int(input())
hash_table = ChainedHashMap()
result = []

for _ in range(Q):
    command = input().split()
    if command[0] == "put":
        hash_table.put(command[1], int(command[2]))
    elif command[0] == "get":
        value = hash_table.get(command[1])
        if value is None:
            result.append("Error")
        else:
            result.append(str(value))
    elif command[0] == "del":
        value = hash_table.remove(command[1])
        if value is None:
            result.append("Error")
        else:
            result.append(str(value))
    elif command[0] == "size":
        result.append(str(hash_table.size))

for i in result:
    print(i)
