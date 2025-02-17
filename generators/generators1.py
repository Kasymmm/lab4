#Create a generator that generates the squares of numbers up to some number N.

def sq(a):
    for i in range(a+1):
        yield i*i
x=int(input())
print(*sq(x))