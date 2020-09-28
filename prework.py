# Question 1 - Write a function to print "Hello_USERNAME"

def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name(' Hetal')


# Question 2 - Print first 100 odd numbers in Python.
def odd_numbers():
    for i in range(0, 101, 2):
        print(i)

# Question 3 - Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = max(a_list)
    return max


# Question 4 - Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
        if a_year % 4 == 0 and a_year % 100 != 0:
            print(f'{a_year} is a leap year')
        elif  a_year % 400 == 0:
            print(f'{a_year} is a leap year')
        else:
            a_year = False
            print(f'{a_year}')

        # question 4 1.b solution

            def is_leap(a_year):
                if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
                    print(True)
                else:
                    print(False)
            is_leap_year(2019)


#Question 5  Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) -1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
                status = False
                print(status)
