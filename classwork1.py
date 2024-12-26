def Average(A):
    _sum = 0
    for i in A:
        _sum += i
    return int(_sum/len(A))


def Factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

#Classwork 1 10/14/2024
A = [1,2,3,4,5,6,7,8,9]
print(Average(A))
print(Factorial(10))

#10/21/2024
def absolute_value(n):
    if n < 0:
        return -n
    return n


def find_roots():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"
    elif d == 0:
        return -b/(2*a)
    else:
        return (-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a)
    
print(absolute_value(-5))
print(find_roots())