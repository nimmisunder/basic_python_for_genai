# Task 4: Truthy and Falsy Values
# Create a script that tests various values to determine if they're truthy or falsy:

# Test these values:

# 0
# 1
# "" (empty string)
# "hello"
# [] (empty list)
# [1, 2, 3]
# None
# True
# False
# "False" (the string, not the boolean)
# For each value, print:

# The value itself
# Whether it's truthy or falsy
# A brief explanation
# Format your output in a table-like structure using f-strings.


values = [(0,"zero"),(1,"true"),("" ,"empty string"),("hello","string"),([],"empty list"),([1, 2, 3],"list"),(None,"no value"),
          (True,"True value"),(False,"False value"),("False","the string, not the boolean")]
print(values)

print("="* 80)
print(f"{'value':<15}{'result':<15}{'desc':<15}")
print("="* 80)
for value,desc in values:
    result = True if bool(value) else False
    print(f"{str(value):<18}{result:<16}{desc}")
print("="* 80)
