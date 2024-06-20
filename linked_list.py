class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def to_array(self):
        arr = []
        if self.head is None:
            return arr
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr
    
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
    
    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        # the below if statement helps us to keep track of the last node from the beginning itself, so that when we have to add a node to the end of the linked list, we do not have to traverse the whole linked list to do so.
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        
        # the below traversal using while loop is no longer needed as we are now keeoing track of the last node when we add a node for the first time itself. This optimizes our linked list data structure.
        if self.last_node is None:
            print("last node is None")
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = Node(data, None)
            self.last_node = node.next_node
        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node
