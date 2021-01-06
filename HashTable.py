import time #Measures execution time in seconds
from sys import getsizeof #Measures memory usage in bytes
from math import floor, modf #For multiplicative Hashing only
import random #For randomization of strings
import string #For random strings

class HashTable: #Hash Table Specification
    def __init__(self, M, hf, ch):
        self.size = M #Prime number at large size
        self.ch = ch
        self.hf = hf
        if ch == "lp":
            self.bucket = [None for generation in range(self.size)] #[] for chaining, None for linear probing
        elif ch == "ch":
            self.bucket = [[] for generation in range(self.size)]

    def print_bucket(self):
        print(self.bucket)

    def memory_usage(self):
        return getsizeof(self.bucket)

    def hash_function(self, key):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        if self.hf == "mod":
            return hash_code % self.size
        elif self.hf == "mu":
            constant = (3^40)/(2^64)
            return floor(self.size * (modf(hash_code * constant)[0]))

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

    def __setitem__(self, key, value): 
        hash_code = self.hash_function(key)
        if self.ch == "ch":
            found = False
            for index, element in enumerate(self.bucket):
                if len(element) == 2 and element[0] == key:
                    self.bucket[hash_code][index] = (key, value)
                    break
            if not found:
                self.bucket[hash_code].append((key, value))
        elif self.ch == "lp":
            if self.bucket[hash_code] is None:
                self.bucket[hash_code] = (key, value)
            else:
                self.bucket[self.linear_probe(key, hash_code)] = (key, value)

    def __getitem__(self, key): 
        hash_code = self.hash_function(key)
        if self.ch == "ch":
            for elements in self.bucket[hash_code]:
                if elements[0] == key:
                    return elements[1]
            raise Exception("Key does not exist in Hash Table")
        elif self.ch == "lp":
            if self.bucket[hash_code] is None:
                return None
            for index in self.probe_range(hash_code):
                if self.bucket[index] is None:
                    return None
                if type(self.bucket[index]) != bool:
                    if self.bucket[index][0] == key:
                        return self.bucket[index][1]

N = 10000

letters = string.ascii_lowercase
keys = []
for i in range(N):
    keys.append("".join(random.choice(letters) for i in range(random.randint(1,26))))

def insert(hash_table):
    global keys
    for key in keys:
        hash_table[key] = False

def retrieve(hash_table):
    global keys
    for key in keys:
        print(hash_table[key])

operations = (
    [100003,"mod","ch"],
    [19991,"mod","ch"],
    [11113,"mod","ch"],
    [100003,"mod","lp"], 
    [19991,"mod","lp"],
    [11113,"mod","lp"],
    [100003,"mu","ch"], 
    [19991,"mu","ch"],
    [11113,"mu","ch"],
    [100003,"mu","lp"],
    [19991,"mu","lp"],
    [11113,"mu","lp"]
    )

directories = (
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModCH Execution Time/SModCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModCH Execution Time/HModCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModCH Execution Time/LModCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModLP Execution Time/SModLP.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModLP Execution Time/HModLP.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/ModLP Execution Time/LModLP.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuCH Execution Time/SMuCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuCH Execution Time/HMuCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuCH Execution Time/LMuCH.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuLP Execution Time/SMuLP.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuLP Execution Time/HMuLP.csv",
    r"/Users/mingchungxia/Desktop/IB Extended Essay Data/Version 3/MuLP Execution Time/LMuLP.csv",
)

for i, op in enumerate(operations):

    hash_table = HashTable(op[0],op[1],op[2])

    with open(directories[i], "a") as file:
        #Insertion
        initial_time = time.time()
        insert(hash_table)
        insertion_time = time.time() - initial_time

        #Retrieval
        initial_time = time.time()
        retrieve(hash_table)
        retrieval_time = time.time() - initial_time
        file.write(f"\n{insertion_time:.20f},{retrieval_time:.20f}")
    
    print(f"Completed {i} operation.")