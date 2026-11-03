# Build a simple math calculator that:

# Takes two numbers from the user

# Performs and displays all arithmetic operations:

# Addition
# Subtraction
# Multiplication
# Division (regular)
# Floor division
# Modulo (remainder)
# Exponentiation
# Format the output clearly, showing the operation and result

print("="*40)
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))

add = num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
flor=num1//num2
mod=num1%num2
exp=num1**num2

print(f"{num1}+{num2}={add}")
print(f"{num1}-{num2}={sub}")
print(f"{num1}*{num2}={mul}")
print(f"{num1}/{num2}={div}")
print(f"{num1}//{num2}={flor}")
print(f"{num1}%{num2}={mod}")
print(f"{num1}**{num2}={exp}")
