#Implement a generator that returns all numbers from (n) down to 0.

def a(x):
    while x>=0:
        yield x
        x-=1
x=int(input())
print(*a(x))