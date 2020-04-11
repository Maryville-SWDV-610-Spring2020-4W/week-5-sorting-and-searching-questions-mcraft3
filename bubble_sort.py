""" bubble_sort.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 5
Module 5.12 Sorting and Searching Questions.
PE 1.1: Bubble Sort

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
"""
Bubble Sort
The bubble sort makes multiple passes through a
list. It compares adjacent items and exchanges
those that are out of order. Each pass through the
list places the next largest value in its proper
place. In essence, each item “bubbles” up to the
location where it belongs.

Simultaneous Swap
The Bubble Sort can perform the exchange of the i
and (i+1)th items using the three–step procedure:
    
    # 3 way with temp assignment
    temp = alist[i]          
    alist[i] = alist[i+1]
    alist[i+1] = temp

or can be replaced utilizing the Python
simultaneous swap:

    # using simultaneous assignment
    alist[i], alist[i+1] = alist[i+1], alist[i]

bubble sort-sorts in O(n^2)
           -multiple passes of a list
           -pushes higher values up
           -may not make an exchange each pass
           -n-1 comparisons each pass + the swap
           - will make n-2 passes
"""
def bubbleSort(alist):
    # will make 9 comparisons for 10 indexes,
    # counts down 9,8,7, etc
    for passnum in range(len(alist) -1, 0, -1):
        
        # index of range one less than length
        # range 0 to 9, counts up 0,1,2,etc
        for i in range(passnum):
            
            # compares indexes (0,1), then (1,2)...
            # if left bigger, swap/exchange
            if alist[i] > alist[i + 1]:
            
                # 3 way with temp assignment
                #temp = alist[i]          
                #alist[i] = alist[i+1]
                #alist[i+1] = temp
                
                # using simultaneous assignment
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def test1():
    alist=[1,2,3,4,5,6,7,8,9,10]
    print("Bubble Sort\n")
    print("alist in sequential order: ", alist)
    #print()
    bubbleSort(alist)
    print("sorted: ", alist)
    
def test2():
    alist=[10,9,8,7,6,5,4,3,2,1]
    print("\nalist in reverse order: ", alist)    
    #print()
    bubbleSort(alist)
    print("sorted: ", alist)
    
def test3():
    alist=[10,1,8,3,6,4,5,7,2,9]
    print("\nalist in interleaved reverse/forward order: ", alist)
    #print()
    bubbleSort(alist)
    print("sorted: ", alist)

def test4():
    alist=[1,9,2,3,4,5,6,7,8,10]
    print("\nalist left short sort: ", alist)
    #print()
    bubbleSort(alist)
    print("sorted: ", alist)
    
def test5():
    alist=[1,3,4,5,6,7,8,9,2,10]
    print("\nalist right short sort: ", alist)
    #print()
    bubbleSort(alist)
    print("sorted: ", alist)
    
def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    
main()

