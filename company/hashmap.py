

class Hashmap:
    def __init__(self):
        self.arr =[0] * 20 

    def get_hash_value(self, s):
        hash = 0
        for i in range(len(s)):
            hash += ord(s[i])
        return hash % 10

    def add_item(self, key, value):
        hash_key = self.get_hash_value(key)
        self.arr[hash_key] = value 
        return "done"

    def get_item(self, key):
        hash_key = self.get_hash_value(key)
        value = self.arr[hash_key]
        return value

def main():
    lr = Hashmap()
    print(lr.add_item("a", 1))
    print(lr.get_item("a"))
    print(lr.add_item("b", 2))
    print(lr.get_item("b"))

main()


