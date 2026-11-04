num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,155,18,19,20]
num=list(range(1,21))
even=[]
odd =[]
sum=0
product=1
for i in num:
    if i%2==0:
        even.append(i)
    if i%3==0:
        odd.append(i)
    sum+=i
    product*=i
print("All numbers:", num)
print("Even numbers:", even)
print("Numbers divisible by 3:", odd)
print("Sum of all numbers:", sum)   
print("Product of all numbers:", product)    