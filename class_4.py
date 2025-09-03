#dictionary 

info = {
    "name" : "ghazala sehar",
    "subjects" : ["java" , "c" , "c#"],  #list
    "topics" : ("dict" , "set"), #tuples
    "age" : 15,
    "is_adult" : True,
    "marks" : 43.9,
}

print(type(info))
print(info)

print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["marks"])


info["name"] = "biya" #overwrite
print(info)



null_dict = {}
null_dict["name"] = "apna college"
print(null_dict)

#nested dictionary
student = {
    "name" : "ayesha",
    "subjects" : {
        "phy" : 89,
        "isl" : 32,
        "math" : 98
    }
}

""" print(student)
print(student["subjects"])
print(student["subjects"]["isl"]) """

print(student.keys()) #keys
print(len(student))
print(student.values()) #values
print(student.items())

# print(student["name2"]) #--->error
# print(student.get["name2"]) #return none beacuse they does'nt exist

student.update({"city" :"karachi"})
print(student)


#sets 
#sets ignore the duplicate values
collec = {1,2,3,4,2,1, "hello" , "hello" , "world"}
print(collec)
print(len(collec))

collection = set() #empty set syntax
print(type(collection))


#set methods
col = set()
#add
col.add(1)
col.add("apna college")
col.add(2)
col.add(2)
col.add(3)

print(col)

#remove
# col.remove("apna college")
# print(col)


print(len(col))

#clear
col.clear()
print(len(col))

#pop is used to print the randomly values 
colle = {"hello" , "world" , "apna" , "college" , "program" , "codeing" , "python"}
print(colle.pop())

""" #union 
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) """


#intersection
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2))


#stroe following word in a python dictionary
dict = {
    "table" : ["a peice of furniture " , "list of facts & figures"],
    "cat" : "a small animal",
}
print(dict)


set_d = {"python" , "java" ,"c++"  ,"python", "javascript" , "java" , "python", "java" , "c++" , "c"}
print(len(set_d))


""" #
marks = {}

x =int(input("Enter phy marks: "))
marks.update({"phy" : x})

x =int(input("Enter math marks: "))
marks.update({"math" : x})

x =int(input("Enter isl marks: "))
marks.update({"isl" : x})

print(marks) """


val = {9,9.0,8,8.0}
print(val)