#Implement a generator called squares to yield the square of all numbers from (a) to (b). 
# Test it with a "for" loop and print each of the yielded values.

def sq(x,y):
    for i in range(x,y+1):
        yield i*1
x=int(input())
y=int(input())
print(*sq(x,y))