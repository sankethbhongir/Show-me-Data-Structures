class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


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
    # Your Solution Here
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    pass