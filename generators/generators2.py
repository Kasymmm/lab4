#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def a(x):
    for i in range(x+1):
        if i%2==0:
            yield i
b=int(input())
print(*a(b))