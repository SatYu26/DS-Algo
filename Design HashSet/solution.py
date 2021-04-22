class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 15000
        self.buckets = [[] for i in range(self.numBuckets)]
        
    def hash_function(self, key):
        return key % self.numBuckets
        

    def add(self, key: int) -> None:
        i = self.hash_function(key)
        
        if not key in self.buckets[i]:
            self.buckets[i].append(key)  

    def remove(self, key: int) -> None:
        i = self.hash_function(key)
        
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
        
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.hash_function(key)
        
        if key in self.buckets[i]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)