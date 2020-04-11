""" insertion_sort.py

SWDV-610-4W 20/SP2 DATA STRUCTURES WK 5
Module 5.12 Sorting and Searching Questions.
PE 1.3 Insertion Sort

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
Insertion Sort
The insertion sort, although still O(n^2), works
in a slightly different way. It always maintains
a sorted sublist in the lower positions of the
list. Each new item is then “inserted” back into
the previous sublist such that the sorted sublist
is one item larger. 

Insertion Sort runs at O(n^2). Max number of
comparison is sum n-1. Note a shift vs exchange
requires 1/3 processing since only one assignment
is performed, giving good perf in benchmark
studies."""

def insertionSort(alist):
    # will loop index 1 to 10)
    for index in range(1,len(alist)):
        
        # for test 1 sets value 2 (index 1) to currentvalue, and so on
        # for test 2 sets value 9 (index 1) to currentvalue, and so on
        currentvalue = alist[index]
        
        # sets index 1 (not value) to position
        position = index
        
        # for test 1 while 1>0 (True) and 1>2 (first pass)(False) skiploop
        # for test 2 1>0(True) and 10>9(True) enterloop
        while position>0 and alist[position-1]>currentvalue:
            
            # if all True, for test 2 shifts 10 to index 1
            alist[position]=alist[position-1]
            
            # for test 2 updates position to index 0
            position = position-1

        # udpates position to current value (shift)
        # for test 2 would set 9 to index 0
        alist[position]=currentvalue

def test1():
    alist=[1,2,3,4,5,6,7,8,9,10]
    print("Insertion Sort\n")
    print("alist in sequential order: ", alist)
    #print()
    insertionSort(alist)
    print("sorted: ", alist)
    
def test2():
    alist=[10,9,8,7,6,5,4,3,2,1]
    print("\nalist in reverse order: ", alist)    
    #print()
    insertionSort(alist)
    print("sorted: ", alist)
    
def test3():
    alist=[10,1,8,3,6,4,5,7,2,9]
    print("\nalist in interleaved reverse/forward order: ", alist)
    #print()
    insertionSort(alist)
    print("sorted: ", alist)

def test4():
    alist=[1,9,2,3,4,5,6,7,8,10]
    print("\nalist left short sort: ", alist)
    #print()
    insertionSort(alist)
    print("sorted: ", alist)
    
def test5():
    alist=[1,3,4,5,6,7,8,9,2,10]
    print("\nalist right short sort: ", alist)
    #print()
    insertionSort(alist)
    print("sorted: ", alist)
    
def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    
main()

