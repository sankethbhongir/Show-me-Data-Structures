class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        
        # Queue to track recently used keys
        self.queue = []
        # dictionary to store key value pair
        self.cache_dict = {}
        # capacity of our cache
        self.capacity = capacity
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache_dict:
            # moving recently used keys to the end 
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_dict[key]
        else:
            return -1
    
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the least used item. 
        if key not in self.cache_dict:
            if not self.is_capacity_full():
                self.cache_dict[key] = value
                self.queue.append(key)
            else:
                least_used = self.queue.pop(0)
                del self.cache_dict[least_used]
                self.cache_dict[key] = value
                self.queue.append(key)
        else:
            return '{} Key is already present in cache'.format(key)
            
    def is_capacity_full(self):
        return len(self.queue) == self.capacity
    
    def get_keys(self):
        return self.cache_dict.keys()
    

''' Test Case 1'''            
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get_keys()) #[1,2,3,4]

print(our_cache.get(1))       
# returns 1
print(our_cache.get(2))       
# returns 2
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get_keys()) 
#returns [1,2,4,5,6]

print(our_cache.get(3))      
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

''' Test Case 2'''
our_cache = LRU_Cache(5)
our_cache.set('a', 1)
our_cache.set('b', 2)
our_cache.set('c', 3)
our_cache.set('d', 4)
print(our_cache.set('d', 4)) # d Key is already present in cache
our_cache.set('e', 5)
print(our_cache.get_keys()) #[a,b,c,d,e]

''' Test Case 3'''
our_cache = LRU_Cache(5)
our_cache.set('a', 1)
our_cache.set('b', 2)
our_cache.set('c', 3)
our_cache.set('d', 4)
our_cache.set('e', 5)

print(our_cache.get('a'))       
# returns 1
print(our_cache.get('b'))       
# returns 2
print(our_cache.get('c'))  
# returns 3
print(our_cache.get('d'))       
# returns 4
print(our_cache.get('e'))       
# returns 5
our_cache.set('f', 6)
print(our_cache.get_keys()) #[b,c,d,e,f]
