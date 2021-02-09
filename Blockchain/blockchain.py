import hashlib
import time
from datetime import datetime



class Block:

    def __init__(self, data, previous_hash=None):
        self.timestamp = self.calc_gmt()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        data = self.data + ' created at ' + str(self.timestamp)
        hash_str =  data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_hash(self):
        return self.hash
    
    def calc_gmt(self):
        rightnow = time.time()
        utc = datetime.utcfromtimestamp(rightnow)
        return utc
    
    def __str__(self):
        return f"timestamp: {self.timestamp}\n data: {self.data} \n previous_hash: {self.previous_hash} \n hash: {self.hash}"
        

class Blockchain:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        if self.head is None:
            self.head = Block(data)
            self.tail = self.head
            return
        
        self.tail.next = Block(data)
        self.tail.next.previous_hash = self.tail.get_hash()
        self.tail = self.tail.next
        return
    
    def __repr__(self):
        s = 'Block Chain\n\n'
        block = self.head
        while block:
            s +=   str(block) + '\n\n'
            block = block.next
            
        return s
        
   
''' Test Case 1 '''     
block_chain = Blockchain()
block_chain.append('abc')
block_chain.append('xyz')
block_chain.append('123')
print(block_chain)  
# prints blocks connected to each other 

''' Test Case 2 '''     
block_chain = Blockchain()
block_chain.append('abc')
block_chain.append('123')
block_chain.append('abc')
print(block_chain)  
# prints blocks connected to each other where same data has unique hash

''' Test Case 3 '''     
block_chain = Blockchain()
block_chain.append('abc')
block_chain.append('abcd')
block_chain.append('abcde')
block_chain.append('123')
block_chain.append('1234')
block_chain.append('12345')
block_chain.append('xyz')
block_chain.append('987')
block_chain.append('this')
block_chain.append('is')
block_chain.append('block')
block_chain.append('chian')
block_chain.append('using')
block_chain.append('linked')
block_chain.append('list')
print(block_chain)  
# prints large block chain

