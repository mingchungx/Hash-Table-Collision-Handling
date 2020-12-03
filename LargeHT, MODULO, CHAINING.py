#Hash Table 1, size 10000 (large), modulo hash function function, CHAINING
class LHashTable:
    def __init__(self):
        self.size = 10000
        self.bucket = [[] for generation in range(self.size)]
    
    def hash_function(self,key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self.size
    
    def __setitem__(self,key,value):
        hash_code = self.hash_function(key)
        found = False
        for index,element in enumerate(self.bucket[hash_code]):
            if len(element) == 2 and element[0] == key:
                self.bucket[hash_code][index] = (key,value)
                break
        if not found:
            self.bucket[hash_code].append((key,value))
    
    def __getitem__(self,key):
        hash_code = self.hash_function(key)
        for elements in self.bucket[hash_code]:
            if elements[0] == key:
                return elements[1]
        raise Exception("Key does not exist in Hash Table")

    def __delitem__(self,key):
        hash_code = self.hash_function(key)
        for index,element in enumerate(self.bucket[hash_code]):
            if element[0] == key:
                del self.bucket[hash_code][index]
        raise Exception("Key does not exist in Hash Table")