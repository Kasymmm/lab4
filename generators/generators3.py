#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def a(x):
    for i in range(x+1):
        if i%3==0 and i%4==0:
            yield i
b=int(input())
print(*a(b))