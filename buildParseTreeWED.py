# buildParseTreeWED.py
"""
SWDV-610-4W 20/SP2 DATA STRUCTURES WK 6
Module 6.11 Forest for the Trees.

This file addresses: PE 3
3.Extend the buildParseTree function to handle
mathematical expressions that do not have
spaces between every character. Submitted with
this file are the files binaryTree.py and
doublyLinkedStack.py that are both required
and imported by buildParseTree.py.

Maryville University of St. Louis, MO
John E. Simon School of Business
Professor Timothy Kyle
Student Mike Craft"""
# ------------------------------------------------
"""Specified Requirements from Canvas:

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
# Required to run the Parse Tree, both Stack
# and BinaryTree.
from doublyLinkedStack import Stack
from binaryTreeWED import BinaryTree

"""This module extends the buildParseTree function
to handle mathematical expressions that do not
have spaces between every character.

This update, annotated with filename
buildParseTreeWED.py requires use of two modules,
the matching updated binaryTreeWED.py, and the
non updated doublyLinkedStack.py. Together the two
undated files provide a With Error Detection
capability to provide a low level expression error
detection capability for items such as redundant
parenthesis or other errors that make an expression
not proper or incorrect.

This updated buildParseTreeWED.py will
generate a helper file to the same
directory or folder these files are in called
errorDetection.txt that is a temp or buffer
that will overwrite each run. You do not need
it to start, it will create and update as
needed.

buildParseTree:
Utilizes a stack to keep track of current node and
parent of the current node. Whenever you descend to
a child of the current node, first push the current
node on the stack. When you return to the parent of
the current node, pop the parent off the stack"""

def buildParseTree(fpexp):
    # import string, split and make list
    fplist = fpexp.split()  
    pStack = Stack()        # initialize stack
    eTree = BinaryTree('')  # initialize Tree
    pStack.push(eTree)      # push to stack
    currentTree = eTree     # make current tree
# ------------------------------------------------
    for i in fplist:
        """ To build a parse tree, break up the
        expression string into a list of tokens.
        There are four different kinds of tokens
        to consider: left parentheses, right
        parentheses, operators, and operands.
        If a '(' create new tree, if a ')' we have
        finished an expression. Operands = leaf nodes
        and children of their operators. Operators
        have both L and R child."""
        
        """Four if/elif statements code these rules:
# ------------------------------------------------
        1. If the current token is a '(', add a new node
        as the left child of the current node, push
        current node on stack, and descend to the left
        child (make current node this new child)."""
        if i == '(':
            
            currentTree.insertLeft('') # create new node as left child
            pStack.push(currentTree)   # add to stack
            currentTree = currentTree.getLeftChild() # make current this new child
        
            """2. If the current token is in the list
            ['+','-','/','*'], set the root value of the
            current node to the operator represented by
            the current token. Add a new node as the
            right child of the current node, push current
            node on stack, and descend to the right child
            (make current node this new child)."""
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i) # set root value of current
            currentTree.insertRight('') #  add new node right child
            pStack.push(currentTree)    # add to stack
            currentTree = currentTree.getRightChild() # set new right child as current
# ------------------------------------------------            
            """3. If the current token is a ')', pop the
            parent off the stack, and go to the parent
            of the current node."""
        elif i == ')':
            currentTree = pStack.pop() # remove from stack
# ------------------------------------------------            
            """4. If the current token is a number,
            (not an operator), set the root value of the
            current node to the number, pop the parent off
            the stack, and return to the parent (make
            current node the parent)."""        
        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i)) # set root of current to i 
                parent = pStack.pop()  # remove from stack
                currentTree = parent   # make parent current

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

# ------------------------------------------------
def expressionConverter():
    print("""
    This module extends the buildParseTree function
    to handle mathematical expressions that do not
    have spaces between every character.""")

    # starting expression with no spaces
    #myExpressionNoSpaces = "((15+10)*6)"     # proper expression
    #myExpressionNoSpaces = "(((15+10))*6)"  # extra inner parenthesis
    #myExpressionNoSpaces = "((24+(20*4)))"  # extra out parenthesis
    myExpressionNoSpaces = "(24+(20*4))"    # proper expression alternate

    print("\nExpression with no spaces:", myExpressionNoSpaces)
    print()

    # convert to string
    myExpressionNoSpacesString = str(myExpressionNoSpaces)

    # initialize new spaced string to empty
    myExpressionStringSpaced = ""

    # loop through unspacced string
    for i in range(len(myExpressionNoSpacesString)):
        # case 1
        if myExpressionNoSpacesString[i] == '(': 
            # concatenate empty spaced string
            # with index from unspaced string
            # and with a space " "
            # loop to complete entire string
            myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i] + " "
        # case 2
        elif myExpressionNoSpacesString[i] in ['+', '-', '*', '/']:
            h = i - 1
            
            if myExpressionNoSpacesString[h] == ")":
                myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i] + " "
            
            elif myExpressionNoSpacesString[h] not in ['+', '-', '*', '/']: # its a number 0-9
                myExpressionStringSpaced = myExpressionStringSpaced + " " + myExpressionNoSpacesString[i] + " "
                
            else:
                myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i] + " "
        # case 3
        elif myExpressionNoSpacesString[i] not in ['+', '-', '*', '/', ')']: # its a number 0-9
            
            try:
                myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i]
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))    
        # case 4
        elif myExpressionNoSpacesString[i] == ')':        
            h = i - 1
            
            if myExpressionNoSpacesString[h] == ")":
                myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i] + " "
            
            elif myExpressionNoSpacesString[h] not in ['+', '-', '*', '/']: # its number 0-9  
                myExpressionStringSpaced = myExpressionStringSpaced + " " + myExpressionNoSpacesString[i] + " "
                
            else:
                myExpressionStringSpaced = myExpressionStringSpaced + myExpressionNoSpacesString[i] + " "

    myExpressionStringSpaced = myExpressionStringSpaced.rstrip()

    return myExpressionStringSpaced # return output
    
# ------------------------------------------------
def main():
    myExpressionStringSpaced = expressionConverter()
    
    print("Expression after conversion and now spaced:", myExpressionStringSpaced)
    print("\nCreating Parse Tree with MyExpressionStringSpaced as a parameter.")
    # Create an empty tree.
    pt = buildParseTree(myExpressionStringSpaced)
    #pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    
    print("\nPost Order Traversal:")
    pt.postorder()  # post order traversal to print ints and operators
    
    #print("\nEvaluation of Expression in Parse Tree is: ", evaluate(pt))
    print("\nEvaluation of Expression in Parse Tree is: ", pt.postordereval())

    # print converted expression
    print("\nExpression extracted from Parse Tree (and reassembled with parenthesis)")
    print("using printexp method of binaryTree:    " ,end=" ")
    pt.printexp()
    print()

#----start With Error Detection updated code------
    # make printexp print to file and write and append, and close then read and strip.
    # compare to input with below and should pass comparison or fail comparison at that point.
    outfile = open("errorDetection.txt", "w")
    pt.printexpWED(outfile)
    outfile.close()
    
    # open the file
    infile = open( "errorDetection.txt", 'r' )
    expression = infile.read()
    print("\nExpression extracted from Parse Tree (and reassembled with parenthesis)")
    print("using printexpWED method of binaryTree: " ,end=" ")
    expression = expression.rstrip()
    print(expression)
    
    if expression != myExpressionStringSpaced:
        print("\n\nError:  An extra set of parenthesis or other error has been detected in ")
        print("the Expression that is in ParseTree.")
        
        print("\nExpression entered into ParseTree:    ", myExpressionStringSpaced)
        print("Expression extracted with printexpWED:", expression)
        
        print("\nCompare the entered to extracted. The input expression requires removal of") 
        print("the redundant parenthesis or other error to make it a proper expression that")
        print("can be properly processed, traversed, evaluated and output.")
        
main()
    