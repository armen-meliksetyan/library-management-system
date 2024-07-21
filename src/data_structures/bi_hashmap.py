from .hashmap import Hashmap

class BiHashmap:
    def __init__(self):
        self.keyToValueMap = Hashmap()
        self.valueToKeyMap = Hashmap()

    def set(self, key, value):
        if self.keyToValueMap.get(key):
            self.remove_by_key(key)
        if self.valueToKeyMap.get(value):
            self.remove_by_value(value)

        self.keyToValueMap.set(key, value)
        self.valueToKeyMap.set(value, key)

    def get_by_key(self, key):
        return self.keyToValueMap.get(key)

    def get_by_value(self, value):
        return self.valueToKeyMap.get(value)

    def remove_by_key(self, key):
        value = self.keyToValueMap.get(key)
        if value:
            self.keyToValueMap.remove(key)
            self.valueToKeyMap.remove(value)

    def remove_by_value(self, value):
        key = self.valueToKeyMap.get(value)
        if key:
            self.valueToKeyMap.remove(value)
            self.keyToValueMap.remove(key)