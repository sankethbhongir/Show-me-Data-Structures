import sys
import heapq
import heapq

class Node:
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree():
    def __init__(self, value=None):
        self.root = Node(value) 
    def get_root(self):
        return self.root
    
class HuffmanNode:
    def __init__(self,char=None,freq=None, left=None, right= None, code=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = code
                
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __repr__(self):
        return f"HuffmanNode({self.char, self.freq})"


def huffman_encoding(data=None):
    min_heap = []
    for key, value in codes.items():
        node  = HuffmanNode(key, value)
        heapq.heappush(min_heap, node)
    print(min_heap)
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