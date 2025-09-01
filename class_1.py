print("My name is Ghazala")
print("My age is 20")

print("hello world" , "my self biya")
# print() function do strings ko screen pe space ke sath print karega.
print(20)
print(30+20)

name = "biya"
age = 19
price = 25.00

print("My name is:" ,name)
print("My age is:" , age)
print("Our company price is:", price)


print(type(name))
print(type(age))
print(type(price))

 


a = True
b = None
print(type(a))
print(type(b))

#sum of two numbers

num_1 = 10
num_2 = 20
sum_num = num_1 + num_2
print("num 1 value is:" , num_1)
print("num 2 value is:", num_2)
print("the sum of two number is :", sum_num) 



#arithematic operator
val_1 = 2
val_2 = 3
print(val_1 + val_2)
print(val_1 - val_2)
print(val_1 * val_2)
print(val_1 / val_2)
print(val_1 % val_2)
print(val_1 ** val_2)

#relational / comparison operator
print(val_1 == val_2)#false
print(val_1 != val_2)#true
print(val_1 >= val_2)#false
print(val_1 > val_2)#false
print(val_1 <= val_2)#true
print(val_1 < val_2)#true


#assignment operator

""" num_ = 10
num_ = num_ + 10
print(num_) """

#num = num + 10 (ko short mai likny ka tareeqa) num += num

b = 5
c = 5
d = 5
e = 10
f = 7
g = 3

b += 2
c -= 2
d *= 2
e /= 2
f %= 2
g **= 2

 
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#logical operator : and, or , not

""" #input
my_name = input("enter your name ")
print("welcome",my_name) """

""" namee = str(input("Enter name:"))
age = int(input("Enter age:"))
marks = float(input("Enter marks:"))

print("welcome",namee)
print("your age is:",age)
print("your marks is:",marks) """


""" my_num1 = int(input("Enter number 1:"))
my_num2 = int(input("Enter number 2:"))
my_num_sum = my_num1 + my_num2 
print("The sum of two number is:",my_num_sum) """


""" side = float(input("Enter square side:"))
# area = side*side
area = side ** 2

print("area =",area) """
 
first = float(input("Enter number 1:"))
second = float(input("Enter number 2:"))

average = (first +second) / 2
print("average of two number is:",average)


print("hello world!")

# print the same line
print("my name is ghazala" , "i'm  aptech student")
 


#variables 
name = "ghazala"
price = 235.00
age = 20

print("my name is " ,name)
print("price is " ,price)
print("my age is " ,age)

print(type(name))

""" food = input("food is: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet!") """

#clever if
age  = int(input("Enter age: "))
vote = ("no" , "yes") [age >= 18]
print(vote)

#conditions
food = input("food is: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet!")