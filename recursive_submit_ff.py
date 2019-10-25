###################
#### FACTORIAL ####
###################

# Construct a factorial function for non-negative integers.
gimme_number =-1000

# The actual function itself.
def factorial(confirmed_number):
    if confirmed_number == 1:
        print("\n1! is equal to 1.")
    elif confirmed_number == 0:
        confirmed_number = 1
        print("\n0! is equal to 1.")
    else:
        j=1
        slowly_multiply = 1
        while j <= confirmed_number:
            slowly_multiply *= j
            j+=1
        print(f"\n{confirmed_number}! is equal to equal to { format(slowly_multiply, ',d')}.\n")

def welcome_me():
    global gimme_number
    print("This is a factorial and a Fibonacci exercise.\nWe will do the factorial exercise first.\nPlease give me a non-negative integer.")
    gimme_number=input("")

confirmed_number = 10000

def verifying_conditions(gimme_number):
    global confirmed_number
    while not gimme_number.isdigit() or int( gimme_number ) < 0:
        print("This is not a non-negative integer input. Try again.")
        gimme_number = input("")

    confirmed_number = int(gimme_number)

welcome_me()
verifying_conditions(gimme_number)
factorial(confirmed_number)

###################
#### FIBONACCI ####
###################

# Fibonacci numbers are 0,1,1,2,3,5,8,13,21,...
# Starting with index 0.
# Starting from the second term, each term is sum of the two previous terms.

give_me_fibonacci = -1000

previous_previous_term = 0
previous_term = 1
new_term = 0

def welcome_fibonacci():
    global give_me_fibonacci
    print("Now let's do the Fibonacci exercise.\nPlease submit an index (n), a non-negative integer input.\nAnd we will display the nth term of the famous Fibonacci sequence.\n")
    give_me_fibonacci = input("")


def calculate_fibonacci(confirmed_fibonacci):
    if confirmed_fibonacci == 0:
        print("The 0th term of the Fibonacci is 0.")
    elif confirmed_fibonacci == 1:
        print("The 1st term of the Fibonacci is 1.")

    else:
        global previous_previous_term
        global previous_term
        global new_term

        i = confirmed_fibonacci - 1

        print(f"\nThe first {confirmed_fibonacci+1} Fibonacci terms are {previous_previous_term}, {previous_term}, ",end="")

        while i >= 2 and i < confirmed_fibonacci:

            new_term = previous_previous_term + previous_term
            print(f"{new_term}, ", end="")
            i -= 1
            previous_previous_term = previous_term
            previous_term = new_term

        # calculate the final sum.
        new_term = previous_previous_term + previous_term
        print(f"{new_term}.\n\nAnd the {confirmed_fibonacci}(th) Fibonacci term (starting from the 0th index) is {new_term}.\n")

def verifying_conditionss(give_me_fibonacci):
    global confirmed_fibonacci
    while not give_me_fibonacci.isdigit() or int( give_me_fibonacci ) < -1:
        print("This is not a non-negative integer input. Try again.")
        give_me_fibonacci = input("")

    confirmed_fibonacci = int(give_me_fibonacci)
            

welcome_fibonacci()
verifying_conditionss(give_me_fibonacci)
calculate_fibonacci(confirmed_fibonacci)

"""
git clone git@github.com:nahiphog/challenge-full-stack-web-development-bootcamp-with-python-recursive-challenges.git
"""