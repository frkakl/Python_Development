print("Hello World") #print function

"""
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
print("Efendim" in a) #Checks if "Efendim" is included in the variable

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
    print("Bu gün Hava Soğuk.")


# While Loop
i = 1 
while i <= 10:
    print(i * "*")
    i += 1

    
# Lists
names = ["Ömer", "Ahmet", "Mehmet", "Ali", "Veli"]
print(names)
print(names[0])
names[3] = "Yavuz"
print(names)
print(names[0:3]) # Print out 0th to 3th

names.append("Efe") # Add "Efe" to names list
print(names)

names.insert(0, "Osman") # Add "Osman" to 0th index of names list
print(names)

names.remove("Mehmet") # Remove "Mehmet" from names list
print(names)

print("Ahmet" in names) # Checks if "Ahmet" is included in the list

print(len(names)) # Print number of the elements in list


# For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



# range() Function
nums = range(10) # nums limited with 10
for number in nums:
    print(number)


nums_1 = range(5, 10) # nums limited with 5 between 10
for number in nums_1:
    print(number)


nums_2 = range(5, 10, 2) # nums limited with 5 between 10 and numbers increase with plus in two
for number in nums_2:
    print(number)



#Tuples
#Tuples are similar to lists but tuples are cannot be changed
asd = (1, 2, 3, 4, 5)
# asd[3] = 2 code gives us this error "'tuple' object does not support item assignment"
print(asd)


#Functions
def user_register(): #Defining function
    fname = input("Name: ")
    fsurname = input("Surname: ")
    print("Wellcome " + fname + " " + fsurname + ". You are Registered Now.")

print("Wellcome Please Register")
user_register() #Call the function 

"""

