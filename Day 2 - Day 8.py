#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


print(Hello World)


# ### integers

# In[3]:


1


# In[4]:


343


# In[5]:


6756756


# In[6]:


print(78)


# ## FLOATS: decimal value

# In[7]:


7.0


# In[8]:


7


# In[9]:


print(7.6)


# In[10]:


type(7)


# In[11]:


type(7.0)


# ## strings:
# 
#  " ", ''

# In[13]:


"porosity"


# In[14]:


'porosity'


# In[15]:


type("porosity")


# In[16]:


"@##$(@#$()@*&*(@#(043nxmknx,mcn,mnsknds)))"


# In[17]:


"7"


# In[18]:


type(7)


# In[19]:


type(7.0)


# In[20]:


type("7")


# In[21]:


"97897+93493"


# ## Booleans

# In[22]:


8>2


# In[23]:


True


# In[24]:


False


# In[25]:


type(True)


# ## Mathematical Operations

# In[26]:


55+44


# In[27]:


55*2


# In[28]:


23-12


# In[29]:


55/2


# In[30]:


10/2


# In[31]:


10.0+5


# In[32]:


10+5


# In[33]:


5**3


# In[34]:


# * for multiplication, ** for exponential power

print(5*2)
print(5**2)


# In[35]:


31/5


# In[36]:


31//5


# In[37]:


31%5


# In[38]:


# string


# In[39]:


"55+22"


# In[40]:


"55"+"33"


# In[42]:


"Hello"+" All"


# In[43]:


"5"*3


# In[44]:


"5"+"5"+"5"


# In[45]:


"petroleum "*3


# In[46]:


## booleans


# In[47]:


78>56


# In[48]:


78<56


# In[49]:


55==55


# In[50]:


55==65


# In[51]:


56>23 


# In[52]:


25<45


# In[56]:


56>23 and 25<45


# In[55]:


56>23 and 25<20


# In[57]:


43>23


# In[58]:


45<21


# In[60]:


43<23 or 45<21


# ## Variables:
# 
# - Containers for storing informations
# 
# - variables are created "="
# 
# - for a given runtime

# In[61]:


porosity = 20


# In[62]:


porosity


# In[64]:


"hello"


# In[65]:


porosity==45


# In[67]:


b = "Petroleum"


# In[68]:


b


# In[69]:


type(b)


# In[4]:


#reintialise
b = "porosity"


# In[5]:


b


# In[6]:


b


# ### Variable names cannot start with a number or special character, ie 2,3,4,@#
# 
# 
# ### Variable name doesnot have any space in between two characters, but underscore can be used

# In[7]:


1a = 45


# In[8]:


a1 = 45


# In[9]:


a1 


# In[10]:


@a = 43


# In[11]:


_a = 45


# In[12]:


_a


# In[13]:


porosity 1 = 45


# In[14]:


poosity_1 = 45


# In[15]:


poosity_1


# In[16]:


poro_1 = 20
poro_2 = 10 


# In[17]:


poro_1+poro_2


# In[18]:


poro_1-poro_2


# In[19]:


poro_1/poro_2


# In[26]:


a = "Hello "
b = 3


# In[23]:


a*3


# In[27]:


a,b = "Hello",3


# In[28]:


a


# In[29]:


b


# ## input = taking input from user
# 
# - takes input in for of strings

# In[30]:


input()


# In[31]:


perm = input()


# In[32]:


perm


# In[33]:


type(perm)


# In[34]:


perm = input("Enter the formation's permeability: ")


# In[35]:


perm


# In[36]:


perm/2


# ## type conversions

# In[37]:


perm


# In[38]:


type(perm)


# In[39]:


float(perm)


# In[40]:


type(perm)


# In[41]:


perm


# In[42]:


perm = float(perm)


# In[43]:


type(perm)


# In[44]:


perm


# In[45]:


a = 3


# In[46]:


type(a)


# In[47]:


str(a)


# In[48]:


a = str(a)


# In[49]:


a


# In[50]:


float(a)


# In[51]:


a = 'petroleum'


# In[52]:


a


# In[53]:


float(a)


# In[54]:


a= 6.5


# In[55]:


int(a)


# In[56]:


int(6.7)


# In[57]:


permeability = float(input("Enter the formation's permeability: "))


# In[58]:


permeability


# In[60]:


type(permeability)


# ## String Formatting

# In[71]:


permeability = float(input("Enter the formation's permeability: "))
porosity = float(input("Enter the formation's porosity: "))
print(f"Formation Porosity is {porosity*100}, and permeability is {permeability} md, and product of both is {porosity*permeability}")


# In[67]:


print("Formation Porosity is {}, and permeability is {} md".format(porosity,permeability))


# In[68]:


print("Formation porosity is ", porosity, "and permeability is ", permeability)


# In[1]:


weather = "rainy"
weather2="very cloudy"

f"today is a very sunny day"


# In[2]:


f"today is a {weather} day"


# In[3]:


f"today is a {weather} and {weather2} day"


# In[4]:


perm=[2,5,77,[44,66,81,10], 43,33]


# In[5]:


perm


# In[6]:


perm[3]


# In[7]:


perm[3][2]


# In[8]:


len[perm]


# In[9]:


len(perm)


# In[10]:


perm[-1]


# In[11]:


perm


# In[12]:


perm[2]="Ahmad"


# In[13]:


perm


# In[14]:


# append to add element to the list
perm.append(99)


# In[15]:


perm


# # Slicing : accessing more than one data
# list[start, stop, step]
# stopping index is always EXECLUDED, meaning: in any slicing process, always increase 1 more, because python will excelude it and hence you get exactly the last value you want in slicing. In negative slicing, do vise versa. 
# (I noticed that when we use step size, the last index is included?!

# In[16]:


# if we want to slice perm between Ahmad (which is index 2), and 33 (which is index 5), increase 1 to the last index:
perm[2:6]


# In[17]:


perm[1:300]


# In[18]:


perm[1:]


# In[25]:


perm
perm[:3]


# In[20]:


perm[:100]


# In[24]:


perm


# In[26]:


perm[:]


# In[27]:


perm[::]


# In[28]:


perm[::2]


# In[30]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']


# In[31]:


li


# In[42]:


li[6][3][ -4: :-2]


# In[5]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']


# In[6]:


li


# In[7]:


li[6]


# In[32]:


li[6][3][-4::-2]


# In[33]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']
# Get ghery, 98695

li[6]


# In[34]:


li[6][3]


# In[55]:


li[6][3][2::-2]
# we don't put (0) as stop point because stop point will be excluded then you end up having only 'ghery'. so keep 
#the stop point open. 


# In[39]:


li[6][3][-4::-2]


# In[53]:


li[6][3][-4::-2]


# # Tuples: 
# # Class#4, Sunday 9-Sep. 2023
# 
# ()
# immutable
# like list, it can be sliced and accessed
# ordered 

# In[44]:


# Reverse items in a tuple

tuple1 = (10, 20, 30, 40, 50)
tuple1=tuple1[::-1]
tuple1


# In[80]:


t=(34,23,1,230)
t[1]


# In[83]:


# Tuples are immutable, unlike lists:
t[1]=[22]


# In[46]:


tuple2=('1', '2','3','4','6')
type(tuple2)


# In[49]:


tuple2=tuple2[::-1]
tuple2


# In[50]:


# The given tuple is a nested tuple. write a Python program to print the value 20.
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple1[0]


# In[52]:


tuple1[1][1]


# In[58]:


# Exercise 3: Create a tuple with single item 50
tuple1=(50,)
tuple1


# In[91]:


# Write a program to unpack the following tuple into four variables and display each variable.
tuple1 = (10, 20, 30, 40)

a= tuple1[0]
b= tuple1[1]
c= tuple1[2]
d= tuple1[3]
print(f"variable1 = {a}\n variable2 = {b}\n variable3 = {c}\n variable4 = {d}")


# In[62]:


# OR

tuple1=a,b,c,d
tuple1


# In[94]:


#Exercise 5: Swap two tuples in Python
#Given:

tuple3 = (11, 22)
tuple4 = (99, 88)

tuple3,tuple4=tuple4,tuple3

print(f"Tuple3 is: {tuple3}")
print(f"Tuple4 is: {tuple4}")


# In[76]:


#Exercise 6: Copy specific elements from one tuple to a new tuple
#Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)

tuple2=tuple1[3:5]
tuple2


# In[78]:


#OR
tuple2 = tuple1[3:-1]
tuple2


# In[107]:


# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tup = (11, [22, 33], 44, 55)


# In[108]:


tup[1]


# In[112]:


# I tried to put 222 in sequare brackets, it gave 222 inside breackets which is not correct i guess.
# Then i tried to place it between parentheses (), it works... however, in the website, they put it only number 222.
# my method and the website shows same answer

tup[1][0]=222
tup


# In[4]:


my_tuple2 = tuple(['apple', 'banana', 'cherry'])


# In[5]:


my_tuple2


# In[6]:


type(my_tuple2)


# In[8]:


# from: https://www.linkedin.com/pulse/tuples-beginners-guide-pythons-immutable-data-type-swarooprani-manoor/


# Creating a tuple using parentheses
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Creating a tuple using the tuple() function
my_tuple2 = tuple(['apple', 'banana', 'cherry'])

# Creating an empty tuple
empty_tuple = ()

print(my_tuple)     # (1, 2, 3, 'a', 'b', 'c')
print(my_tuple2)    # ('apple', 'banana', 'cherry')
print(empty_tuple)  # ()


# In[9]:


# Accessing elements using indexing
print(my_tuple[0])   # 1
print(my_tuple[3])   # 'a'
print(my_tuple[-1])  # 'c'

# Accessing elements using slicing
print(my_tuple[1:4])    # (2, 3, 'a')
print(my_tuple[3:])     # ('a', 'b', 'c')
print(my_tuple[:2])     # (1, 2)
print(my_tuple[::2])    # (1, 3, 'b')

# Accessing elements using iteration
for element in my_tuple:
    print(element)


# In[10]:


# create a tuple
t = (1, 2, 3, 2, 4, 2)

# use the count method to count the number of times a given element appears in the tuple
count_of_2 = t.count(2)
print(count_of_2)   # output: 3

# use the index method to find the index of the first occurrence of a given element in the tuple
index_of_4 = t.index(4)
print(index_of_4)   # output: 4


# In[11]:


# create two tuples
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

# concatenate the two tuples
t3 = t1 + t2
print("Concatenated Tuple:", t3)

# find the maximum element in the tuple
print("Maximum Element in Tuple:", max(t1))

# find the minimum element in the tuple
print("Minimum Element in Tuple:", min(t2))

# find the length of the tuple
print("Length of Tuple:", len(t3))


# # Storing Coordinates: Tuples are often used to store coordinates in 2D or 3D space. 
# 
#     It is advantageous to use a tuple to store coordinates because coordinates 
#     are essentially an ordered pair or set of values that are used to represent a specific location in space. 
#     Tuples, being immutable and ordered, provide a natural and efficient way to store and manipulate such data.
# For example, suppose you are writing a program that involves plotting points on a 2D graph. 
# Each point can be represented by a tuple with its x and y coordinates.
# Since tuples are immutable, you can be assured that the coordinates of 
# each point will not change accidentally or intentionally. 
# This is particularly important when you have a large number of points, as it helps to maintain the integrity of your data.
# In addition, tuples can be easily unpacked, which makes 
# it convenient to work with the individual components of a coordinate. For instance,
# if you have a tuple representing a point, you can easily extract its x and y values and use them in your 
# calculations without having to write additional code to extract the values from a list or dictionary.

# In[12]:


# Define coordinates using a tuple
coordinates = (3, 4)

# Access the coordinates using index
x = coordinates[0]
y = coordinates[1]

# Print the coordinates
print("x-coordinate: ", x)
print("y-coordinate: ", y)


# # Storing date and time
# Suppose you are developing a booking system for a hotel. Each booking includes a check-in date and a check-out date. 
# You could represent each date as a tuple with the following structure: (year, month, day). 
#     Similarly, you could represent each time as a tuple with the following structure: (hour, minute).
# For example, a booking for a room from April 1st, 2023 to April 5th, 2023 and a check-in time of 3:00 PM 
#     could be represented as the following tuple:
#     

# In[14]:


check_in = (2023, 4, 1, 15, 0)
check_out = (2023, 4, 5)


# In[15]:


# Example tuple for returning multiple values from a function
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)
rectangle_values = calculate_rectangle(5, 10)
print(rectangle_values)


# # Dictionary
# 

# In[3]:


#keys: values
    #{}
    #stoe dict, ,lists, tuples, str, int, floats in values
   # helps in storing data 
    


# In[5]:


# keys must be unique
# if keys are duplicated, the value will be updated to the latest data
# meaning, you can't assign it to more than value


# In[7]:


## special characters are not allwed for key
## but, float,integers, and strings are allowed as keys


# In[8]:


## values can be anything: list, tuples, set, anything


# # Accessing data from a dict

# In[3]:


d1={'n',[2,3,4],{2.3.1}}


# In[10]:


# to access a set, you convert it to list first


# In[11]:


d=("ahmd",3,3)


# In[12]:


type(d)


# In[15]:


rock_properties={'porosity':0.3, 'permeability':10, 'waterSat':0.25}


# In[16]:


rock_properties


# In[23]:


specific_gravity = [0.2,0.3,0.4,0.87,0.9,1,0.2]
for i in specific_gravity:
    API= (141.5/i-131.5)
    print(f"API gravity for a specific gravity {i} is {API}")


# In[24]:


specific_gravity = [0.2,0.3,0.4,0.87,0.9,1,0.2]
for i in specific_gravity:
    API= (141.5/i-131.5)
    print(f"API gravity for a specific gravity {i} is {API}")


# In[25]:


#Print = In field _____ , the value of porosity(%) is _____ and perm is ____


# In[34]:


perm = [1,2,3]
field_name = ['Neelam','Panna', 'volve']
porosity = [0.2,0.3,0.4]
for i,j,k in zip(perm,field_name,porosity):
    print(f"In field {j}, the value of porosity(%) is {k*100} and perm is {i}")


# In[25]:


#Print = In field _____ , the value of porosity(%) is _____ and perm is ____
perm = [.3,52,13]
formation_name = ['Dhruma','Dammam', 'Hanifa']
porosity = [0.17,0.18,0.22]

# solution
# we have to use zip with iteration because of multiple inputs

for k, f, p in zip (perm, formation_name, porosity):
    print(f"In formation {f}, the value of porosity is {p*100} %, and perm is {k} mD")


# In[28]:


poro=(0.3,.12, .22,.15)
poro


# In[29]:


poro=(0.3,.12, .22,.15)
for i in poro:
    print(i)


# In[31]:


poro=(0.3,.12, .22,.15)
for i in poro:
    print(f"the value of i is {i}")
    print(i)
    print("++++++++++++++")
print("Outside the for loop")


# In[63]:


API_specific_gravity = []
specific_gravity=[.2,.3,.4,.87,.9,1,.2]
for i in specific_gravity:
    api=141.5/i-131.5
    print(f"API value for SG {i} is {api}")
    API_specific_gravity.append(api)


# In[61]:


API_specific_gravity


# In[65]:


import matplotlib.pyplot as plt
specific_gravity.sort()
API_specific_gravity.sort()
plt.plot(API_specific_gravity,specific_gravity)


# In[66]:


perm = [12,10,33]

specific_gravity


# In[68]:


for i in perm:
    print(f"For perm vlaue {i}")
    print("Specific Gravities will be printed")
    for j in specific_gravity:
        print(f" for perm {i}, SG is {j}")
        print("+++======+++======")


# # ZIP

# In[70]:


perm


# In[71]:


poro


# In[72]:


specific_gravity


# In[74]:


for i,j,k in zip(perm,poro,specific_gravity):
    print(f"perm is {i}")
    print(f"poro is {j}")
    print(f"specific gravity is {k}")
    print("**********")
    


# In[75]:


for i,j,k in zip(perm,poro,specific_gravity):
    c=i*k/j
    print(f" The value of perm * SG / poro is {c}")


# In[82]:


formation_pro =[]
for i,j,k in zip(perm,poro,specific_gravity):
    c=i*k/j
    print(f"The value of perm * SG / poro is {c}")
    formation_pro.append(int(c))
    print("^^^^^^^^")
print(f"Formation_pro are {formation_pro}")


# In[83]:


formation_pro


# In[ ]:


#Print = In field _____ , the value of porosity(%) is _____ and perm is ____



# # If -else   ...class#5 Fri 22 Sep.

# In[84]:


float(input("Enter the reservoir pressur"))


# In[16]:


if False:
    print(f"Formation porosity")
    
else:
    print(f"Formation permeability will be used")


# In[68]:


# I think there is a way to make the script shorter..

Pr=float(input("Enter the reservoir-pressur: "))
Pb=float(input("Enter the pubble-point pressur: "))
if Pr < Pb :
    print("Reservoir pressure is less than pubble point pressure, therefore gas has been evolved")
elif Pr > Pb :
    print("Reservoir pressure is greater than pubble point pressure and is undersaturated")
if Pr == Pb:
    print("Reservoir is saturated")


# # While loop: To repeat a block of code again and again; until the condition satisfies

# In[64]:


c= 4
while c<10:
    print(f"{c} is lesser than 10")
    print(f"c is = {c}")
    c = c+1


# In[ ]:


temperature (C) = 50

#doing a process because of which our RP is increasing

while pressure < 2500:
    print(f"{pressure} is not abnormal")
    ##process
    pressure = pressure+100
    
print(f"{pressure} is abnormal now")


# In[71]:


temperature = 50

#doing a process because of which our temperature is increasing

while temperature < 90:
    print(f"{temperature} is not critical")
    # process
    temperature = temperature+5
print(f"{temperature} is over the limit")


# In[73]:


Password = input("Enter the Pc Passowrd: ")

while Password!="Geologist2023":
    print("You Enter a wrong password, Please try again!!!")
    Password = input ("Enter the Passowrd again: ")
print("Access is now Granted.. Good Luck")


# # break statement: for breaking the loop prematurely
# 
# # this is to break the loop at certain place while iterating and it will stop there.

# In[77]:


x = 0

while x<7:
    x+=1
    if x==6:
        break
        
    print(x)


# In[86]:


Rp = 3000

while True:
    print(f"{Rp} is below abnormal pressure")
    #process
    Rp= Rp+ 100
    
    if Rp == 4000:
        print(f"Reservoir pressure has reached its maximum value, break the loop")
        break
print("Finished")


# In[87]:


# break with for/if loop:

x = ("Ahmad", 3,2,11,88,44)




# In[88]:


type(x)


# In[89]:


for i in x:
    print(i)
    if i == 11:
        print("Break the statement")
        break
    print("Not broken yet")


# In[93]:


x = [34,3,23,453,23,23,45,23,5464,23,5466,645,435]

list(range(len(x)))


# In[95]:


for i in x:
    print(i)


# In[110]:


for i in range(len(x)):
    print (i)
    print(f"The element at {i} index in list is {x[i]}")
    


# In[111]:


for i in range(len(x)):
    print (i)
    print(f"The element at {i} index in list is {x[i]}")
    if i == 8:
        print(f"break the loop")
        break
print ("The loop is not yet broken")


# In[113]:


for i in range(len(x)):
    print (i)
    print(f"The element at {i} index in list is {x[i]}")
    if i == 8:
        print(f"break the loop")
        break
    print ("The loop is not yet broken")


# # Continue: to jump back to top of the loop, rather than breaking/stopping it
# 
# stop the current iteration, continue with the next one.
# 

# In[114]:


for i in range(15):
    if i%2 ==0:
        print("Skipping even numbers")
        continue
    print(i)


# In[123]:


for i in range(10):
    if i%2 !=0:
        print("Skipping odd numbers")
        continue
    print(i)


# In[131]:


for i in range(15):
    if i%2 !=0:
        print(i)
        print("the result is an even number")


# In[145]:


pressure = 2500
while pressure < 5000:
    pressure = pressure+100
    
    if pressure == 4000:
        print("Skip the pressure at 4000 psi")
        continue
    print(f"pressure is {pressure} psi")


# # Square root of a number using Newton Raphson using while loop
# 
# - a numerical solution to find square roots of functions and numbers.
# - it has a general formula
# - you need first to root the function or the number to be squared,meaning make it equal = zero then you find its derivative.
# - then you make initial guess and apply it in the rooted function until you get a closer value to zero, here you use that value that makes it close to zero as your starting point and you find the deriviative and f(x) as well.
#  - for example: to find the square root of 121:
#  x = Sqrt(121)
#  X^2 = 121
#  (root it):
#  X^2 -121 = 0    This is your f(x) of the general formula of Newton-Raphson and the code, also 121 is your n in the while loop code below
#  for example if your initial guess is 4:
#  f(4) = (4^2)-121.. and you continue until you reach a value very close to zero. You will find that 10  to 10.5 or even 11 (which is the exact answer) whoud give results close to zero and you can iterate from there.
#  f'(x) = 2*x

# In[146]:


n = float(input("Enter a number to get is square root"))
x = float(input("Enter the initial guess"))

while (abs(x**2-n) > 0.0001):
    print(x)
    # process
    x = x - ((x**2-n)/(2*x))
    


# In[152]:


n = float(input("Enter a number to get its square root "))
x = float(input("Enter the initial guess "))

while (abs(x**2-n) > 0.001):
    print(x)
    # process
    x = x - ((x**2-n)/(2*x))
print(f"The square root of {n} is {x}")
print(f" The actual root of {n} is {n**0.5}")


# # Day 7 
# 
# 
# # Klinkenberg Effect in python using WHILE function

# In[5]:


# Klinkenberg Effect in python

# K(g) = Kl + c(1/pm)

# K(g) = measured gas permeability, pm = mean pressure, Kl = equivalent liquid perm(absolute perm), c = slope of line

# c = b.K(l) = 6.9 K(l)^(-0.36)

# Thus, K(g) = Kl + 6.9 Kl^(-0.36) * Kl [1/pm]
# kg * pm = K(l) * pm + 6.9 * K(l)^0.64

# f(x) = 6.9 * Kl^0.64 + pm * (Kl - kg)

# f'(x) = 4.416 * Kl**(-0.36) +pm

kg = float(input("Enter the measured Kg: "))
pm = float(input("Enter the mean pressure across the core: "))
K = float(input("Enter the initial guess of the absolute permeability: "))

while (abs(6.9 * K**0.64 + pm*K - pm*kg) > 0.00001):
    k = k - ((6.9*k**0.64+pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))

print (f" The equivalent liquid permeability K is {k}")
print (f"The percentage error is: {100*abs((k-23.66)/k)} ")


# In[14]:


kg = float(input("Enter the gas permeability of the core: "))
pm = float(input("Enter the mean pressure across the core: "))
k = float(input("Enter initial guess of the absolute permeability: "))

while (abs(6.9*k**0.64 + pm*k - pm*kg)> 0.0000001):
    k = k - ((6.9*k**0.64 + pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))
print (f"The equivalent liquid permeability of the core is {k}")
print (f"The percentage error is {abs(k-23.66)/k*100}")


# In[176]:


kg = float(input("Enter the measured permeability: "))
pm = float(input("Enter the mean pressure across the core: "))
k = float(input("Enter the initial guess of absolute permeability: "))


while (abs(6.9*k**0.64+pm*k - pm*kg)>0.0000000001):
    k = k - ((6.9*k**0.64+pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))
    
print(f"The final value of Perm K is: {k} ")

print(f"The % Error is: {100*abs((k-23.66)/k)}")


# # Python functions:
# 
# Block of statements, that does a specific task, and return something to user
# 

# In[ ]:


# instead 


# In[ ]:


b


# In[32]:


print("Hello Tarun, welcome to the class")

print("Hello Peila, welcome to the class")

print("Hello Alzokane, welcome to the class")



# In[68]:


# instead of repeating the typing ...we can use def function to make it short
def greet(name):
     print(f"Hello {name}, welcome to the class")    
     return name


# In[69]:


# I can see that I have to write it as string
greet("Saleh")


# In[70]:


greet ("السلام عليكم")


# In[71]:


greet("Khalid")


# In[72]:


def add(x,y):
    z = x+y
    print(f"Sum of {x} and {y} is {z}")
    
# I noticed that we don't need to define x and y previously:


# In[73]:


add(2,5)


# In[74]:


def add(x,y):
    z = x+y
    print(f"Sum of {x} and {y} is {z}")
    return z


# In[75]:


add (4,3)


# In[95]:


def test():
    print("This a test function")
test


# In[96]:


test()


# In[128]:


def add(x,y):
    z=x+y
    print(f" Sum of {x} and {y} is {z}")
    return z
    


# In[129]:


add(5,100)


# In[130]:


# return is now saving the add result in z and NOW z can be used outside the function:
# meaning you can get the z result and further use it in extra calculations. 
# see below
t= add(5,100)


# In[131]:


# t here will be using z outside the function for any further calculations:
t+10


# In[140]:


# multiple return can be obtained as well:

def operations(x,y):
    add=x+y
    sub=x-y
    mult=x*y
    div=x/y
    print(f" Sum of {x} and {y} is {add}")
    print(f" Subtraction of {x} and {y} is {sub}")
    print(f" Multiplication of {x} and {y} is {mult}")
    print(f" Division of {x} and {y} is {div}")
    return add,sub,mult,div
    


# In[141]:


operations(3,4)


# In[142]:


t = operations(3,4)


# In[143]:


t


# In[147]:


t*2


# In[158]:


a,b,c,d = operations(3,4)


# In[159]:


a


# In[160]:


b


# In[161]:


c


# In[162]:


def operations(x,y):
    add=x+y
    sub=x-y
    mult=x*y
    div=x/y
    print(f" Sum of {x} and {y} is {add}")
    print(f" Subtraction of {x} and {y} is {sub}")
    print(f" Multiplication of {x} and {y} is {mult}")
    print(f" Division of {x} and {y} is {div}")
    return (add,sub),[mult,div]


# In[166]:


operations(3,4)


# In[169]:


t = operations(3,4)
t


# In[170]:


t[0]


# In[171]:


t,l=operations(3,4)


# In[172]:


t


# In[173]:


l


# In[174]:


# we also can define y at the beginning: 
def operations(x,y=5):
    add=x+y
    sub=x-y
    mult=x*y
    div=x/y
    print(f" Sum of {x} and {y} is {add}")
    print(f" Subtraction of {x} and {y} is {sub}")
    print(f" Multiplication of {x} and {y} is {mult}")
    print(f" Division of {x} and {y} is {div}")
    return (add,sub),[mult,div]


# In[175]:


operations(5)


# In[202]:


def klinkenberg (kg,pm,k):
    while (abs(6.9*k**0.64 + pm*k - pm*kg)> 0.0000001):
        k = k - ((6.9*k**0.64 + pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))
    print (f"The equivalent liquid permeability of the core is {k}")
    return k


# In[203]:


klinkenberg (25,0.5,12)


# In[ ]:


# if you press shift + Tab in the pranthesis of klinkenberg, it will 
# show you the information about it.
# if you use comment, you will not see such information about documentation of your function.
klinkenberg(40,2.9,10)


# # Docstring

# In[2]:


# if you press shift + Tab in the pranthesis of klinkenberg, it will 
# show you the information about it.
# if you use comment, you will not see such information about documentation of your function.
# klinkenberg(40,2.9,10)
# Important when used by other people in a large script where search for information in comments could be difficult


# In[18]:


def klinkenberg (kg,pm,k):
    """
     This klinkenberg function calculates absolute permeability for given gas permeability at a given mean pressure.
    INPUTS:
    kg=> gas permeability in lab at a given mean pressure pm
    pm => mean pressure
    k=>User initial guess for absolute perm.
    
    return:
    k=> value of absolute permeability
    """
    count = 0
    while (abs(6.9*k**0.64 + pm*k - pm*kg)> 0.0000001):
        k = k - ((6.9*k**0.64 + pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))
        count = count+1
    print (f"The equivalent liquid permeability of the core is {k}")
    print (f"The number of iterations used = {count}")
    return k


# In[19]:


klinkenberg (46.6,2.5,2)


# In[20]:


klinkenberg(12,1,10)


# # Day 8 Numpy
# 
# - Numerical Python
# - Fast, computationally efficient
# - Arrays, doesn't exist in core python..that's why we import them

# In[ ]:


# this is how to insert a photo.. just make the line as Mark Down either by clicking 'm' on the line number or
#by choosing Mark Down from the menu.
# Press copy image, then paste and run in the conding line here.


# ![image.png](attachment:image.png)

# In[23]:


import numpy as np
a=(2,5,1,3)
a


# In[28]:


np.array

# this will convert our tuple into array by adding [].
# That dosen't denote a list, but it denotes an array with specific dimension


# In[29]:


np.array(a)


# In[30]:


porosity = [12,10,23,45,100]
por_array = np.array(porosity)
por_array


# In[31]:


type(por_array)


# # Array Dimensions
# #arrays have dimensions, 0D, 1D, 2D, 3D, and 4D

# # 0-D array:
# # it is just one point..no dimension
# # has only parantheses..no sq. brackets

# In[221]:


arr_0d = np.array(4)


# In[222]:


arr_0d


# In[223]:


type(arr_0d)


# In[224]:


arr_0d.ndim


# # 1-D Array: Array have 0-D arrays as its elements

# In[230]:


# a collection of 0 D (points or dots)
# has one sq. brackets only


# In[43]:


arr_1d = np.array([1,2,3,4])


# In[232]:


arr_1d


# In[233]:


arr_1d.ndim


# # 2-D Array: Arrays having 1-D arrays as its prime elements
# # these are matrix

# In[235]:


import numpy as np

arr_2d = np. array([[12,34,54,32], [56,34,23,23],[45,56,76,45]])


# In[236]:


arr_2d.ndim


# In[239]:


type(arr_2d)


# In[237]:


arr_2d


# # 3-D array: 2d arrays as building blocks

# In[246]:


arr = np.array([[[23,43,23],[4654,43,645]],[[567,343,23],[98,54,32]]])


# In[249]:


arr


# In[247]:


type(arr)


# In[248]:


arr.ndim


# # Higher Dimentional arraysm

# In[253]:


# number of brackets to determine the dimension of the array
arr = np.array([[[[[[34,45,6,8]]]]]])


# In[254]:


arr.ndim


# # Shape: Check the shape of array
# # how many dimensional arrays we have
# # in a particular set

# In[263]:


arr_0d


# In[264]:


arr_0d.shape


# In[265]:


arr_1d


# In[266]:


arr_1d.shape


# In[267]:


# that means: we have 4 of 0-Dimentional arrays.
# Nothing is after the comma, that means it has elements in one dimension. 


# In[268]:


arr_2d


# In[269]:


arr_2d.shape


# In[273]:


arra = np.array([[12,45], [15,20]])


# In[274]:


arra.ndim


# In[ ]:





# In[275]:


arra


# In[276]:


arra.shape


# In[279]:


arra2 = np.array([[12,45], [15,20], [17,9]])


# In[280]:


arra2


# In[281]:


arra.shape


# In[283]:


arr = np.array([[[23,43,23],[4654,43,645]],[[567,343,23],[98,54,32]]])


# In[284]:


arr


# In[285]:


arr.shape


# In[ ]:


# first we count how many square brackets we have in the arrays
# based on that we say for example 3 brackets so it is a 
# 3-D array that consists of groups of 2-D arrays. Then ask the following:
# how many 2-D arrays do we have...then
# how many 1-D array do we have in each 2-D array?
# last, how many elements/dots (i.e. 0-D arrays) do we have in 1-D array?


# if it is a 4-D array we find that it consists of groups of 3-D arrays.


# In[ ]:


##### I reached till Range in the class record. 

#### just open it again and proceed from there. 


# In[45]:


p=3
a=[2,3,4,5]
p*a


# # Using inbuild methods for generating arrays:
# 
# # arange
# # linspace (not linespace)
# # zeros,ones
# # identity matrix

# In[46]:


range(1,10)


# In[51]:


list(range(0,10))


# # Arange: np.arrange(start,stop,step), stop point is not included

# In[62]:


porosities = np.arange(5,35,2)
porosities


# # Linspace: Linearly spaced arrays
# #Note:no letter (e) in linspace function!!
# #Total number of points we want
# #np.linespace (start,stop, number of data points)
# #stopping point is INCLUDED here

# In[78]:


saturations=np.linspace(0,1,50)
saturations


# In[75]:


capillary_pressures = np.linspace(0,100,9)
capillary_pressures


# In[76]:


len(capillary_pressures)


# # Zeros and ones and identity matrix:

# In[ ]:


# Zeros are very useful as place holders for values later on. This is particularily powerful in reservoir simulation


# In[79]:


zeros = np.zeros(3,4)
# forgot the parantheses


# In[125]:


zeros = np.zeros((4,5))
zeros

# by default here, the array is 2-D, because it has 4 which means 4 1-D arrays and 5 is number of points or dots (i.e. 0-D)


# In[126]:


zeros = np.zeros((2,4,4))
zeros

# by default, this a 3-D array, because first, it has 2 2-D arrays and inside each 2-D, there are 4 1-D arrays, and finally
# there are 5 0-D arrays.


# In[127]:


zeros.shape


# In[5]:


import numpy as np


# In[6]:


ones = np.ones((2,4,4))
ones


# In[7]:


a= [2,3,4,5]
p=3

a*p


# In[8]:


a= [2,3,4,5]
b=[1,4,5,6]

a*b


# In[9]:


npa=np.array(a)
npa


# In[10]:


# Here you can multiply each element INSIDE the list as array. 
3*npa


# In[11]:


p = 3
p* ones


# In[12]:


b=[3,4,5]
c=[2,3,10]
b+c


# In[13]:


arrb = np.array(b)
arrc = np.array(c)

arrb+arrc


# In[14]:


arrb*arrc


# # eye: Identity Matrix
# 
# # having zeros or ones as identity matrix
# 
# # use 'eye' with np to create it

# In[19]:


np.eye(2)


# In[21]:


np.eye(4)


# In[22]:


np.eye(2,5,6)


# In[25]:


np.eye(3,5)


# # Array Indexing

# In[26]:


arr = np.array([1,23,45,67,54,433,32,543])


# In[27]:


arr


# In[29]:


arr[5]


# In[31]:


arr=np.array([12,34,23])


# In[32]:


arr


# In[33]:


arr=np.array([[12,34,23],[40,80,70], [12,10,6],[45,62,40]])


# In[34]:


arr


# In[35]:


arr.shape


# In[36]:


arr[3]


# In[37]:


arr[3][1]


# In[39]:


arr[-1][-2]


# In[53]:


ar=np.array([[[1,2,3],[2,3,4]],[[34,45,56],[34,78,23]]])


# In[54]:


ar


# In[56]:


2,2,3


# In[57]:


ar.shape


# In[ ]:


# How to access number (56) in the array:

# This is a 3-D array, so indexing would contain 3 squares. [] [] []
# First: since it is a 3-D array, we ask in which 2-D arrays the number falls (i.e. 1)
# second: we ask, in which array of the 1-D arrays the number falls(i.e. 0)
# Third: we ask, in the 0-D array what is the index of that number (i.e. 2)


# In[59]:


ar[1][0][2]


# In[ ]:


# get access to number 78


# In[60]:


ar[1][1][1]


# In[63]:


add=np.array([[[[1,2],[3,4],[5,6]], [[7,8],[9,67],[12,45]]],[[[24,676],[89,56],[454,23]],[[56,76],[89,89],[65,45]]]])


# In[64]:


add


# In[66]:


2,2,3,2
add.shape


# In[70]:


# Get number 646:
# - It is a 4-D array (i.e. 4 square brakets will be in the answer)
# - has two (i.e. 0 and 1) 3-D arrays, 676 is present in the 1 3-D array
# - It is in the 0 2-D array
# - It is in the 0 1-D array 
# - It is in the 1 0-D array


# In[71]:


add[1][0][0][1]


# In[ ]:


# Get the number 89 (second one)


# In[72]:


add[1][1][1][1]


# ## Array Slicing

# In[73]:


arr


# In[76]:


arr_1d = [1,2,3,4]
arr_1d=np.array(arr_1d)


# In[77]:


arr_1d


# In[78]:


# to slice from 2 to 3

arr_1d[1:3]


# In[79]:


arr


# In[81]:


# slice 10,6 and 62,40

arr[2]


# In[89]:


arr[2:, 1:]


# In[102]:


ar1=np.array([[1,2,3,4,5],[4,5,6,7,8],[12,34,56,67,85],[21,56,67,32,53]])


# In[103]:


ar1


# In[109]:


4,5
ar1.shape


# In[111]:


# How to sclice 56,67 and 67,32?

#  First: Slicing in the vertical direction:

ar1[1:3]


# In[112]:


# Second: Slicing in the horizontal direction:

ar1[1:3, 2:4]


# In[113]:


ar1


# In[150]:


# Slice [[6,8],[67,53]]:

ar1[1][2::2]

ar1[3][2::2]


# In[158]:


ar1[1::2]


# In[159]:


ar1[1::2,2::2]


# In[161]:


perm = np.array([[13,23,32,43,54],[43,55,60,7,8],[12,34,45,77,87],[2,55,39,82,49]])


# In[162]:


perm


# In[163]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[166]:


plt.figure(figsize = (10,8))
plt.title('Reservoir Permeability Grids')
sns.heatmap(perm)


# In[168]:


plt.figure(figsize = (10,8))
plt.title('Reservoir Permeability Grids')
sns.heatmap(perm,annot = True)


# In[169]:


perm


# In[176]:


perm[1:3,2:4]


# In[178]:


# Assuming that these perms have reduced by 80% due to scale. How to reflect this on the plot and data:

perm[1:3,2:4]=0.80*perm[1:3,2:4]


# In[179]:


# the specified values will now be multiplied by 80%:

perm


# In[181]:


plt.figure(figsize = (10,8))
plt.title('Reservoir Permeability Grids due to scale')
sns.heatmap(perm,annot = True)


# In[ ]:




