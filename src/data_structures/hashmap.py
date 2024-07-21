class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashmap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        index = self._hash(key)
        head = self.buckets[index]
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        head = self.buckets[index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def remove(self, key):
        index = self._hash(key)
        head = self.buckets[index]
        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.buckets[index] = head.next
                self.size -= 1
                return True
            prev = head
            head = head.next
        return False