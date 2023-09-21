#VARIABLES

#age = 21
#age += 1
#print("Your age is: " + str(age)) 

###################

#variable (float = floating point number {a decimal number})
#also includes string literal with typecasting to convert height to string

#height = 250.5
#print("Your heigh is: " + str(height)+"cm")
#print(type(height))

#BOOLEAN DATATYPE = STILL A VARIABLE, ONLY STORES TRUE OR FALSE
## useful when you get to if statements to determine whether not a statement is true or false

#human = True
#print("Are you a human: "+str(human))
#print(type(human))

#that's the basics of variables: they act as a container for a value, and they behave as the value that they contan.
                                                                                                                                            #there are 4 basic datatypes: 
#-->strings (series of characters)
#-->ints (a whole integer)
#-->floats (floating point numbers / a numeric value with a decimal)
#-->booleans (only store true or false)

######################

                                                                                                                                            #multiple assignment in Python

#multiple assignment allows us to assign multiple variables at the same time in a single line of code

#name = "Bro"
#age = 21
#attractive = True

#name, age, attractive = "Bro", 21, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = 30
#Patrick = 30
#Sandy = 30
#Squidward = 30

#Spongebob = Patrick = Sandy = Squidward = 30 

#print(Spongebob)
#print(Patrick)
#print(Sandy)
#print(Squidward)

                                                                                                                                            #useful string methods in Python

#name = "judson"

#print(len(name)) =============== print the length of a string
#print(name.find("d")) =========== find a character within a string
#print(name.capitalize()) ========= capitalizes the first letter in the string
#print(name.upper()) =========== capitalizes everything in the string 
#print(name.lower()) ========== decapitalizes everything in the string
#print(name.isdigit()) ====== will return true or false if the string is digits
#print(name.isalpha()) ======== check if string contains only alphabetical letters
#print(name.count("o")) =========== counts how many characters are in the string -- takes at least on argument (specify character)
#print(name.replace("o", "a")) ============ takes the arg (character) you provide and changes it to the second arg (replacement character) you desire
#print(name*8) ========== multiplies the string (name) by the number you put in--NOT multiplying the print command as if it was a loop
                                                                                                                                        #typecasting in Python
                                                                                                                                        #typecasting is the ability to convert the data type of a value to another data type
#x = 1 #int
#y = 2.0 #float
#z = "3" #str {cannnot usually perform math on strings}

#print(x)
#print(int(y)) ============ convert y into an integer from a float so that it displays 2 instead of 2.0 {NOT PERMANENT}
#print(z)

#OR

#y = int(y) ============== now y is hardcoded into an integer

#because you cannot do math on a string, typing print(z*3) would output 333
#BUT
#z = int(z)
#print(z*3) = output 9 {because you hardcoded it}

#print(x)
#print(y)
#print(z)

#NOW lets convert x,y,z into floating point numbers

#x = 1
#y = 2.0
#z = "3"

#x = float(x)
#y = float(y)
# = float(z)

#print(x)
#print(y)
#print(z)

                                                                                                                                    #stringcasting integers

#x = 1
#y = 2.0
#z = "3"

#print("X is "+str(x))
#print("Y is "+str(y))
#print("Z is "+str(z))

                                                                                                                                    #HOW TO ACCEPT USER INPUT IN PYTHON

#name = input("What's your name?: ")
#age = int(input("How old are you?"))
#height = float(input("How tall are you?"))

#when we accept user input, it is always in string data type
#if we accept numbers as user input, we need to cast it as either INTEGER or FLOAT datatype

#print("Hello, " +name)
#print("You are "+str(age)+ "years old.")
#print("You are "+str(height) + "cm tall")

#BASICALLY, when accepting user input that includes numbers, we accept STRING DATATYPE, cast it to INT datatype so we can treat it as a NUMBER not a CHARACTER
#but when we want to display it again, we concactenate it back to a STRING that we can use it and display all of the strings together

#HOWEVER, if user inputs a float, we run into an error, so that is where floats come in 
#you need to convert from float to string to render a proper output

                                                                                                                                    #MATH FUNCTIONS

#import math

#pi = 3.14

#print(round(pi))========rounds up a float
#print(math.ciel(pi))=======rounds up to the nearest whole integer
#print(math.floor(pi))======rounds down to the nearest whole integer
#print(abs(pi))=====absolute value (ABS) tells you how far a number is away from 0; entering a positive number gives you a negative number and vice versa
#print(pow(pi,2)=======rounds to a power (2 arguments: number + desired power)
#print (math.sqrt(pi))==========founds the square root

#x = 1
#y = 2 
#z = 3

#print(max(1,2,3))===========finds the largest value between any given numbers {x,y,z}
#print(max(1,2,3))===========finds the smallest value between any given numbers {x,y,z}

                                                                                                                                    #COMPARISON OPERATORS

# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal

                                                                                                                                    #TRY AND EXCEPT
#you surround a dangerous section of code with TRY and ACCEPT
#if the code in TRY works, the EXCEPT is skipped
#if the code in TRY fails, it jumps to the EXCEPT section

                                                                                                                                    #DEF
#Def doesn't do anything, but it remembers. "These two lines what you'd like to run when you invoke 'thing'."
#def thing():
    #print ('Hello')
    #print ('Quindale Dingle')

#^^^^^^This is the definition of a function.^^^^^^#

#thing()
#print('MHM')
#thing()

#^^^^^^This is the invocation of a function. The output is: 
#Hello
#Quindale Dingle
#MHM
#Hello
#Quindale Dingle

#^^^^^Hello / Quindale Dingle = thing() one
#^^^^^MHM = the print statment in the invocation
#^^^^^Hello / Quindale Dingle = thng() two

                                                                                                                                    #<------- THESE REUSABLE PIECES OF CODE ARE CALLED 'FUNCTIONS

                                                                                                                                   #TWO TYPES OF FUNCTIONS IN PYTHON -- BUILT-IN FUCTIONS, AND FUNCTIONS {CUSTOM FUNCTIONS}
                                                                                                                    #Def functions allow us to create new reserved words of our own making that extend the Python language after we define the function.

