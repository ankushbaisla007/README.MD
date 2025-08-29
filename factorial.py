n= int(input("Enter your number for factorical : "))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i 
    return fact
print(f"factorial of {n} is {factorial (n)} ")

