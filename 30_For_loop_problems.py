# Check whether a number is positive, negative, or zero.
num=int(input("Enter a number: "))
if num==0:
    print("ZERO")
elif num>0:
    print("Positive")
else:
    print("Negative ")

# Take a number and check if it is even or odd.
def even_odd(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"
num=int(input("Enter a number to check even or odd :"))
print(even_odd(num))
# Check whether a person is eligible to vote (age ≥ 18).
age=int(input("Enter your age: "))
if age>=18:
    print("Your are eligible")
else:
    print("Not eligible for Vote")
# Take two numbers and print the greater number.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number"))
if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("Both numbers are equal")
# Check whether a number is divisible by 5 or not.
num=int(input("Enter a number: "))
if num%5==0:
    print(f"{num} is divisable by 5")
else:
    print(f"{num} is not divisable by 5")

# # Take a number and check if it is a multiple of 3; otherwise print “Not multiple of 3”.
num=int(input("Enter a number"))
if num%3==0:
    print(f"{num} is Multiple of 3")
else:
    print(f"{num} is Not multiple of 3")
# Check whether a character is a vowel or consonant.
ch = input("Enter a character: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
# Take a number and check if it is greater than 100 or not.
num=int(input("Enter a number: "))
if num>100:
    print("Greater than 100")
else:
    print("Not greater than 100")
# Check whether a year is a leap year or not.
year=int(input("Enter a year : "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")
# Take temperature input and print “Hot” or “Cold” based on value (>30 hot).
temp=float(input("Enter Temperature: "))
if temp>30:
    print("Hot")
else:
    print("Cool")
# Take marks and print grade: A (90+), B (75–89), C (50–74), Fail (<50).
marks=int(input("Enter Your marks: "))
if marks<0 or marks>100:
    print("IVALID MARKS")
elif marks>=90:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade C")
else:
    print("Fail")
# Create a simple calculator using two numbers and an operator (+, -, *, /).
num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
operator=input("Enetr '+' addition ,'-' substraction ,'*' Multification ,'/' Division \n" )
if operator=='+':
    print(f"Addition of two numbers {num1}+{num2} ={num1+num2}")
elif operator=='-':
    print(f"Substraction of two numbers {num1}-{num2} ={num1-num2}")
elif operator=='*':
    print(f"Multification of two numbers {num1}*{num2} ={num1*num2}")
else:
    print(f"Division of two numbers {num1}/{num2} ={num1/num2}")
# Take a number and print: “FizzBuzz” (divisible by 3 & 5), “Fizz” (only 3), “Buzz” (only 5), otherwise print number.
num=int(input("Enter a number : "))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)
# Check whether a character is uppercase, lowercase, digit, or special character.
ch=input("Enter a character : ")
if ch.isupper():
    print("uppercase")
elif ch.islower():
    print("lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
# Take salary and assign tax percentage: No tax (<2.5L), 5% (2.5L–5L), 20% (5L–10L), 30% (>10L).
salary=int(input("Enter your salary: "))
if salary<250000:
    print("NO Tax")
elif salary>=250001 and salary<=500000:
    print("Tax is ",salary*0.05)
elif salary>=500001 and salary<=1000000:
    print("Tax is ",salary*0.20)
else:
    print("Tax is ",salary*0.30)

# Find the largest of three numbers using nested if.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2:
    if num1>num3:
        print(f"{num1} is largest number")
    else:
        print(f"{num3} is legerst nnumber")
else:
    if num2>num3:
        print(f"{num2} is lergest number")
    else:
        print(f"{num3} is leargest number ")


# Take username and password and check login success or failure.
user_name=input("Enter user name").lower()
password=input("Enter password: ")
if user_name=='madhu' and password=='Madhu143@':
    print("login Success")
else:
    print("Login Failure")
# # Check whether a number is positive; if yes, then check even or odd.
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

elif num == 0:
    print("Zero")

else:
    print("Negative")
# ATM withdrawal system: check balance, then withdrawal limit, then allow/deny transaction.
# Input balance and withdrawal amount
balance = float(input("Enter your account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
# # Nested if
if balance > 0:
    if withdraw <= balance:
        if withdraw <= 10000:   # Daily withdrawal limit
            balance = balance - withdraw
            print("Transaction Successful!")
            print("Amount Withdrawn:", withdraw)
            print("Remaining Balance:", balance)
        else:
            print("Transaction Denied! Withdrawal limit is ₹10,000.")
    else:
        print("Transaction Denied! Insufficient balance.")
else:
    print("Invalid account balance.")
# Check student result: If marks ≥ 35 → Pass; inside pass check Distinction (≥75) or First Class (≥60).
marks = int(input("Enter student marks: "))
if marks >= 35:
    print("Result: Pass")

    if marks >= 75:
        print("Grade: Distinction")
    elif marks >= 60:
        print("Grade: First Class")
    else:
        print("Grade: Second Class")
else:
    print("Result: Fail")
# Check whether a number is a 3-digit number or not.
num=int(int("Enter a number : "))
if num>=100 and num<=999:
    print(f"{num} is Three digit Number")
else:
    print(f"{num} is Not Three digit Number")

# Take three angles and check if they form a valid triangle.
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
# Find the second largest among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Second largest number is:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second largest number is:", b)
else:
    print("Second largest number is:", c)

# Check whether a character is an alphabet or not (without using built-in functions).
ch=input("Enter a Character : ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(f"{ch} is Alphabet")
else:
    print(f"{ch} is not Alphabet")
# Calculate electricity bill based on units: First 100 free, next 100 ₹5/unit, above 200 ₹10/unit.
units=int(input("Enter units : "))
total=0
if units <= 100:
    total = 0

elif units <= 200:
    total = (units - 100) * 5

else:
    total = 100 * 5 + (units - 200) * 10

print(total)

# Movie ticket pricing based on age: Child (<12), Adult, Senior (>60).
age=int(input("Enter Your age to book Movie ticket : "))
if age<12:
    print("Category: Child \nTicket Price is :$ 100")
elif age>=12 and age<=60:
    print("Category: Adult \nTicket Price is :$ 150")
else:
    print("Category: Senior \nTicket Price is :$ 120")

# Implement login system with maximum 3 attempts (use nested if).
for i in range(3):
    user_name=input("Enter Your name : ").lower()
    password=input("Enter your password : ")
    if user_name=='madhu' and password=='madhu143@':
        print(f"Login Success\n Hello {user_name}")
        break
    else:
        print("user name or password in incorrect ....please Try again ")
else:
    print("Maximum login limit is executed")
# Check whether a number is a palindrome (use conditions).
num=int(input("Enter a number : "))
res=str(num)
if num==int(res[::-1]):
    print(f"{num} is Palindrome Number")
else:
    print(f"{num} is NOT a Palindrome Number")
# Apply discount based on shopping amount: 5000 → 20%, >2000 → 10%, otherwise no discount.
amount=int(input("Enter ammount: "))
if amount>=2000 and amount<5000:
    print(f"discount 10% {amount} is = {amount*0.10}\n TOtal bils is {amount-amount*0.10}")
elif amount>=5000:
    print(f"discount 20% {amount} is = {amount*0.20}\n TOtal bils is {amount-amount*0.50}")
else:
    print(f"No Discount \n Total amount is {amount}")

# Traffic signal system: Red, Yellow, Green actions.
signal=input("Enter Signal colour : ").lower()
if signal=='red':
    print(f"{signal} = STOP")
elif signal=='yellow':
    print(f"{signal} = WAIT")
elif signal=='green':
    print(F"{signal} = LET'S GO")
else:
    print(f"{signal} IS INVAID SIGNAL COLOUR")
