class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
    
    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return
        
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1
        return

    def get_size(self):
        return self.size

def union(llist_1, llist_2):
    '''
    args: Two linked lists
    returns:  union of two linked lists
    '''
    
    # hash table to store unique values
    hash_table = {}
    
    union_llist = LinkedList()
    
    # traversing first linked list
    node_l1  = llist_1.head
    while node_l1:
        node_value = node_l1.get_value()
        
        # checking if we have already seen the element  
        # if not then add it to output list 
        if node_value not in hash_table:
            union_llist.append(node_value)
        hash_table[node_value] = hash_table.get(node_value, 0) + 1
        node_l1 = node_l1.next  
    
    # traversing second linked list
    node_l2  = llist_2.head
    while node_l2:
        node_value = node_l2.get_value()
        
        # checking if we have already seen the element  
        # if not then add it to output list 
        if node_value not in hash_table:
            union_llist.append(node_value)
        hash_table[node_value] = hash_table.get(node_value, 0) + 1
        node_l2 = node_l2.next
        
    return union_llist

def intersection(llist_1, llist_2):
    '''
    args: Two linked lists
    returns:  intersection of two linked lists
    '''
    
    # hash tables to unique values
    hash_table1 = {}
    hash_table2 = {}
    
    inter_llist = LinkedList()

    # traversing first linked list and adding the data to its corresponding hash table (i.e hash_table2))
    node_l1  = llist_1.head
    while node_l1:
        node_value = node_l1.get_value()
        hash_table1[node_value] = hash_table1.get(node_value, 0) + 1
        node_l1 = node_l1.next  

    # traversing second linked list and adding the data to its corresponding hash table (i.e hash_table2)
    node_l2  = llist_2.head
    while node_l2:
        node_value = node_l2.get_value()
        hash_table2[node_value] = hash_table2.get(node_value, 0) + 1
        node_l2 = node_l2.next

    # iterating through our first hash table to see if the element is present in 
    # second hash table, if yes then thats our intersect element
    for i in hash_table1:
        if i in hash_table2:
            inter_llist.append(i)
            
    return inter_llist

