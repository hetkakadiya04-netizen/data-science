# Program to find Greatest Common Divisor of two numbers. For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print("The Greatest Common Divisor of", num1, "and", num2, "is:", result)
