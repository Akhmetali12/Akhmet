#exm1
print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

#exm2
if 5 > 2:
print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")

#exm3
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#exm4
x = 5
y = "John"
print(x)
print(y)

x = "Sally"
y = 'John'
print(x)
print(y)

#exm5
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

#exm6
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#exm7
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#exm8
x = 5
y = "John"
print(x + y)

#exm9
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print("Python is " + x)

#exm10
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#exm11
a = 5
print(type(a))

b = "Hello World"
print(type(b))

c = 20.5
print(type(c))

#exm12
x = 1
y = 2.8 
z = 1j 

print(type(x))
print(type(y))
print(type(z))

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#exm13
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

A = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(A)

#exm14
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

#exm15
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

#exm16
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

#exm17
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip()) # returns "Hello, World!"

#exm18
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

#exm19
a = "Hello"
b = "World"
print(a + b)
print(a + " " + b)

#exm20
age = 36
txt = f"My name is John, I am  {age}"
print(txt)

#exm21
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#exm22
txt = "We are the so-called \"Vikings\" from the north."
