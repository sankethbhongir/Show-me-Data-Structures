import sys
import heapq
from collections import deque

'''Queue used to print tree nodes'''
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

''' HuffmanTree, which has huffman nodes'''
class HuffmanTree():
    
    def __init__(self):
        self.root = None
        
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root
    
    """
    print function for tree
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
 
''' huffman node used to create huffman tree'''       
class HuffmanNode:
    
    def __init__(self,char=None,freq=None, left=None, right= None, bit=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.bit = bit
    
    def set_char(self, char):
        self.char = char
        
    def get_char(self):
        return self.char
    
    def set_bit(self, bit):
        self.bit = bit
        
    def get_bit(self):
        return self.bit
        
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
    
    # comparing huffman nodes    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __repr__(self):
        return f"HuffmanNode({self.char, self.freq, self.bit})"
  
    def __str__(self):
        return f"HuffmanNode({self.char, self.freq, self.bit})"


def path_from_root_to_node(root, char):
    
    """
    :param: root - root of binary tree
    :param: char - value (representing a node's char)
    
    returns: bit string from root to node utilizing path_from_node_to_root function
    """   
    
    # untilizing node_to_root function to get root-node path
    def path_from_node_to_root(root, char):
        """
        :param: root - root of binary tree
        :param: char - value (representing a node's char)
        
        returns: bit string from node to root
        """
        # Base Case
        if root is None:
            return None
        elif root.char == char:
            return root.get_bit()
        
        # recursively traversing left sub-tree bits
        left_answer = path_from_node_to_root(root.left, char)
        left_bit = root.get_bit()
        if  left_answer is not None:
            # if left-root node does not have a bit assigned, we are returning rest of the path
            if left_bit is None:
                return left_answer
            else:
                left_answer+=left_bit
                return left_answer
        
        # recursively traversing right sub-tree bits
        right_answer = path_from_node_to_root(root.right, char)
        right_bit = root.get_bit()
        if  right_answer is not None:
            # if right-root node does not have a bit assigned, we are returning rest of the path
            if right_bit is None:
                return right_answer
            else:
                right_answer+=right_bit
                return right_answer
            
        return None

    output_code = path_from_node_to_root(root,char)
    
    # reversing the output to get path from root to node
    return output_code[::-1]
    
def huffman_encoding(data):
    """
    :param: data - string to be encoded
    
    returns: bit-string (i.e encoded data) and Huffman tree
    """
    # edge case if data is empty string
    if not data:
        return '', None
    
    # creating freqency table for characters in the data
    freq_table = {}
    for char in data:
        freq_table[char] = freq_table.get(char, 0) + 1        
    #print(freq_table)
    
    # creating min-heap with HuffmanNodes
    min_heap = []
    for char, freq in freq_table.items():
        node  = HuffmanNode(char, freq)
        heapq.heappush(min_heap, node)
    #print(min_heap)
    
    # edge case if data is having single character
    if len(min_heap) == 1:
        root_node = heapq.heappop(min_heap)
        root_node.set_bit('0')
        heapq.heappush(min_heap, root_node)
    else:    
        # Building Huffman Tree
        while len(min_heap)>1:
            
            # poping out two min nodes from the min_heap
            min_node1 = heapq.heappop(min_heap)
            min_node2 = heapq.heappop(min_heap)
            
            # creating internal node with a frequency equal to the sum of the two min nodes
            internal_node = HuffmanNode()
            internal_node.freq = min_node1.freq + min_node2.freq
            
            # assigning 1st min-node as left child to internal node, and bit-0 to left chuld
            min_node1.set_bit('0')
            internal_node.set_left_child(min_node1)
            
            # assigning 2nd min-node as right child to internal node, and bit-1 to right child
            min_node2.set_bit('1')
            internal_node.set_right_child(min_node2)
            
            # Pushing internal node back to the heap
            heapq.heappush(min_heap, internal_node)
        
    # initializng Huffman Tree
    huffman_tree = HuffmanTree()
    huffman_tree.set_root(min_heap[0])
    #print(huffman_tree)
    root = huffman_tree.get_root()
    
    # updating freqency table by generating unique code for each character in our data
    for char in freq_table:
        freq_table[char] = path_from_root_to_node(root, char)
        
    # encoding our data using the unique codes from the freqency table
    encoded_data = ''
    for char in data:
        encoded_data+=freq_table[char]
        
    return encoded_data, huffman_tree

def huffman_decoding(encode_data,huff_tree):
    """
    :param: encoded data - bit string
    
    returns: decoded data (i.e actual data, our data)
    """
    
    # edge case, if the data is empty
    if (not encode_data) and  huff_tree is None:
        return None
    
    # root node of the Huffman tree
    root = huff_tree.get_root()
    
    # edge case; if data is having single character
    if (not root.has_left_child()) and (not root.has_right_child()):
        return root.get_char() * len(encode_data)
    
    # decoding using Huffman tree
    decoded_string = ''
    node = root
    
    for bit in encode_data:
        # If the current bit of encoded data is 0, move to the left child,
        # else move to the right child of the tree if the current bit is 1
        if bit == '0':
            node = node.get_left_child()
        else:
             node = node.get_right_child()  
             
         # if a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string
         # and moving back to root
        decoded_char = node.get_char()
        if decoded_char is not None:
            decoded_string+= decoded_char
            node = root
            
    return decoded_string
        

if __name__ == "__main__":
  
    print('------------------ Test Case 1 --------------------------')
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # size should get reduced
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))
    # The bird is the word
    
    print('\n------------------ Test Case 2 --------------------------')
    a_great_sentence = "AAAAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # size should get reduced
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))
    # BBBBBBBB
    
    print('\n------------------ Test Case 3 --------------------------')
    a_great_sentence = ""

    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # empty string
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the dencoded data is: {}\n".format(decoded_data))
    # None
    
    
