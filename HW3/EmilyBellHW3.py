# 1) Power of a Number: Please write a function that takes a number x and a power y and outputs the number to that power, x^y
def power(x, y):
    return x ** y
result1 = power(7, 2)  
print(result1)  #ouputs 49

# 2) Write a function that takes in a list of number and returns the minimum and maximum values as a tuple.
def min_and_max(numbers):
    return(min(numbers), max(numbers))

numbers = [2, 6, 8, 3, 6, 5]
result = min_and_max(numbers)
print(result) #(2, 8)

# 3) Leap Year Write a function that takes in a year and returns True if it is a leap year and False is it isn’t. A year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400.
def is_it_a_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
print(is_it_a_leap_year(2000))  # True 
print(is_it_a_leap_year(1900))  # False 
print(is_it_a_leap_year(2004))  # True
print(is_it_a_leap_year(2100))  # False

# 4) Write a function that takes in a person’s weight in kilograms and their height in meters and returns their BMI.
def what_is_BMI(height, weight):
    if height == 0:
        return "nobody is 0m tall!"
    return (weight/(height**2))
weight = 70  # in kilograms
height = 1.8  # in meters
print(what_is_BMI(weight, height))

# 5) Write a function that takes in an integer and rotates all its digits to the right by one position i.e. the last digit becomes the first digit, the first digit becomes the second digit etc. You may not cast to the number to a string.
def rotate_digits_right(n):
    #single-digit numbers and zero
    if n < 10 and n >= 0:
        return n

    # Find last digit
    last_digit = n % 10

    # Remove last digit
    n //= 10

    # Determine the order of magnitude of the number
    magnitude = 1
    temp = n
    while temp > 0:
        temp //= 10
        magnitude *= 10

    # Rotate the last digit to the front and combine
    rotated = last_digit * magnitude + n

    return rotated

number = 1234
print(rotate_digits_right(number))  # Outputs 4123

# 6) For both minimum and maximum, write one function to manually find that value using a for loop and another to manually find it using a while loop. You may not use min() or max(). In total you should have written 4 functions
# minimum value using a while loop
def find_min_while(numbers):
    if not numbers:
        return None  # Return None if list is empty

    min_val = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] < min_val:
            min_val = numbers[index]
        index += 1
    return min_val

#maximum value using a while loop
def find_max_while(numbers):
    if not numbers:
        return None  # Return None if list is empty

    max_val = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] > max_val:
            max_val = numbers[index]
        index += 1
    return max_val

# minimum value using for loop
def find_min_for(numbers):
    if not numbers:
        return None  # Return None if list is empty

    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

#maximum value using for loop
def find_max_for(numbers):
    if not numbers:
        return None  # Return None if list is empty

    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_min_for(numbers))  # Outputs: 1
print(find_max_for(numbers))  # Outputs: 9
print(find_min_while(numbers))  # Outputs: 1
print(find_max_while(numbers))  # Outputs: 9

# 7) Write a function in python which takes in a string and outputs the number of vowels. Consider only a,e,i,o,u to be vowels and do not forget about capital letters.
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

text = "UC Berkeley"
print(count_vowels(text))  # outputs 4

# 8) Write a function that takes in an integer and returns the sum of the digits (the digital root).
def digital_root(n):
    while n >= 10:  
        sum_of_digits = 0
        while n > 0:
            sum_of_digits += n % 10  # Add last number
            n //= 10  # Remove last number
        n = sum_of_digits  # Set n to the sum of its digits for the next iteration
    return n

# Test the function
print(digital_root(955))  # 6 



