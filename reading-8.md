# reading 8
source - https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# Lists Comprehensions
List comprehension methods are an elegant way to create and manage lists. 
In Python, list comprehensions are a more compact way of creating lists. 
More flexible than for loops, list comprehension is usually faster than other methods.

### range()

    # construct a basic list using range() and list comprehensions
    # syntax
    # [ expression for item in list ]
    digits = [x for x in range(10)]
    
    print(digits)
    Output
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Let’s break down this python example by starting with the first ‘x’. This is our expression. It doesn’t 
do anything because we’re simply recording the number. The second ‘x’ represents each item in the list 
created by the range() method.

### Using Loops and List Comprehension in Python

     create a list using a for loop
    squares = []
    
    for x in range(10):
        # raise x to the power of 2
        squares.append(x**2)
    
    print(squares)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

refactored

    # create a list using list comprehension
    squares = [x**2 for x in range(10)]

    print(squares)


### Multiplication with list comprehensions

    # create a list with list comprehensions
    multiples_of_three = [ x*3 for x in range(10) ]
    
    print(multiples_of_three)
    Output
    
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

### Separating the characters in a string

    # use list comprehension to print the letters in a string
    letters = [ letter for letter in "20,000 Leagues Under The Sea"]
    
    print(letters)
    Output
    
    ['2', '0', ',', '0', '0', '0', ' ', 'L', 'e', 'a', 'g', 'u', 'e', 's',
    ' ', 'U', 'n', 'd', 'e', 'r', ' ', 'T', 'h', 'e', ' ', 'S', 'e', 'a']

### Lower/Upper case converter using Python

Making use of Python’s lower() and upper() methods

     lower_case = [ letter.lower() for letter in ['A','B','C'] ]
    upper_case = [ letter.upper() for letter in ['a','b','c'] ]
    
    print(lower_case, upper_case)   
    ['a', 'b', 'c'] ['A', 'B', 'C']

### Identify numbers in a string using the isdigit() method

    # user data entered as name and phone number
    user_data = "Elvis Presley 987-654-3210"
    phone_number = [ x for x in user_data if x.isdigit()]
    
    print(phone_number)
    Output
    
    ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

### Adding arguments to list comprehension

    # list comprehension with functions
    # create a function that returns a number doubled
    def double(x):
        return x*2
    
    nums = [double(x) for x in range(1,10)]
    print(nums)
    Output
    
    [2, 4, 6, 8, 10, 12, 14, 16, 18]

    # add a filter so we only double even numbers
    even_nums = [double(x) for x in range(1,10) if x%2 == 0]
    print(even_nums)
    Output
    
    [4, 8, 12, 16]

Additional arguments can be added to create more complex logic.

    nums = [x+y for x in [1,2,3] for y in [10,20,30]]
    print(nums)
    Output
    
    [11, 21, 31, 12, 22, 32, 13, 23, 33]