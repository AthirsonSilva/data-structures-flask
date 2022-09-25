class Node:
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node
            

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None