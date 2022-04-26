# reading 7
source - https://realpython.com/python-scope-legb-rule/#understanding-scope

## Scope

n programming, the scope of a name defines the area of a program in which you can unambiguously access 
that name, such as variables, functions, objects, and so on. 

Global scope: The names that you define in this scope are available to all your code.

Local scope: The names that you define in this scope are only available or visible to the code within the scope.

The letters in LEGB stand for Local, Enclosing, Global, and Built-in.The LEGB rule is a kind of name lookup
procedure, which determines the order in which Python looks up names.

Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope
contains the names that you define inside the function. These names will only be visible from the code of the
function. It’s created at function call, not at function definition, so you’ll have as many different local scopes
as function calls. This is true even if you call the same function multiple times, or recursively. Each call will
result in a new local scope being created.

Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an
inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope
contains the names that you define in the enclosing function. The names in the enclosing scope are visible from
the code of the inner and enclosing functions.

Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains
all of the names that you define at the top level of a program or a module. Names in this Python scope are visible
from everywhere in your code.

Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive
session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into
Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by
Python when you run a program or script.

A comprehension is a compact way to process all or part of the elements in a collection or sequence.Comprehensions
consist of a pair of brackets ([]) or curly braces ({}) containing an expression, followed by one or more for
clauses and then zero or one if clause per for clause.

The exception variable is a variable that holds a reference to the exception raised by a try statement.
In Python 3.x, such variables are local to the except block and are forgotten when the block ends.

he class local scope isn’t created at call time, but at execution time. Each class object has its own.
__dict__ attribute that holds the class scope or namespace where all the class attributes live.

In Python, globals() is a built-in function that returns a reference to the current global scope or namespace
dictionary. This dictionary always stores the names of the current module. This means that if you call globals()
in a given module, then you’ll get a dictionary containing all the names that you’ve defined in that module, right
before the call to globals().

Python scope and namespaces is locals(). This function updates and returns a dictionary that holds a copy of the
current state of the local Python scope or namespace. When you call locals() in a function block, you get all the
names assigned in the local or function scope up to the point where you call locals().

vars() is a Python built-in function that returns the .__dict__ attribute of a module, class, instance, or any
other object which has a dictionary attribute. Remember that .__dict__ is a special dictionary that Python
uses to implement namespaces.

dir() without arguments to get the list of names in the current Python scope. If you call dir() with an argument,
then the function attempts to return a list of valid attributes for that object.

The scope of a variable or name defines its visibility throughout your code. In Python, scope is implemented as
either a Local, Enclosing, Global, or Built-in scope. When you use a variable or name, Python searches these scopes
sequentially to resolve it. If the name isn’t found, then you’ll get an error. This is the general mechanism that
Python uses for name resolution and is known as the LEGB rule.