# Reading 2

source - https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932

### Unit Test
Unit tests are some pieces of code to exercise the input, the output
and the behaviour of your code.

Arrange - Organize the data needed to execute that piece of code.
Act - execute the code being tested.
Assert - Check the output results.

The Cycle - Write a unit test and make it fail. Then write the
feature and make it pass. Finally, refactor the code. 

### What does the if __name__ == “__main__”: do?
source - https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

Python interpreter reads source file and define few special variables/global variables. 
If the python interpreter is running that module (the source file) as the main 
program, it sets the special __name__ variable to have a value “__main__”. If this 
file is being imported from another module, __name__ will be set to the module’s name.

### Recursion
source - https://www.geeksforgeeks.org/recursion/
The process in which a function calls itself directly or indirectly is called recursion and 
the corresponding function is called as recursive function.
(A function that is called within a function.)

[BACK TO MAIN](./README.md)
