
Python Learning -- Day 2
1. Lists
A list stores multiple values in one variable.
numbers = [10, 20, 30, 40, 50]
Create an empty list and add items
shopping_list = []

while True:
    item = input("Enter an item (or type done to finish): ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("Shopping list:", shopping_list)
Useful list methods:

  Method                   Purpose
  append(value)          Adds an item to the end
insert(index, value)   Adds an item at a position
remove(value)          Removes the first matching item
pop()                  Removes and returns the last item
sort()                 Sorts the original list
reverse()              Reverses the original list
clear()                Removes all items
sort() vs sorted()
numbers = [40, 10, 30, 20]

numbers.sort()                 # Changes the original list
new_list = sorted(numbers)     # Returns a new sorted list
descending = sorted(numbers, reverse=True)
Remember: list.sort() returns None. Do not write
new_list = numbers.sort().
2. Dictionaries
A dictionary stores information as key-value pairs.
book = {
    "title": "Wings of Fire",
    "author": "A. P. J. Abdul Kalam",
    "year": 1999,
    "pages": 180,
    "rating": 4.5
}
Access a value:
print(book["title"])
print(book["rating"])
Update a value:
book["rating"] = 5.0
Add a new key:
book["genre"] = "Autobiography"
Check whether a key exists:
if "publisher" not in book:
    book["publisher"] = "ABC Publications"
Remove a key:
book.pop("year", None)
The default None prevents an error if the key is missing.
Loop through a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

# Keys
for key in student:
    print(key)

# Keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Values only
for value in student.values():
    print(value)
  Expression           Gives you
  student            Keys
student.keys()     Keys
student.values()   Values
student.items()    Key-value pairs

Use the correct data type: store years and page counts as integers, and
ratings as numbers rather than strings.
3. for Loops and range()
A for loop repeats code for each item in a sequence.
for number in range(1, 6):
    print(number)
range(start, stop, step) excludes the stop value.

Count backwards:
for number in range(10, 0, -1):
    print(number)
Count backwards by two:
for number in range(20, 0, -2):
    print(number)
Create a list of numbers from 1 to 20:
numbers = list(range(1, 21))
4. Modulo Operator %
The modulo operator returns the remainder after division.
print(10 % 2)  # 0
print(7 % 2)   # 1
Check even numbers:
if number % 2 == 0:
    print("Even")
Check numbers divisible by 3:
if number % 3 == 0:
    print("Divisible by 3")
Check numbers divisible by both 2 and 3:
if number % 2 == 0 and number % 3 == 0:
    print(number)
5. Calculate a Sum and Product with a Loop
Sum
numbers = list(range(1, 6))
total = 0

for number in numbers:
    total += number

print("Sum:", total)  # 15
Product
numbers = list(range(1, 6))
product = 1

for number in numbers:
    product *= number

print("Product:", product)  # 120
Important: Start a sum at 0, but start a product at 1. Starting
a product at zero would make the result zero.
6. enumerate()
enumerate() gives both the index and the value while looping.
fruits = ["Apple", "Mango", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
Start counting from 1:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
Use enumerate() when you need both an item's position and its value.
7. Get Five Numbers from the User
numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Numbers:", numbers)
input() returns text, so int() converts the entered value to an
integer.
8. Find Maximum, Minimum, and Average Using a Loop
numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

maximum = numbers[0]
minimum = numbers[0]
total = 0

for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

    total += number

average = total / len(numbers)

print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
Why initialize maximum and minimum with numbers[0]? The first item
gives us a real value to compare with the remaining items.

Average = total of all values divided by the number of values.
