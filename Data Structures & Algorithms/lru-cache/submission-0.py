class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.catche = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from catche
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        if key in self.catche:
            self.remove(self.catche[key])
            self.insert(self.catche[key])
            return self.catche[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.catche:
            self.remove(self.catche[key])
        self.catche[key] = Node(key, value)
        self.insert(self.catche[key])

        if len(self.catche) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.catche[LRU.key]


        

        
