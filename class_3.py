#list

marks = [32.7 , 87.4 , 45.7 , 90.2 , 32.4]
print(marks)
print(type(marks))
print(marks[2])
print(marks[1])
print(len(marks))


""" #string is immutable (can't be changed) eg:
str = "hello"
print(str[0])
str[0] = "y" """

#list is imutable (can be changed) eg:
student = ["amaya" , 89.4 , 32 ,"karachi"]
print(student[2])
student[2] = 12
print(student)


#list slicing 
mark = [21,54,87,34,87]
# print(mark[1:4])
# print(mark[1:])
# print(mark[ :4])
print(mark[-3:-1])

#append (end mai jor dena)
my_list = [2,1,3,1]

""" my_list.append(4)
print(my_list) """

""" #sort
my_list.sort() #ascen
print(my_list) """

""" #sort
my_list.sort(reverse=True) #descen
print(my_list) """

""" #reverse
my_list.reverse()
print(my_list) """

""" my_list.insert(1,5)
print(my_list)
 """

""" #remove : first occurence of element 
my_list.remove(1) # 1 is index 
print(my_list) """


#tuple is immutable
tup = (2,1,3,1)
print(tup)
print(type(tup))
print(tup[2])
print(tup[3])
print(tup[1:3])

#tuples method
print(tup.index(2))# 2 is element not a index 
print(tup.count(1))

# tup[0] = 5 -----> error because tuple is immutable 


""" #WAP to ask the user favouriate movei name and store them in a list. 

moveis =[]
mov = input("Enter movei number 1: ")
moveis.append(mov)

mov = input("Enter movei number 2: ")
moveis.append(mov)

mov = input("Enter movei number 3: ")
moveis.append(mov)


print(moveis) """



#palindrome words: Civic,Level,Madam,Mom,Noon,Radar,Deed,Racecar,Refer

""" #WAP to check if a list is palindrome of element (hint use copy() method)

list1 = [1,2,1] #PALINDROME
list1 = ["m" , "a" , "a" , "m"] #PALINDROME
#list1 = ["m" , "a" , "a" , "m" , "p"] #NOT PALINDROME
# list1 = [1,2,3]   NOT PALINDROME

cop_list1 = list1.copy()
cop_list1.reverse()


if(cop_list1 == list1):
    print("palindrome")
else:
    print("not palindrome") """


#WAP to count the number of student with the A grade in the following tuples 
#["C" , "D" , "A" , "A" , "B" , "B" , "A"]

tupl = ("C" , "D" , "A" , "A" , "B" , "B" , "A")
print(tupl.count("A"))


#store the above value in the list and sort them  from "A" to "B"

grade = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]
grade.sort()
print(grade)