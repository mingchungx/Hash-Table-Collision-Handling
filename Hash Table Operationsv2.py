#IB Extended Essay - Linear Probing vs Chaining Collision Handling Python 3.8.3 64-Bit
------------------------------------------------------------

Prerequisites

import time #Measures execution time in seconds
from sys import getsizeof #Measures memory usage in bytes
from math import floor, modf #For multiplicative Hashing only
import random #For randomization of strings
import string #For random strings

class HashTableXXXX: #Hash Table Specification
    def __init__(self):
        self.size = XXXX #Load Factor; s = 997, h = 199, l = 109
        self.bucket = [XXXX for generation in range(self.size)] #[] for chaining, None for linear probing

    def print_bucket(self):
        print(self.bucket)

    def memory_usage(self):
        return getsizeof(self.bucket) 

------------------------------------------------------------
Modular Hash and Chaining

    def modular_hash(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self.size

    def __setitem__(self, key, value):
        hash_code = self.modular_hash(key)
        found = False
        for index, element in enumerate(self.bucket):
            if len(element) == 2 and element[0] == key:
                self.bucket[hash_code][index] = (key, value)
                break
        if not found:
            self.bucket[hash_code].append((key, value))
    
    def __getitem__(self, key):
        hash_code = self.modular_hash(key)
        for elements in self.bucket[hash_code]:
            if elements[0] == key:
                return elements[1]
        raise Exception("Key does not exist in Hash Table")

    def __delitem__(self, key):
        hash_code = self.modular_hash(key)
        for index, element in enumerate(self.bucket[hash_code]):
            if element[0] == key:
                del self.bucket[hash_code][index]
                return
        raise Exception("Key does not exist in Hash Table")

------------------------------------------------------------
Multiplicative Hash and Chaining

    def multiplicative_hash(self, key):
        constant = (3^40)/(2^64) #Random real number fitting c = s/2^64, 0 < s < 2^w
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return floor(self.size * (modf(hash_code * constant)[0]))

    def __setitem__(self, key, value):
        hash_code = self.multiplicative_hash(key)
        found = False
        for index, element in enumerate(self.bucket):
            if len(element) == 2 and element[0] == key:
                self.bucket[hash_code][index] = (key, value)
                break
        if not found:
            self.bucket[hash_code].append((key, value))
    
    def __getitem__(self, key):
        hash_code = self.multiplicative_hash(key)
        for elements in self.bucket[hash_code]:
            if elements[0] == key:
                return elements[1]
        raise Exception("Key does not exist in Hash Table")

    def __delitem__(self, key):
        hash_code = self.multiplicative_hash(key)
        for index, element in enumerate(self.bucket[hash_code]):
            if element[0] == key:
                del self.bucket[hash_code][index]
                return
        raise Exception("Key does not exist in Hash Table")

------------------------------------------------------------
Modular Hash and Linear Probing

    def probe_range(self, index):
        return [*range(index, len(self.bucket))] + [*range(0, index)]

    def linear_probe(self, key, index):
        for index in self.probe_range(index):
            if self.bucket[index] is None:
                return index
            if type(self.bucket[index]) != bool: #This needs to be checked in case of collision simulation of False filled self.bucket
                if self.bucket[index][0] == key:
                    return index
        raise Exception("Hash Table is full")

    def modular_hash(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self.size

    def __setitem__(self, key, value):
        hash_code = self.modular_hash(key)
        if self.bucket[hash_code] is None:
            self.bucket[hash_code] = (key, value)
        else:
            self.bucket[self.linear_probe(key, hash_code)] = (key, value)
    
    def __getitem__(self, key):
        hash_code = self.modular_hash(key)
        if self.bucket[hash_code] is None:
            return None
        for index in self.probe_range(hash_code):
            if self.bucket[index] is None:
                return None
            if type(self.bucket[index]) != bool:
                if self.bucket[index][0] == key:
                    return self.bucket[index][1]

    def __delitem__(self, key):
        hash_code = self.modular_hash(key)
        if self.bucket[hash_code] is None:
            return None
        for index in self.probe_range(hash_code):
            if self.bucket[index] is None:
                raise Exception("Key does not exist in Hash Table")
            if self.bucket[index][0] == key:
                self.bucket[index] = None
                break

------------------------------------------------------------
Multiplicative Hash and Linear Probing

    def probe_range(self, index):
        return [*range(index, len(self.bucket))] + [*range(0, index)]

    def linear_probe(self, key, index):
        for index in self.probe_range(index):
            if self.bucket[index] is None:
                return index
            if type(self.bucket[index]) != bool:
                if self.bucket[index][0] == key:
                    return index
        raise Exception("Hash Table is full")

    def multiplicative_hash(self, key):
        constant = (3^40)/(2^64)
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return floor(self.size * (modf(hash_code * constant)[0]))

    def __setitem__(self, key, value):
        hash_code = self.multiplicative_hash(key)
        if self.bucket[hash_code] is None:
            self.bucket[hash_code] = (key, value)
        else:
            self.bucket[self.linear_probe(key, hash_code)] = (key, value)
    
    def __getitem__(self, key):
        hash_code = self.multiplicative_hash(key)
        if self.bucket[hash_code] is None:
            return None
        for index in self.probe_range(hash_code):
            if self.bucket[index] is None:
                return None
            if type(self.bucket[index]) != bool:
                if self.bucket[index][0] == key:
                    return self.bucket[index][1]

    def __delitem__(self, key):
        hash_code = self.multiplicative_hash(key)
        if self.bucket[hash_code] is None:
            return None
        for index in self.probe_range(hash_code):
            if self.bucket[index] is None:
                raise Exception("Key does not exist in Hash Table")
            if type(self.bucket[index]) != bool:
                if self.bucket[index][0] == key:
                    self.bucket[index] = None
                    break

------------------------------------------------------------
For Insertion:

hash_table = HashTableXXXX()

def insert(hash_table):
    letters = string.ascii_lowercase
    for i in range(100): #N = 100
        key = "".join(random.choice(letters) for i in range(random.randint(1,26)))
        hash_table[key] = False #Generates a random combination of letters from lengths 1-26

initial_time = time.time()

insert(hash_table)

execution_time = time.time() - initial_time

------------------------------------------------------------
For Retrieval:

hash_table = HashTableXXXX()

keys = [] #Store a bunch of keys to randomly retrieve from

def insert(hash_table):
    global keys
    letters = string.ascii_lowercase
    for i in range(100): #N = 100
        key = "".join(random.choice(letters) for i in range(random.randint(1,26)))
        keys.append(key)
        hash_table[key] = False #Generates a random combination of letters from lengths 1-26
insert(hash_table)

def retrieve(hash_table):
    global keys
    for key in keys:
        print(key)

initial_time = time.time()

retrieve(hash_table)

execution_time = time.time() - initial_time

------------------------------------------------------------

t_directory = r"XXXX" #XXXX = File Directory
m_directory = r"XXXX"
with open(t_directory,"a") as time_data:
    time_data.write(f"\n{execution_time:.20f}")

with open(m_directory, "a") as memory_data:
    memory_data.write(f"\n{hash_table.memory_usage()}")

------------------------------------------------------------

for execution in range(100):
    exec(open(f"XXXX").read()) #XXXX = File Directory
