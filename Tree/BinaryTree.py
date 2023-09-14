import sys
import queue
class Node:
    def __init__(self, data, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree:
    def __init__(self, root = None):
        self.root = root

    def isEmpty(self):
        return not self.root # empty: return true, else: return False
    
    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if not cur.lchild:
                    cur.lchild = node
                    return
                elif not cur.rchild:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def getLeft(self):
        return self.root.lchild
    
    def getRight(self):
        return self.root.rchild

    def printTree(self):
        if self.isEmpty():
            return None
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                print(cur.data)
                if cur.lchild:
                    queue.append(cur.lchild)
                if cur.rchild:
                    queue.append(cur.rchild)

    def preOrder(self, node = None):
        if node is not None:
            print(node.data)
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)
    def inOrder(self, node = None):
        if node is not None:
            self.inOrder(node.lchild)
            print(node.data)
            self.inOrder(node.rchild)
    def postOrder(self,node = None):
        if node is not None:
            self.postOrder(node.lchild)
            self.postOrder(node.rchild)
            print(node.data)            
k = BiTree()
for i in range(7):
    k.add(i)
print("Print Entire tree by level")
k.printTree()
print("Print tree in preOrder")
k.preOrder(k.root)
print("Print tree in inOrder")
k.inOrder(k.root)
print("Print tree in postOrder")
k.postOrder(k.root)