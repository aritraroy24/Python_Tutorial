# LIST INDEXING

mylist = ["apple", "banana", "cherry", "man", "fruit",
          "ram", "shyam", "jadu", "madhu", "rohan"]
print(mylist[2])   # gives cherry as output
print(mylist.index("banana"))   # gives index of query (for first element element only if there is duplicate)
print(len(mylist))  # gives 10 as output



# # LIST SLICING

# Lst[Initial: End: IndexJump]
print(mylist[2:7]) # gives element from index 2 to index 6
print(mylist[::2])  # gives elment from start to end but giving one gap each
print(mylist[::-1]) # gives reverse list



# FOR LOOP  
for item in mylist:
    print(item)
a = 20
num = int(input("Enter a number- "))
for i in range(num):  # it runs for 0 to (num-1)
    a = a+5
    print(a)  # prints value of a in each iteration
for i in range(2, 5):  # it runs for 2 to 4
    a = a+5
print(a)  # print value of a after the completion of loop work



# ESCAPE SEQUENCES
print("\n")  # newline character
print("\t")   # gives horizontal tab