#loops are used to repeat instruction
#process of searching is called linear serching 
""" #while loop
count = 1
while(count <=5):
    print("hello")
    count +=1 """


""" #reverse while loop from 1 to 5
i = 5
while(i >=1):
    print(i)
    i -=1 """


""" #print numebr from 1 to 100
num = 1
while(num <=100):
    print(num)
    num += 1 """

""" #print numebr from 1 to 100

n = 100
while(n >=1):
    print(n)
    n -= 1 """

""" #print the table 
n = int(input("Enter any numbuers: "))
i = 1
while(i <= 10):
    print(n * i)
    i +=1 """

"""  #list 
num = [1,4,9,16,25,36,49,64,81,100]
 
idx = 0
while(idx < len(num)):
    print(num[idx])
    idx += 1 """
 

""" #list
hero = ["ironman" , "thor" , "batsman" , "superman"]

idx = 0
while(idx < len(hero)):
    print(hero[idx])
    idx += 1 """

""" #tuples 
num = (1,4,9,16,25,36,49,64,81,100 , 36)

x = 36

idx = 0 
while(idx < len(num)):

    if(num[idx] == x):
        print("found at idx " , idx)
        break
    else:
        print("finding .... ")
    idx += 1 """



""" #break: ysed to terminate the lopp when ensountered(jaha break likengy whi loop ruk jayega )
i = 1 
while( i <= 5):
    print(i)

    if(i == 3):
        break
    i += 1
 """

""" #continue terminate execution in the current iteration & continue execution loop with the next iteration(current iteration ko rukhta hy phir agy barh jata hy )

i = 0 
while(i <= 5):
    if(i == 3):
        i +=1
        continue #skip
    print(i)
    i += 1 """



#for loop
""" num = [1,2,3,4,5]
for val in num:
    print(val) """


""" tup = (1,2,3,4,5)
for num in tup:
    print(num) """


""" #piece the all words
str = "apnacollege"
for chr in str:
    if(chr == 'o'):
        print("o found")
        break
    print(chr)
else:
    print("Loop end!!") """



""" 
#process of searching is called linear serching
num = [1,4,9,16,25,36,49,64,81,100, 49]
x = 49

idx = 0
for n in num:
   if(n == x):
      print("index found at" , idx)
      break
   idx +=1 """


#range function
""" seq = range(10)

for i in seq:
     print(i) """

   
""" for i in range(10): #range(stop)
    print(i) """

""" for i in range(2,10): #range(start ,stop)
    print(i) """

""" for i in range(2,10,2): #range(start ,stop , step-size) 
#step-size means kitny se increase karna hy
    print(i) """


""" for i in range(1, 101):
    print(i) """

""" for i in range(100, 0, -1):
    print(i) """

""" 
#table using for loop

n = int(input("Enter any number: "))

for i in range(1,11):
    print( n * i) """

""" #pass is a numm statment that does nothing . it is useda s a placeholder for future code.
for i in range(10):
    pass

print("example of pass stameent") """

""" #WAP to find the sum of first natural number
n = 4
sum =0 
for i in range(1 , n+1):
    sum += i
print("sum of first natural number is:" , sum) """

""" #WAP to find the sum of first natural number(using while loop)
n = 7
sum = 0 
i = 1
while(i <=n):
    sum += i
    i += 1
print("total sum =" , sum) """


""" #factorial (while loop)
n =5
fac = 1
i = 1
while(i <= n ):
    fac *= i
    i += 1

print("factorial is: ",fac) """



""" #factorial (for loop)
n = 5
fac = 1
for i in range(1, n+1):
    fac *= i
print("factorial is: ",fac) """