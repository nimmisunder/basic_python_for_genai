# Task 2: f-strings Practice
Productname= "Wireless Mouse"
Price= 29.99
Quantity= 5
Discountpercentage= 10
Totalbeforediscount = Price *Quantity
Discountamount =(Totalbeforediscount*Discountpercentage/100) 
Finaltotalafterdiscount = Totalbeforediscount -Discountamount

print("=" *60)
print("                 Receipt")

print(f"Product Name: {Productname}")
print(f"Unit price: {Price}")
print(f"Quantity: {Quantity}")
print(f"Subtotal: {Totalbeforediscount}")
print(f"Discountamount: {Discountamount:.2f}")
print(f"Total: {Finaltotalafterdiscount:.2f}")
print("=" *60)


