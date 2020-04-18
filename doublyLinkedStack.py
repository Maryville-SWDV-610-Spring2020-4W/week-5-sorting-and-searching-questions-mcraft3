"""doublyLinkedStack.py"""

# ------------------------------------------------
"""Provides a doubly linked list stack.

   Provides a Last In / First Out LIFO Stack.
   Includes use of a class Node. Items are added
   and removed at the top of the stack. Provides
   for the dynamic allocation of data to avoid
   stack overflow error issues associated
   with when the size of the stack is restricted
   and the size of the stack exceeds the maximum
   size, throwing an error."""   
#-------------- class Node -----------------------
class Node: 
  
    #--------- Node constructor ------------------
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null         
    
#---------------- class Stack --------------------          
# Stack class contains a Node object 
class Stack:
    """LIFO Stack implementation using a doubly
       linked list for storage."""

    #----------- Stack constructor ---------------
    def __init__(self): 
        self.head = None
        
    #----------- Stack public accessors ----------
    # Function to return top element in the stack  
    def top(self): 
  
        return self.head.data 
  
    # Function to return the size of the stack  
    def size(self): 
   
        temp=self.head
        count=0
        if temp == None:
            return 0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
      
    # Function to check if stack is empty or not   
    def is_empty(self):
          
        if self.head is None: 
            return True
        else: 
            return False
                    
    #-------------- Stack methods ----------------
    # Function to add element data to top of stack  
    def push(self, data): 
  
        if self.head is None: 
            self.head = Node(data) 
        else: 
            new_node = Node(data)
            self.head.prev = new_node 
            new_node.next = self.head 
            new_node.prev = None
            self.head = new_node 
              
    # Function to pop top element off stack and
    # return element temp removed from the stack  
    def pop(self): 
  
        if self.head is None: 
            return None
        else: 
            temp = self.head.data 
            self.head = self.head.next
            return temp
        
    # Function to print the stack 
    def print_stack(self): 
          
        print("stack elements are:") 
        temp = self.head
        if temp == None:
            print("None")

        while temp is not None: 
            print(temp.data, end ="->") 
            temp = temp.next           

# ------------------------------------------------
