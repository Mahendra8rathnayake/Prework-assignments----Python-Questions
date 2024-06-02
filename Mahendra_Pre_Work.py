# Question 1:Write a function to print "hello_USERNAME!" USERNAME is the input of the function
def hello_USERNAME(username):
    """Display a my arival to new begining of Pyhton world."""
    print("Hello! My name is Mahendra Please accept me to " + username.title() + "!")

hello_USERNAME('python world')

# Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing#
# Making a empty list to append odd numbers: 
even_numbers = []
odd_numbers = []

for number in range(1, 100):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Odd Numbers: ", odd_numbers)    
       
# Question 3: Please write a Python function, max_num_in_list to return the max number of a given list:
# Find maximum value in list

def find_max(number_list):
    max_valu = number_list[0]
    for m in range(len(number_list)):
        if number_list[m] >= max_valu:
            max_valu = number_list[m]
    return max_valu

age = [5, 7, 11, 9 , 35, 22, 49, 65, 3, 101, 88, 8, 73]
print("Maximum age of this list is: ", find_max(age))

# Question 4: Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400
#  The return should be boolean Type (true/false)

def is_leap(year):
    # leap = False
    if year % 4 == 0:
        leap = True
        if year % 100== 0:
            leap = False
        elif year % 400 == 0:
            leap = True

        else:
            leap = False
        
        return leap

    year = int(input())  
print(is_leap(2024))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers

def is_consecutive(a_list):
    # consecutive  = False
    if a_list % 2 == 25:
        consecutive = True
        if a_list % 5 == 5:
            consecutive = False
        elif a_list % 4 == 8100:
            consecutive = True

        else:
            consecutive = False
        
        return consecutive

    a_list = int(input())  
print(is_consecutive(5))

