print(f"Welcome to User Info Collector!")

print(f"Please provide the following information:!")

f_name=input("First Name :")
l_name=input("Last Name :")
age =int(input("Age :"))
while True:
 if age>0:
  break
else:
  print("Invalid age! Please enter a positive number.")

birth = 2026-age
Email = input("Email :")
while True:
 if "@" in Email:
  break
 else:
  print("Enter a valid email")
Phone = input("Phone :")
City= input("City :")
Languagesnown = int(input("Number of programming languages you know :"))
Favoritel=input("favorite programming language :")
Experience=int(input("Years of coding experience :"))
Level = input("Are you currently a student? (yes/no) :")
Avg = Languagesnown/Experience
print(f"║        USER INFORMATION SUMMARY        ║")
print(f"Name : {f_name}{l_name}")
print(f"age : {age}'")
print(f"birth year : {birth}'")
print(f"Email : {Email}'")
print(f"Phone : {Phone}'")
print(f"City : {City}'")
print(f"Programming Experience:")
print(f"Languages Known : {Languagesnown}'")
print(f"Favorite Language : {Favoritel}'")
print(f"Years of Experience : {Experience}'")



if Experience > 0:
 print(f"Avg Languages/Year : {Avg:.2f}'")
 

if Experience <1:
 print(f"Experience Level :Beginner'")
elif Experience <= 3:
 print(f"Experience Level :Intermediate'") 
else:
 print(f"Experience Level :Advanced'")


print(f"Student Status : {Level}'")
print(f"║     Message: Keep up the great work!          ║")



