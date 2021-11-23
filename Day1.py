import random
print(random.randint(5, 50))  # gives random int value between 5 and 50

dic = ({1: [1, 2, 3], 2: [4, 5, 6], 3: "test", "test": "chem"}) 
print(dic[2])
print(type(dic))    #dictionary
lst = [2, 5.3, "a", {1: "a", 2: "b"}]
print(type(lst))    #list
tpl = (2, "hello")
print(type(tpl)) #tuple

n = int(input("Enter a number: "))
if n < 20:
    print("n is less than 20")
elif n == 20:
    print("n is eq to 20")
else:
    print("n is greater than 20")

a = float(input("Enter a number: "))
print(type(a))

a = "test"
b = "6546"
print(a+b)


"""
Task: Random Password Generator
=> gives random password made of 15 digits
    * small letter
    * capital letter
    * number
    * sign
=> hint:
    * 4 list of diff types
    * take random sequence and shuffle
    * add all those shuffled characters
    * print the result
"""


""""
BASIC GIT COMMANDS

*   git status
*   git add .  (to add all the files)
*   git commit -m ""  (to attach a msg to the commit)
*   git push  (push to GitHub)
"""