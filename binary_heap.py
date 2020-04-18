# binary_heap.py

"""
SWDV-610-4W 20/SP2 DATA STRUCTURES WK 6
Module 6.11 Forest for the Trees.

This file addresses: PE 1 and PE 2
1. Generate a random list of integers.
Show the binary heap tree resulting from
inserting the integers on the list one at a
time.
      
2. Using the list from the previous question,
show the binary search tree resulting from
the list as a parameter to the buildHeap
method. Show both the tree and list form.

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft"""
# ------------------------------------------------
"""
Specified Requirements from Canvas:

   1. Generate a random list of integers.
      Show the binary heap tree resulting from
      inserting the integers on the list one at a
      time.
      
   2. Using the list from the previous question,
      show the binary search tree resulting from
      the list as a parameter to the buildHeap
      method.
      Show both the tree and list form.
      
   3. (optional bonus question) Extend the
      buildParseTree function to handle
      mathematical expressions that do not have
      spaces between every character.
      
   4. (optional bonus question) Extend the
      buildParseTree and evaluate functions to
      handle boolean statements. Remember that
      "not" is a unary operator, so this will
      complicate your code somewhat.

Please appropriately name your files to reflect
which question they answer.

In addition to coding these tasks, you must post a
video running and explaining your code.  This
allows for you to demonstrate what is occurring in
the code as it is happening and how it is
organized.  You must also run your code in the
video to explain the output and why the program
produced that output.
"""
# ------------------------------------------------
"""GitHub Submission Instructions:
Once you complete these exercises, be sure you
have committed your solutions locally and pushed
them up to the remote repository. If you are
unsure how to clone the repository for this
assignment, please review Pull and Push for
Assignments.

GitHub Link:
https://classroom.github.com/a/FZrZZ3AK"""
# ------------------------------------------------
"""Canvas Submission Instructions:

When you have completed this assignment and pushed
your work to the remote GitHub repository, answer
the following question(s):

    How many hours do you estimate you used
    completing this assignment?
    
    What was easiest for you when completing this
    assignment?
    
    What was the most difficult challenge you
    experienced when completing this assignment?

To begin, click the Submit Assignment button in
Canvas and respond in the available text entry
box."""
# ------------------------------------------------
"""Tree Search Rubric

1. Generate list of integers.

2. Binary Heap Tree Readability - Code is readable
   and well organized.

3. Binary Tree Output - Output shows binary heap
   tree from inserting integers one at a time.

4. buildHeap method Use - Uses the buildHeap
   method properly.

5. Part 2 Output - Proper output is produced from
   using the buildHeap method.
   
6. Answer all canvas questions.

7. Video Submission - Clearly explains the
   organization and out put of the program.
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
   experienced when completing this assignment?
"""
# ------------------------------------------------

from random import randrange
"""
Binary Heap (Implementation of a Priority Queue).

BinHeap acts like a priority queue, or a queue in
that you dequeue an item by removing it from the
front. However, in a priority queue the logical
order of items inside a queue is determined by
their priority. The highest priority items are
at the front of the queue and the lowest priority
items are at the back. Thus when you enqueue an
item on a priority queue, the new item may move
all the way to the front."""

"""This heap takes key value pairs,
we will assume that the keys are integers

min heap - smalles key is always at the front
max heap - largest key is always at the front.

This is a min heap.

With the binary heap when you diagram the heap
it looks a lot like a tree, but when you
implement it you use only a single list as an
internal representation.

Heap Order Property: In a heap, for every node x
with parent p, the key in p is smaller than or
equal to the key in x.

               5 
             /   \
            /     \
           9       11
         /  \       /\
       14    18   19  21
       /\    / 
     33 17  27

Heap Order:
0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27
List Index:
0, 1, 2,  3,  4,  5,  6,  7,  8,  9, 10, 11
""" 
# ------------------------------------------------
"""
Accessors and methods fo the BinHeap Class:

BinHeap() creates a new, empty, binary heap.

percUp(i)# After an insert(), it will call percUp
which is used to reset the Heap Structure
Property. It will Compare newly added item with
its parent. If the newly added item is less than
its parent, it swaps the item with its parent.
This may involve a series of swaps needed to
percolate the newly added item up to its proper
position in the tree.

percDown(i) Helper for buildHeap, percs bigger
items down list. Will perc down 1 at a time.
BuildHeap will iterate entire list and call
perdDown on each to reset Heap Order Property.
PercDown calls minChild as helper to calc for
PercDown where to  swap current with its
smallest child.

minChild(i) Helper method for percDown; calcs
min Child to tell percDown where to swap
current during percDown, to reset Heap Order
Property.

insert(k) adds a new item to the heap.

findMin() returns the item with the minimum key
value, leaving item in the heap.

delMin() returns the item with the minimum key
value, removing the item from the heap. Notice
that no matter the order that we add tems to the
heap, the smallest is removed each time.

isEmpty() returns true if the heap is empty,
false otherwise.

size() returns the number of items in the heap.

buildHeap(alist) builds a new heap from a list of
keys.
"""
# ------------------------------------------------
class BinHeap:
    
    #--------class constructor--------------------
    def __init__(self):
        self.heapList = [0]  # initialize
        self.currentSize = 0 # initialize

    #--------class accessors---------------------
    def size(self):
        return self.currentSize
    
    # root or min is at index 1
    def findMin(self):
        return self.heapList[1]
    
    # boolean call is heap empty?
    def isEmpty(self): 
        if currentSize == 0:
            return True
        else:
            return False
        
    #--------class methods------------------------
    # Helper for insert method for single item.
    # Regain Heap Structure Property.
    # Compare newly added item with its parent.
    def percUp(self,i): 
        
        # calc parent of any node by using integer
        # div by 2
        while i // 2 > 0: 
            
            # calc parent of any node by integer
            # div by 2         
            if self.heapList[i] < \
               self.heapList[i // 2]:
                
                # set calc to temp var
                tmp = self.heapList[i // 2]
                
                # set/swap parent with its
                # smallest child less than parent
                self.heapList[i // 2] = \
                                self.heapList[i]
                
                # set current to parent 
                self.heapList[i] = tmp
                
            # iterate to compare/swap next parent    
            i = i // 2 
      
    # append to end of list, then reset Heap
    # Structure Property with percUp.
    def insert(self,k): 
        self.heapList.append(k) # appends to end
        
        # increment size 
        self.currentSize = self.currentSize + 1
        
        # calls percUp end item
        self.percUp(self.currentSize) 
       
    # helper for buildHeap, percs bigger items
    # down. BuildHeap will iterate list and call
    # percdown 1 at a time. Resets Heap Order
    # Property. 
    def percDown(self,i): 
        while (i * 2) <= self.currentSize:
            
            # Helper to find smallest to swap
            # current with its smallest child
            mc = self.minChild(i)
            
            # if current greater than minChild
            if self.heapList[i] > \
               self.heapList[mc]:
                
                # backup current to temp var
                tmp = self.heapList[i]
                
                # swap minChild to currrent slot 
                self.heapList[i] = \
                                 self.heapList[mc]
                
                # swap current backup into
                # minChild slot
                self.heapList[mc] = tmp
                
            # set minChild to current    
            i = mc
 
    # Helper method for percDown; calcs min Child
    # to tell where to swap current during
    # percDown.
    def minChild(self,i): # sample for new root
        # if 1 * 2 + 1=3 >list size:
        if i * 2 + 1 > self.currentSize:
            
            #min is slot 2
            return i * 2
        
        else:
            # if val(1*2) < val(1*2+1)
            if self.heapList[i*2] < \
               self.heapList[i*2+1]:
                
                # min is slot 2
                return i * 2
            
            else:
                # min is slot 3
                return i * 2 + 1     

    # Must reset Heap Order Property after delete
    # of Root, 2 steps.
    def delMin(self):
        # sets root to var to return as removed
        retval = self.heapList[1]
        
        # 1. take last item in list and make it
        # root (moving last maintains heap
        # structure property).
        self.heapList[1] = self.heapList\
                           [self.currentSize]
        
        self.heapList.pop() # pop root (remove)
        
        # decrement size
        self.currentSize = self.currentSize - 1
        
        # push new root down tree to proper
        # position, resetting heap order property.
        self.percDown(1) 
        return retval # return removed root

    # Builds an entire heap from a list. 
    def buildHeap(self,alist):
        
        # start in middle of tree, and work back
        # to root.
        i = len(alist) // 2
        
       # set size to len of list 
        self.currentSize = len(alist)
        
        # adds 0 to index 0(left end of list)
        self.heapList = [0] + alist[:]
        
        # ensure largest child  (greater than
        # index 0) is moved down the tree
        while (i > 0): 
            
           # percDown moves it down the tree, swap
           # with current. 
            self.percDown(i)
            
            # work back towards root, perdown next
            # slot or index
            i = i - 1 
            
# ------------------------------------------------
def main():
    print("BinHeap Demo 1:\n")
    print("Generate a randomList to demo manual insertion")
    print("of each integer one at a time:\n")
    randomList1 = []
    for i in range(5):
        i = randrange(1, 100)
        randomList1.append(i)
    print("randomList1:", randomList1)

    bh = BinHeap()

    bh.insert(randomList1[0])
    bh.insert(randomList1[1])
    bh.insert(randomList1[2])
    bh.insert(randomList1[3])
    bh.insert(randomList1[4])

    print("\nheapList bh from inserting 1 at a time:")
    print(bh.heapList)
    print("BinHeap size:", bh.size())
    print("BinHeap Min Key:", bh.findMin())
    print()

# ------------------------------------------------
    print("binHeap Demo 2:\n")
    print("Generate a random list to insert into binHeap:\n")
    randomList2= []
    for i in range(5):
        i = randrange(1, 100)
        randomList2.append(i)

    print("randomList2:", randomList2)
    print()

    bh = BinHeap()
    print("Tree structure prior to buildHeap:")
    print("#           ", randomList2[0], "    ") 
    print("#           / \   ")
    print("#         ", randomList2[1], " ", randomList2[2] )
    print("#         / \     ")
    print("#      ", randomList2[3], " ", randomList2[4] )
    print()

    bh.buildHeap(randomList2)

    print("BinHeap bh after buildHeap")
    print("with RandomList as parameter:")
    print(bh.heapList)
    print()

    print("Tree structure after buildHeap:")
    print("#           ", bh.heapList[1], "    ") 
    print("#           / \   ")
    print("#         ", bh.heapList[2], " ", bh.heapList[3]  )
    print("#         / \     ")
    print("#      ", bh.heapList[4], " ", bh.heapList[5] )
    print()

    print("BinHeap size:", bh.size())
    print("BinHeap Min Key:", bh.findMin())

main()

