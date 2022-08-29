"""
print("Hello World") #print function


name = "Ömer" #define variable
print(name)


name_1 = input("What is ur name? ") #input function
print("Welcome " + name_1)


# String 
a = "Merhaba Efendim."
print(a.upper())
print(a.lower())
print(a.find("Efe")) #find command, give index of first occurance of search
print(a.replace("Efendim", "Ali"))
print("Efendim" in a) #check the word in variable


# Type Conversion
birth_year = input("What is ur birth year: ")
age = 2022 - int(birth_year) #change data type string to integer
print("You are " + str(age)) #change data type int to str


#basic calculator
x = float(input("Enter first number = "))
y = float(input("Enter second number = "))
sum = x + y
print("Result = " + str(sum))


# Arithmetic Operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3) 
print(10 ** 3)


# Comparison & Logical Op 

>
>
<=
>=
==
!=

and
or
not


# IF & Else
temp = int(input("Hava sıcaklığını giriniz. C° = "))
if temp >= 25:
    print("Hava Çok Sıcak.")
elif 18 <= temp <= 25:
    print("Hava Çok Güzel")
else:



# While Loop
i = 1 
while i <= 10:
    print(i * "*")
    i += 1

    print("Bu gün Hava Soğuk.")
"""
