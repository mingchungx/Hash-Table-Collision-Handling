#Hash Table 1, size 100 (small), modulo hash function function, CHAINING
class SHashTable:
    def __init__(self):
        self.size = 100
        self.bucket = [[] for generation in range(self.size)]

    def hash_function(self,key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self.size

    def __setitem__(self,key,value): #Setting the item
        hash_code = self.hash_function(key)
        found = False
        for index,element in enumerate(self.bucket):
            if len(element) == 2 and element[0] == key: #Already exists
                self.bucket[hash_code][index] = (key,value) #Gets replaced
                break
        if not found:
            self.bucket[hash_code].append((key,value)) #If does not already exist, append it as a tuple at that array
    
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