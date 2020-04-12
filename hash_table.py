""" hash_table.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 5
Module 5.12 Sorting and Searching Questions.
PE 2.c Hash Table

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft"""
# ------------------------------------------------
"""1. Consider the following list of integers:
[1,2,3,4,5,6,7,8,9,10].  Show how this list is
sorted by the following algorithms:

    bubble sort
    selection sort
    insertion sort
    
2.a What is the difference between a list and a
dictionary?

2b. How are they coded differently and what
different implementations they have?

2c. Build a script that utilizes at least one
list and one dictionary (note: Hash Function in
Rubric).    

In addition to coding these tasks, you must post
a video running and explaining your code.  This
allows for you to demonstrate what is occurring
in the code as it is happening and how it is
organized.  You must also run your code in the
video to explain the output and why the program
produced that output."""
# ------------------------------------------------
"""GitHub Submission Instructions:
Click on the following link to accept the
assignment and create your remote GitHub
repository. After you accept the assignment you
will be able to clone the repository in GitHub
desktop.

Once you complete these exercises, be sure you
have committed your solutions locally and pushed
them up to the remote repository. If you are
unsure how to clone the repository for this
assignment, please review Pull and Push for
Assignments.

You can also upload them to canvas.

GitHub Link:
https://classroom.github.com/a/FZrZZ3AK"""
# ------------------------------------------------
"""Sorting Rubric
1. Bubble Sort Readability - Code is readable and
   well organized.
2. Bubble Sort Funtionality - Bubble Sort runs
   properly.
3. Bubble Sort Output - Bubble Sort produces 
   proper output.
4. Selection Sort Readability - Code is readable
   and well organized.
5. Selection Sort Functionality - Selection Sort
   runs properly.
6. Selection Sort Output - Selection Sort produces
   proper output.
7. Insertion Sort Readability - Code is readable
   and well organized.
8. Insertion Sort Funtionality - Insertion Sort
   runs properly.
9. Insertion Sort Output - Insertion Sort produces 
   proper output.

10. Hash Function Use - Program properly uses the
    Hash Function.
11. Hash Function Readability - Code is readable
    and well organized with descriptive names
12. Hash Function Output - Hash Function produces
    proper output.

13. Answer all canvas questions.
14. Video Submission - Clearly explains the
    organization and out put of submitted programs.
"""
# ------------------------------------------------
"""When you have completed this assignment and
pushed your work to the remote GitHub repository,
answer the following question(s):

1. How many hours do you estimate you used
     completing this assignment?

2. What was easiest for you when completing
     this assignment?

3. What was the most difficult challenge you
     experienced when completing this assignment
"""
# ------------------------------------------------
# ---------------Class HashTable------------------
"""
class HashTable; aka Map or Dictionary.


Uses two lists to create a HashTable class that 
implements the Map abstract data type. One list,
called slots, will hold the key items and a
parallel synchronised list, called data, will hold
the data values. When we look up a key, the
corresponding position in the data list will hold
the associated data value.

HashTable() Create a new, empty HashTable. It
returns an empty HashTable collection.

put(key,val) Add a new key-value pair to the
HashTable. If the key is already in the HashTable
then replace the old value with the new value.
Put includes a check for need to auto resize
the HashTable. If needed calls resize.

__setitem__ Calls put(key, data). Enables
H[key]=data with data = value for key.

get_value(key) Given a key, return the value
stored in the HashTable or None otherwise.

__getitem__ Calls get(key). Enables H[key] to get
value.

get_all_keys() Return all keys in HashTable.

get_all_values() Return all values in HashTable.

len_of_table() Return the positions or size of
the HashTable that may be filled or empty (None).

len_of_entries() Return the number of key:value
pairs that are in the HashTable. 

delete_key_value_pair(key) Delete the key-value
pair from the HashTable using a statement of the
form del HashTable[key]. Returns True if deleted
and False if the Key did not exist.

key_in_dict(key) Return True for a statement of
the form key in HashTable, if the given key is in
the HashTable, False otherwise.

_hash_function(key) Hashes the key using
key%self.size with size being len_of_table.

_rehash(oldhash) Rehashes the hash_function using
linear probing using (oldhash+1)%self.size for
collision resolution.

_resize(new_size) Resizes the HashTable and the
underlying list for keys (slots) and list for
values (data). Put method calls resize and uses
loading factor of if entries > size//2 then temp
copy old table, make table 2x -1, then reload old
keys and values with new hash."""

class HashTable:
    # -----------HashTable Constructor------------    
    def __init__(self):
        # Table size. Using prime number for 
        # efficient collision resolution as best
        # as can during resizing operations.
        self.size = 11 
        # Hash Table List, contains keys 
        self.slots = [None] * self.size
        # Hash Table List, contains values
        self.data = [None] * self.size  
        # Accumulator for key:value pairs
        self.entries = 0
        
    # ---------HashTable Public Accessors--------
    def get_value(self,key):
        # computes initial hash value
        startSlot = self._hash_function(key)
        data = None                               # initialize
        stop = False                              # initialize
        found = False                             # initialize
        position = startSlot                      # sets position (cursor/tracker) from hashfunction
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:       # if look = key, you found it
                found = True                      # set to True
                data = self.data[position]        # set position value to data to return it
            else:                                 # not in this index/slot, rehash to linear probe next slot(s)
                position=self._rehash(position)
                if position == startSlot:         # end of list
                    stop = True                   # set to True. Stop look.
        return data                               # return value from position. If None returns None.

    def __getitem__(self,key):                    # allows use of H[44] to get value    
        return self.get_value(key)                # alt to H.get(key)                   

    def get_all_keys(self):                       # returns all keys in Hash Table
        return self.slots
    
    def get_all_values(self):                     # returns all values in Hash Table
        return self.data
    
    def len_of_table(self):                       # returns size of Hash Table
        return self.size
    
    def len_of_entries(self):                     # returns quantity of entries in Table
        return self.entries                       # diff between table and entries are empty slots (with None)

    def key_in_dict(self,key):                    # returns boolean True / False on if a key is in the HashTable
        # computes initial hash value.
        startSlot = self._hash_function(key)
        stop = False                              # Initialize
        found = False                             # Initialize
        position = startSlot                      # Set position (cursor/tracker) from hash function
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:       # found index/slot with key in it
                found = True                      # set to True
            else:                                 # not in this index/slot, rehash to linear probe next slot(s)
                position=self._rehash(position)
                if position == startSlot:         # end of list
                    stop = True                   # set to True. Stop look.
        return found                              # returns found True if found, otherwise returns found is False.

    # -----------HashTable Methods----------------    
    def _hash_function(self,key):                 # implements simple remainder method
        return key%self.size           # sample if key = 77 and size = 11, 77 % 11 = 0 (7 remainder 0) hash to 0
                                       # sample if key = 44 and size = 11, 44 % 11 = 0 (4 remainder 0) 0 full, so rehash +1
                                       # since slot 0 is filled with 77, it rehashes to oldHash + 1 = 0 + 1 = 1  hash to 1

    def _rehash(self,oldHash):                    # collision resolution technique is 
        return (oldHash+1)%self.size              # linear probing with a plus 1 rehash
        
    def put(self,key,data):                       # Adds a new key: value pair; if key exists updates value     
        if self.entries > self.size // 2:         # keep load factor <= 0.5
            new_size = (2 * self.size) - 1        # number 2x - 1 is often prime
            self._resize(new_size)                # calls method to resize using new size

        # computes initial hash value
        startSlot = self._hash_function(key)
        
        if self.slots[startSlot] == None:         # if no key add to this slot
            self.slots[startSlot] = key           # set key to this index / slot
            self.data[startSlot] = data           # set value to this index / slot
            self.entries += 1                     # increments accumulator for table entries
        elif self.slots[startSlot] == key:        # if this key exists in this slot, update value with new value
            self.data[startSlot] = data           # replace
        else:
            # if slot not empty, iterates rehash until you find an empty slot
            nextSlot = self._rehash(startSlot)
            while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                nextSlot = self._rehash(nextSlot)
            if self.slots[nextSlot] == None:      # found an empty slot
                self.slots[nextSlot]=key          # set key to this index / slot
                self.data[nextSlot]=data          # set value to this index / slot
                self.entries += 1
                        
            # if nonempty slot already contains the key
            # the old data value is replaced with new data value                    
            else:
                self.data[nextSlot] = data        # replace

    def __setitem__(self,key,data):               # allows use of H[54]="cat"           
        self.put(key,data)                        # alt to H.put(key, data)             
        
    def delete_key_value_pair(self,key):
        # computes initial hash value.
        startSlot = self._hash_function(key)
        stop = False                              # Initialize
        found = False                             # Initialize
        position = startSlot                      # set position (cursor/tracker) from hash function
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:       # found index/slot with key in it
                found = True                      # set to True
                self.data[position] = None        # set value to None
                self.slots[position] = None       # set key to None
                stop = True                       # return True, pair deleted.
                self.entries -= 1    
            else:                                 # not in this index/slot, rehash to linear probe next slot(s)
                position=self._rehash(position)
                if position == startSlot:         # end of list
                    stop = True                   # set to True. Stop look.
                    return found                  # return found is False, failed pair delete. Did not exist.
        return stop                               # return True, pair deleted.

    def _resize(self, new_size):
        """Resize oldSlots and oldData Lists to new_size and rehash (during .put) all items."""
        oldSlots = self.slots                     # temp assignment of old keys list
        oldData = self.data                       # temp assignment of old values list
        self.slots = new_size * [None]            # Re-Initialize; fill key list to new_size with each index set to None
        self.data = new_size * [None]             # Re-Initialize; fill value list to new_size with each index set to None
        self.size = new_size                      # Table size set to new size
        self.entries = 0                          # entries quantity recomputed during re-insertion of old slots:data.
        k=0                                       # Initialize independent accumulator
        for i in oldSlots:                        # iterate through length of old key list
            if oldSlots[k] != None:               # only insert if key exists, skip if key is None
                self.put(oldSlots[k], oldData[k]) # re-insert assigned key and value from old lists using k for index
            k +=1                                 # increment k accumulator for next loop
            continue                              # stop current loop and start new loop at top
                
# ------------------------------------------------
def hash(aList, listsize):                        # standalone function to demo the hash function
    sum = 0                                       # Initialize
    for pos in range(len(aList)):                 # iterate list to hash
        if aList[pos] != None:                    # only sum actual values, if None skip
            #sum = sum + ord(aList[pos])          # unweighted; anagrams will hash same
            sum = sum + ord(aList[pos])*(pos+1)   # weighted for each pos to hash anagrams
        
        
    return sum%listsize  # calculate Hash cat:   312%11 = 4 unweighted,  641%11 =  3 weighted 
                         # calculate Hash apple: 530%11 = 2 unweighted, 1594%11 = 10 weighted
                         # calculate Hash paelp: 530%11 = 2 unweighted, 1601%11 =  6 weighted
                         
# ------------------------------------------------
def hash_table_demo():
    print("\nHash Table Demonstration (aka Map or Dictionary)\n")
    print("Create Hash Table H <H = HashTable()> ")
    H=HashTable()        # create / initialize Hash Table
    print("Hash Table length of table: ", H.len_of_table(), "  Hash Table length of entries:", H.len_of_entries())       
    print("HashTable H keys are:   ", H.get_all_keys())
    print("HashTable H values are: ", H.get_all_values())
    
    print("\nLet's start loading up the table!\n")
    print('Load key: value using put method <H.put(54, "cat")>.   Hash=54%11= 10. Below Resize 54%21= 12.')        
    H.put(54, "cat")
    print('Load key: value using put method <H.put(26, "dog")>.   Hash=26%11= 4.  Below Resize 26%21= 5.')        
    H.put(26, "dog")
    print('Load key: value using put method <H.put(93, "lion")>.  Hash=93%11= 5.  Below Resize 93%21= 9.')        
    H.put(93, "lion")
    print('Load key: value using put method <H.put(17, "tiger")>. Hash=17%11= 6.  Below Resize 17%21= 17.')
    H.put(17, "tiger")
    print("HashTable H keys are:   \n", H.get_all_keys())
    print("HashTable H values are: \n", H.get_all_values())
    print("Hash Table length of table: ", H.len_of_table(), "  Hash Table length of entries:", H.len_of_entries())       

    print("\nNote: During this next .put of 5 items, the table will automatically resize to 21.\n")

    print('Load key: value using square bracket [] method <H[77]="bird">.    Hash=77%11=0. Resize 77%21= 14.')        
    H[77]="bird"
    print('Load key: value using square bracket [] method <H[32]="cow">.     Has=32%11=10. Resize=32%21= 11.')        
    H[32]="cow"
    print('Load key: value using square bracket [] method <H[2]="goat">.     Hash=2%21= 2.')            
    H[2]="goat"
    print('Load key: value using square bracket [] method <H[35]="pig">.     Hash=35%21= 14. Rehash to 15.')                
    H[35]="pig"
    print('Load key: value using square bracket [] method <H[20]="chicken">. Hash=20%21= 20.')                
    H[20]="chicken"
    print("HashTable H keys are:   \n", H.get_all_keys())
    print("HashTable H values are: \n", H.get_all_values())
    print("Hash Table length of table: ", H.len_of_table(), "  Hash Table length of entries:", H.len_of_entries())       

    print("\nLet's assign a new value to key 20 to replace <'chicken'> with <'duck'> using put <H.put(20, 'duck')>")
    H.put(20, 'duck') 
    print("Now let's print value assigned to key H[20] using H[20]: ", H[20])
    
    print("\nLet's do a get value using [ ] access method <H[99]> for a key that does not exist: ", H[99])
    print("Let's do a get value using <H.get_value(99)> for a key that does not exist: ", H.get_value(99))    
    print("Let's see if key 99 is in dictionary/HashTable H using <H.key_in_dict(99): ", H.key_in_dict(99))
    
    print("\nLet's do a get value using [ ] access method <H[55]> for a key that does exist: ", H[55])
    print("Let's do a get value using <H.get(55)> for a key that does exist: ", H.get_value(55))    
    print("Let's see if key 55 is in dictionary/HashTable H using <H.key_in_dict(55): ", H.key_in_dict(55))

    print("\nHashTable H keys are:   \n", H.get_all_keys())
    print("HashTable H values are: \n", H.get_all_values())
    print("Hash Table length of table is: ", H.len_of_table(), "  Hash Table length of entries are:", H.len_of_entries())       
    print("\nDelete a key: value pair using <H.delete_key_value_pair(77)> :", H.delete_key_value_pair(77))
    print("Try to delete a non existent key:value pair using <H.delete_key_value_pair(99)> :", H.delete_key_value_pair(99))
    print("Print results, key: value pair <77:'bird'> removed and now None. Check size and entries.")
    print("\nHashTable H keys are:   \n", H.get_all_keys())
    print("HashTable H values are: \n", H.get_all_values())
    print("Hash Table length of table is: ", H.len_of_table(), "  Hash Table length of entries are:", H.len_of_entries())       

# ------------------------------------------------           
def main():
    aList = ['c', 'a', 't', None, None, None, None, None, None, None, None]
    bList = ['a', 'p', 'p', 'l', 'e', None, None, None, None, None, None]
    cList = ['p', 'a', 'e', 'l', 'p', None, None, None, None, None, None] 
    print("Simple Hash Function Demonstration\n")
    print("Simple Hash Function: ", aList, hash(aList, 11))
    print("Simple Hash Function: ", bList, hash(bList, 11))    
    print("Simple Hash Function: ", cList, hash(cList, 11))    
    hash_table_demo()
    
main()
