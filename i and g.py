def square_generator(N):
    for i in range(N + 1):
        yield i * i        
N = int(input())
for square in square_generator(N):
    print(square)


def even_number_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i            
n = int(input())
even_numbers = list(even_number_generator(n))
print(", ".join(map(str, even_numbers)))


def divisible_by_3_and_4_generators(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i           
n = int(input())
for number in divisible_by_3_and_4_generators(n):
    print(number) 


def squars(a, b):
    for i in range(a, b + 1):
        yield i * i       
a = int(input())
b = int(input())
for square in squars(a, b):
    print(square) 


def countdouwn(n):
    for i in range(n, -1, -1):
        yield i        
n = int(input())
for number in countdouwn(n):
    print(number) 