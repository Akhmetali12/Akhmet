#ex1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ex2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#ex3
x = "Hello"
y = 15
z = ["apple", 2, "cherry"]
print(bool(x), bool(y), bool(z))
a = False
b = None
c = 0
d = ""
e = []
f = ()
g = {}
print(bool(a), bool(b), bool(c), bool(d), bool(e), bool(f), bool(g))

#ex4
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

#ex5
x = 200
print(isinstance(x, int))

#ex6
x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x**y)
print(x // y)

#ex7
x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x**y)
print(x // y)

#ex8
x = 6

if x > 5 and x < 10:
    print("YES")

if x > 5 or x > 10:
    print("NO")

if not(x > 5 and x < 10):
    print("YES")
else:
    print("NO")

#ex9
x = 10
y = 10

if x is y:
    print("True")

x = 5

if x is not y:
    print("False")

#ex10
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

thislist = list(("apple", "cherry", "banana"))
print(thislist)

#ex11
thislist = ["apple", "cherry", "banana"]
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#ex12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex13
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

thislist.remove("orange")
print(thislist)

thislist.pop(1)
print(thislist)

#ex14
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ex15
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ex16
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) 

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#ex17
thislist = ["apple", "banana", "cherry"]

mylist = thislist.copy()
print(mylist)

itslist = list(thislist)
print(itslist)

#ex18
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list1.extend(list2)
print(list1)

#ex19
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

print(thistuple[1])
print(thistuple[2:5])
print(thistuple[-4:-1])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#ex20
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
y.remove("apple")
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#ex21
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#ex22
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

for i in range(len(thistuple)):
  print(thistuple[i])

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#ex23
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#24
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(len(thisset))

#25
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)
print("banana" not in thisset)

#26
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.remove("banana")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#27
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#28
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.intersection(set5)
print(set6)

set7 = {"apple", "banana", "cherry"}
set8 = {"google", "microsoft", "apple"}
set9 = set7.difference(set8)
print(set9)

set10 = {"apple", "banana", "cherry"}
set11 = {"google", "microsoft", "apple"}
set12 = set10.symmetric_difference(set11)
print(set12)

#29
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(thisdict.get("model"))

thisdict["color"] = "white"
print(thisdict)

print(thisdict.values())
print(thisdict.keys())
print(thisdict.items())

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#30
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

thisdict.pop("model")
print(thisdict)

for x in thisdict:
  print(x)

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)
  
#31
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

#32
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#33
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#34
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#35
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)