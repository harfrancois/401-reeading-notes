# Reading 3

### Reading and Writing Files in Python

source - https://realpython.com/read-write-files-python/

Using the function open() will allow you to open files.
when done, the file must be closed properly.

    file = open('dog_breeds.txt')

The first way to close a file is to use the try-finally block.

    reader = open('dog_breeds.txt')
    try:
    # Further file processing goes here
    finally:
    reader.close()
The second way to close a file is to use the with statement.

    with open('dog_breeds.txt') as reader:
    # Further file processing goes here

'r'	Open for reading. open('abc.txt', 'r')
'w'	Open for writing. open('abc.txt', 'w')
'rb' or 'wb'	Open in binary mode. open('abc.txt', 'rb')

.read(size=-1) Reads file based on bytes size
.readline(size=-1) Reads most size number of characters from the line.
.readlines() This reads the remaining lines from the file object 
and returns them as a list.

Iterating over each line in a file.

         with open('dog_breeds.txt', 'r') as reader:
             # Read and print the entire file line by line
             line = reader.readline()
             while line != '':  # The EOF char is an empty string
                 print(line, end='')
                 line = reader.readline()

.write(string)	This writes the string to the file.
.writelines(seq)	This writes the sequence to the file.

    with open('dog_breeds.txt', 'r') as reader:
    with open('dog_breeds_reversed.txt', 'w') as writer:

### exception error
source - https://realpython.com/python-exceptions/

This type of error occurs whenever syntactically correct Python code results in an error.
Raising an Exception -  Raise allows you to throw an exception at any time.
The AssertionError Exception - Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

The try and except
In the try clause, all statements are executed until an exception is encountered.
Except is used to catch and handle the exception(s) that are encountered in the try clause.
    try:
        linux_interaction()
    except AssertionError as error:
        print(error)
        print('The linux_interaction() function was not executed')


The else Clause
Else lets you code sections that should run only when no exceptions are encountered in the try clause.
    
    try:
    linux_interaction()
     except AssertionError as error:
    print(error)
    else:
    print('Executing the else clause.')

Cleaning Up After Using finally
Finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.

    try:
        linux_interaction()
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')

[BACK TO MAIN](./README.md)
