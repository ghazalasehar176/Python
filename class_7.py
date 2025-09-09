#file I/O (input output)
#File I/O in Python ka matlab hai **file Input aur Output operations** — yani file ko **read** karna (input) aur file me **write** karna (output). ✅
#text file: .txt , .docs , .log etc 
#binary file: .mp4 , .mov , .jpeg , .png , etc


#read
""" f = open("demo.txt" , "r")
# data = f.read() #read file
data = f.readline()#read line by line 
print(data)
print(type(data))
f.close() """


#write
""" f = open("demo.txt" , "w") #overwrite the file
f.write("hello i'm learning javascript tommorrow")
f.close() """

#append
f = open("demo.txt" , "a") #append (add at the end)
f.write("\nthen i'll move to react js")
f.close()


""" #with syntax
with open("demo.txt" , "r") as f:
    data = f.read()
    print(data) """

""" #delete 
import os #os stand for operating system
os.remove("sample.txt") """



""" with open("practice.txt" , "w") as f:
    f.write("hi everyone\nwe are learning file I/O \nusing java\ni like programming in java\n")

with open ("practice.txt" , "r") as f:
    data = f.read()
new_data = data.replace("java" , "python")
print(new_data)


with open ("practice.txt" , "w") as f:
   f.write(new_data) """


""" #search word kearning
def  search_word():

    word = "learning"
    with open("practice.txt" , "r") as f:
        d = f.read()
        if(d.find(word) != -1):
            print("found")
        else:
            print("not found")

search_word()
 """


""" def search_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt" , "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
                 
    return -1

print(search_line()) """


count = 0 
with open("practice.txt", "r") as f:
    data = f.read()
   
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
        
print(count)


 