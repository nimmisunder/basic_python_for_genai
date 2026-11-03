# Write a program that:

# Asks the user for their age

# Asks if they have a driver's license (yes/no)

# Uses comparison and logical operators to determine:

# Can they drive? (age >= 18 AND has license)
# Are they a senior? (age >= 65)
# Are they a teenager? (age >= 13 AND age < 20)
# Can they vote? (age >= 18)
# Display the results in a clear format

Age = input("Age please: ")
license_input = input("Do you have a driver's license? (yes/no): ").lower()
can_drive= Age>=18 and license_input =='yes'
print(f"Can they drive?  {can_drive}")
print(f"Are they a senior?  {senior}")
print(f"Are they a teenager?  {teenager}")
print(f"Can they vote?  {vote}")
