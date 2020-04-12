# week-5-sorting-and-searching-questions-mcraft3
week-5-sorting-and-searching-questions-mcraft3 created by GitHub Classroom
Sat 2020 EST.
Lots of cleanup.
Class HashTable PyDoc comment: 
Updated Put to include check for auto resize of HashTable.
Updated to specify parameters for methods delete key value pair, key in dict, hash function, rehash and resize. cleaned up all methods that was passing len(self.slots) to not pass it to simplify all calls and make use of that call in hash function and once in rehash.  cleaned up some lazy assignments as size to be self.size to keep consistent. significant change in put moved the check for resize to start of method (above the call to hashfunction) so hash function is now below it. Put now completes the resize or skip before the hash function call, which is a cleaner separation of subroutines, and then a clean step into following if loop.  updated the hashTable Demo to clearly show that the resize happens after put key value pair 6 is complete, and during the start of put for key value pair seven, so before key value pair 7 is loaded. Updated the hashtable demo to force after resize to still include the rehash function, so instead of using key 31 for cow using key 32 and instead of key 55 using key 35 so you see to rehashes to show that function is working. Updated simple hash function to show table of 11 slots, with remainder filled with None's and updated algorithm to skip the Nones so use of 11 for hash is correct for size of the list.


Sat 1256 EST. 

@mcraft3
mcraft3 Week 5 submissions

Here are the files. I have 4 videos and am having a hardware failure for the video card 
so it will no longer capture the screen and make videos. I have 3 done and hash table no 
video and may need a new computer or a repair. I will load the .py files and3 videos to 
canvas and if I can get an alternative computer timely make the last video. Mike
