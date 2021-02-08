# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):

        index = self._hash_mod(key)
        node = self.storage[index]
        # Question for Pascal - when I try to run the resize function - I get an error on this line saying "list index out of range" but I don't fully understand why
    
        # If there is already something at that index of the array
        if node == None:
            self.storage[index] = LinkedPair(key, value)
            # Question for Pascal: Why does node = LinkedPair(key,value) not work on line 53 instead?
            return
          
        while node is not None:
            current = node
            if current.key == key:
                current.value = value
                return
            # Move along each time to the next node until the end of the list  
            node = node.next
        # Once the node in the while loop becomes None - the while loop exits, but current still evaluates to the previous node, so we can assign current.next
        # current.next becomes the new node with the new LinkedPair value    
        current.next = LinkedPair(key, value)        


        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        



    def remove(self, key):

        index = self._hash_mod(key)
        node = self.storage[index]

        while node != None and node.key != key:
            current = node
            node = node.next

        if self.storage[index] == None:
            print("Sorry, key not found")
            return

        current = node
        node.value = None
        current.next = node.next
                   


        # self.storage[index] = None    
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
      


    def retrieve(self, key):

        index = self._hash_mod(key)
        node = self.storage[index]

        while node != None and node.key != key:
            node = node.next

        if node == None:
            return None
        return node.value         



        # if node is None:
        #     return None
        # else:

        #     return self.storage[index].value
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        


    def resize(self):
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
       
        # Loop through the old_storage
        for i in old_storage:
            # if the entry is not None
            # if i is not None:
                # take that entry and insert the key value pair into the new storage using the insert function
                # self.insert(i.key, i.value)
                # if the entry has a next, then move to that entry and do the same thing until there is no next

            # Question for Pascal: I was unsure of whether the code would work without lines 148 and 150 but it does... Might need to chat about it.
            
            while i is not None:
                self.insert(i.key, i.value)
                i = i.next

        #     new_storage[i] = self.storage[i]

        # self.storage = new_storage    

        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
