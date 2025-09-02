# \n for next line (escape sequence character)
str = "my name is ghazala.\n i am a SE"
print(str)


#concatenation
str1 = "hello"
print(len(str1))

str2 = " ghazala"
print(len(str2))

print(str1 + str2)

#index help to access character
str3 = "aptech"
ch = str3[3]
print(ch)

#slice (accessing part of a string )
str4 = "aptech"
print(str4[0:4])

#slicing (negative indexing) 
str5 = "apple"
print(str5[-5:-1])

#endswith function 
str6  = "i 'm studying in Aptech learning"
print(str6.endswith("ning"))#true
print(str6.endswith("in"))#false

#Capitilized the first word of the sentence
str7 = "i am student"
str7 = str7.capitalize()
print(str7)

#replace
str8 = "i'm studying python from apna college"
print(str8.replace("o" , "a"))
print(str8.replace("python" , "javascript"))

#find
str9 = "i'm from studying python from apna college"
print(str8.find(" "))

#count
str10 = "i'm from studying python"
print(str10.count("y"))

""" #write a program to input user first name and  print its length
user_int = input("Enter user first name: ")
print("the lenght is :",len(user_int))
 """


""" #WAP to find the gretest of 3 number entered by the user
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if(a >= b and a >= c):
    print("greatest number is A")
elif(b >= c):
    print("greatest number is B")
else:
    print("greatest number is C") """



""" #WAP a program and check number is multiple of 7 or not.
num = int(input("Enter nummebr as you want: "))

if(num % 7 == 0):
    print("multiple of ",num)
else:
    print("not a multiple of", num) """