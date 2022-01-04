
4.


def algebra():
    x = input("x: ")
    y = input("y: ")
    return (int(x)+int(y))*(int(x)+int(y))


print(algebra())


def word_list():
    return{}


1.
planets = ["venus", "mars", "pluto", "venus", "mars", "venus"]
d = input("planet1: ")
e = input("planet2: ")
f = input("planet3: ")
g = planets.count(d)
h = planets.count(e)
i = planets.count(f)
value = (g, h, i)
print(value)
word_list()


3.


def list_search():
    for i in range(4):
        c = input("colors1: ")
    for j in range(4):
        d = input("colors2: ")
    return c


print(list_search())


5.


def addition(a, b):
    sum = a+b
    return sum


result = addition(567, 3)
print(result)


def subtraction(h, j):
    difference = j-h
    return difference


answer = subtraction(23, 80)

print(answer)


def multiplication(f, r):
    product = f*r
    return product


res = multiplication(45, 11)


print(res)


def division(q, t):
    quotient = t/q
    return quotient


ans = division(23, 2323)

print(ans)
