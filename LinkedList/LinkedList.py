
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.cur_node = None

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return "Found it"
            cur = cur.next
        return "Node is not in Lined List"
            
    def append_node(self, value):
        if self.cur_node == None:
            node = Node(value)
            self.head = node
            self.cur_node = node
        else:
            while self.cur_node is not None:
                if self.cur_node.next is None:
                    node = Node(value)
                    node.val = value
                    self.cur_node.next = node
                    self.cur_node = self.cur_node.next
                    break # once the node has been append, we need to suspend the loop
                else:
                    self.cur_node = self.cur_node.next
    def insert_node(self, val, idx):
        cur = self.head
        index = 0
        while cur:
            if index == idx:
                print(f"Found a slot, insert {val} after index {idx}")
                next_part = cur.next # record rest of the list
                node = Node(val) # create a new node
                node.next = next_part # node's next = next_part, so currently next part = node + next_part
                cur.next = node
                return
            index += 1
            cur = cur.next
        print("Not Found a space to insert")
    def remove_ndoe(self, val):
        cur = self.head
        while cur:

            if cur.next.val == val and cur.next is not None:
                sub = cur.next.next
                cur.next = sub
            cur = cur.next

    def reverse_linked_list(self):
        list = []
        cur = self.head
        while cur:
            list.append(cur.val)
            
            cur = cur.next
        list.reverse()
        cur_new = self.head
        index = 0
        while cur_new:
            cur_new.val = list[index]
            cur_new = cur_new.next
            index += 1
        
    def display(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


list = SLinkedList()
list.append_node(3)
list.append_node(4)
list.append_node(6)
print("---------Insert Node----------")
list.insert_node(5,0)
list.display()
print("-----------Remove Node---------")
list.remove_ndoe(6)
list.display()
print("-----------Reverse-----------")
list.reverse_linked_list()
list.display()