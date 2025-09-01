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

