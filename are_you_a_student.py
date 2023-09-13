# let's create a function that acquires a user's name, age, student status, then print dependent statements (welcome messages)
def main():
    firstname = "Steve" 
    lastname = "Jenkins"
    age = 22
    is_student = True

# time to print the welcome message

    print("Hi there, " + firstname + "!")
    print("Actually, would you rather that I called you Mr. " + lastname + "?")

# print the user's age

    print("Clearly, you are " + str(age) + ". ")

# check whether or not the user is a student

    if is_student:
        print("You are a student! I wonder what year you are or what university you attend?")
    else:
        print("Not a student, I see? I wonder if you graduated university already--or perhaps you've got other plans.")

# call the main function?

main()