import sys
import heapq
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
        
    def __len__(self):
        return len(self.q)

class HuffmanTree():
    
    def __init__(self):
        self.root = None
        
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root
    
    """
    define the print function
    """
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level
                
        return s
        
class HuffmanNode:
    def __init__(self,char=None,freq=None, left=None, right= None, code=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = code
    
    def set_code(self, code):
        self.code = code
        
    def get_code(self):
        return self.code
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __repr__(self):
        return f"HuffmanNode({self.char, self.freq, self.code})"
  
    def __str__(self):
        return f"HuffmanNode({self.char, self.freq, self.code})"


def huffman_encoding(data=None):
    min_heap = []
    for key, value in codes.items():
        node  = HuffmanNode(key, value)
        heapq.heappush(min_heap, node)
    print(min_heap)
    
    while len(min_heap)>1:
        min_node1 = heapq.heappop(min_heap)
        min_node2 = heapq.heappop(min_heap)
        internal_node = HuffmanNode()
        internal_node.freq = min_node1.freq + min_node2.freq
        min_node1.set_code('0')
        internal_node.set_left_child(min_node1)
        min_node2.set_code('1')
        internal_node.set_right_child(min_node2)
        heapq.heappush(min_heap, internal_node)
        
    huffman_tree = HuffmanTree()
    huffman_tree.set_root(min_heap[0])
    print(huffman_tree)
    return 

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {'A': 7,
             'B': 3,
             'C': 7,
             'D': 2,
             'E': 6
             }
    huffman_encoding()

'''
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
'''