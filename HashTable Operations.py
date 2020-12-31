#IB Extended Essay - Linear Probing vs Chaining Collision Handling Python 3.8.3 64-Bit
------------------------------------------------------------

Prerequisites

import time #Measures execution time in seconds
from sys import getsizeof #Measures memory usage in bytes
from math import floor, modf #For multiplicative Hashing only

class HashTablesXXXX: #Hash Table Specification
    def __init__(self):
        self.size = XXXX #10000 or 1000000 = Small / Large
        self.bucket = [XXXX for generation in range(self.size)] #[] for chaining, False for linear probing collisions, None for linear probing non collisions
        self.bucket[655] = None #Only For Linear Probing Collisions! This simulates O(n) collisions as "lpvsch" with hash code 656

    def print_bucket(self):
        print(self.bucket)

    def memory_usage(self):
        print(getsizeof(self.bucket))

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

#Collisions HC = 656
hash_table["lpvshc"] = False
hash_table["lpvcsh"] = False
hash_table["lpvchs"] = False
hash_table["lpvhsc"] = False
hash_table["lpvhcs"] = False
hash_table["lpsvch"] = False
hash_table["lpsvhc"] = False
hash_table["lpscvh"] = False
hash_table["lpschv"] = False
hash_table["lpshvc"] = False
hash_table["lpshcv"] = False
hash_table["lpcvsh"] = False
hash_table["lpcvhs"] = False
hash_table["lpcsvh"] = False
hash_table["lpcshv"] = False
hash_table["lpchvs"] = False
hash_table["lpchsv"] = False
hash_table["lphvsc"] = False
hash_table["lphvcs"] = False
hash_table["lphsvc"] = False
hash_table["lphscv"] = False
hash_table["lphcvs"] = False
hash_table["lphcsv"] = False
hash_table["lvpsch"] = False
hash_table["lvpshc"] = False
hash_table["lvpcsh"] = False
hash_table["lvpchs"] = False
hash_table["lvphsc"] = False
hash_table["lvphcs"] = False

#Apply Operation on...
hash_table["lpvsch"] = True

#Non-Collisions
hash_table["%$gD"] = True
hash_table["]Sz@#"] = True
hash_table["!"] = True
hash_table["~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"] = True
hash_table["uvjolx"] = True
hash_table["hajtnulkajsx"] = True
hash_table["djbaffcgtipyyfswqnu"] = True
hash_table["aph"] = True
hash_table["wszajlikf"] = True
hash_table["cnnvsvltndqddogr"] = True
hash_table["lrihcznaxwxshs"] = True
hash_table["kqnzfswojjjhmveoyfqrngitubppwtertuuvxprdywpsha"] = True
hash_table["wngnadicsxqfblkrqfygtrfrix"] = True
hash_table["valnrmpew"] = True
hash_table["fqvsojexjkqlqjtlmzweq"] = True
hash_table["gfkapbqgza"] = True
hash_table["facab"] = True
hash_table["ilffibzd"] = True
hash_table["pdpnykngegzqfz"] = True
hash_table["ltcsbmlgi"] = True
hash_table["zfgcdviookjdefi"] = True
hash_table["prfgquaazjliwsobpdpogbhmhhnhaioivwhzrrfydrngwvlglgjrhlbhrt"] = True
hash_table["gdvub"] = True
hash_table["aqsuwiw n g v a"] = True
hash_table["cwafkhh"] = True
hash_table["fwwmizcazhaapq"] = True
hash_table["zobrutuanrttiwlwlgpdwtjshvnp"] = True
hash_table["taezifxqrmwmun"] = True
hash_table["lmsjwtnqsqwchdushxzauqwkbybpnawfsrvurowzptvhvdwzusizpcbbuzfonqgqhhyfnovtsnaogitluacvx"] = True

#Apply operation on...
hash_table["mxibee"] = True

------------------------------------------------------------

hash_table = HashTableXXXX()

#Prior key insertions here...

initial_time = time.time()

#Operation is set here...
For insertions:
    hash_table["XXXX"] = True

For retrieving:
    print(XXXX)

For deletion:
    del XXXX

execution_time = time.time() - initial_time

directory = r"XXXX" #XXXX = File Directory
with open(directory,"a") as dataset:
    dataset.write(f"\n{execution_time:.20f}")
    
hash_table.memory_usage()

------------------------------------------------------------

for execution in range(100):
    exec(open(f"XXXX").read()) #XXXX = File Directory
