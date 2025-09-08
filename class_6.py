#block of statement that perform a specific task or decrease redudancy
def sum(a,b):
    return a + b 

# cal = sum(2,10)
cal = sum(10,12)
print(cal)

def pri_text():
    print("hello")

pri_text()
pri_text()
pri_text()


""" #avergae of 3 student
def avg(a,b,c,):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

avg(10,29,43)
avg(2,1,3) """


#there are two type of function :
#built-in function or user-defined function

# (, end = " ") used for a text is not printing in next line


"""
#default parameter
 #assinging a default value to parameter , which is used when no argument is passed.
def defu(a,b=1):
    print(a * b)
    return a * b
defu(2) """



""" city = ["karachi" , "delhi" , "mumbai" , "islamabd" ,"lahore"]

def leng(city):
    print(len(city))

leng(city) """


""" #all list print in one line
hero = ["ironman" , "thor" , "spiderman" , "hulk"]

def pr_len(list):
    print(len(list))

def pr_len(list):
    for i in list:
        print(i , end = " ")

pr_len(hero)
print() """


""" #factorial 
n = 5
fact = 1
for i in range( 1, n+1):
   fact *= i

print(fact) """



""" #factorial using function
def cal_fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fac(5) """


#WAF to convert USD in INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val , "USD =" , inr_val , "INR ")

converter(100)


#recursion : when a function call itself repeadtly
#Recursion ek process hai jisme function apne aapko call karta hai jab tak condition (base case) true na ho jaye.

""" def re(n):
    if(n == 0): # ----> called base case
        return
    print(n)
    re(n-1)
re(10) """



""" 
#using recursion calculate factorial
def fac(n):
    if(n == 1 or n == 0):
       return 1
    return fac(n-1) * n

print(fac(4)) """



#write a recursion functionto calculate the sum of first n natural numbers 
def cal(n):
    if(n ==0 ):
        return 0
    return cal(n-1) + n

s = cal(10)
print(s)


#WAP to print all element in list
def li(list , idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    li(list , idx +1)


fruit = ["mango" , "lichi" , "banana" , "orange"]
li(fruit)