class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, max_size):
        self.map = {}
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.size = 0

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node is self.tail and self.tail.next is not None:
                self.tail = node.next
            self.head.next = node
            self.head = node
            self.map[key] = node
        else:
            if self.size < self.max_size:
                node = Node(key, value)
                node.prev = self.head
                if self.head is not None:
                    self.head.next = node
                if self.tail is None:
                    self.tail = node
                if self.size == 1:
                    self.tail.next = node
                self.head = node
                self.map[key] = node
                self.size += 1
            else:
                # node_tail = self.tail
                if self.tail is not None:
                    self.map.pop(self.tail.key)
                    self.tail = self.tail.next
                    # print(node_tail.value)
                    if self.tail:
                        self.tail.prev = None
                node = Node(key, value)
                node.prev = self.head
                self.head.next = node
                self.head = node
                self.map[key] = node

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node is self.tail and self.tail.next is not None:
                self.tail = node.next
            temp = self.head
            self.head.next = node
            self.head = node
            self.head.prev = temp
            value = node.value
            return value
        return -1

def main():
    cache = LRUCache(2); 
    #  it will store a key (1) with value  10 in the cache. 
    cache.set(1, 10)  
    cache.set(2, 20)  

    print("Value for the key: 1 is " , cache.get(1)); # returns 10 
    # print("Value for the key: 2 is ", cache.get(2)); # returns -1 (not found) 

    # evicts key 2 and store a key (3) with  value 30 in the cache. 
    cache.set(3, 30)  
    print("Value for the key: 2 is ", cache.get(2)); # returns -1 (not found) 

    # evicts key 1 and store a key (4) with value 40 in the cache. 
    cache.set(4, 40)
    print("Value for the key: 1 is " , cache.get(1)); # returns -1 (not found) 
    print("Value for the key: 3 is " , cache.get(3)); # returns 30 
    print("Value for the key: 4 is ", cache.get(4)); # return 40 


def customeCache():
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(3, 2)  
    print(cache.get(3))
    print(cache.get(2))
    cache.set(4, 3)  
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))


customeCache()
# main()
