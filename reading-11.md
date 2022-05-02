# Numpy
source - https://www.dataquest.io/blog/numpy-tutorial-python/

NumPy is a commonly used Python data analysis package.

### Lists Of Lists for CSV Data

Before using NumPy, we’ll first try to work with the data using Python and the csv package. We can read in the file 
using the csv.reader object, which will allow us to read in and split up all the content from the ssv file.

- Import the csv library.
- Open the winequality-red.csv file.
- With the file open, create a new csv.reader object.
- Pass in the keyword argument delimiter=";" to make sure that the records are split up on the semicolon character 
instead of the default comma character.
- Call the list type to get all the rows from the file.
- Assign the result to wines.

A 2-dimensional array is also known as a matrix, and is something you should be familiar with. In fact, it’s just a 
different way of thinking about a list of lists. A matrix has rows and columns. By specifying a row number and a 
column number, we’re able to extract an element from a matrix.

A 1-dimensional array only needs a single index to retrieve an element. Each row and column in a 2-dimensional 
array is a 1-dimensional array. Just like a list of lists is analogous to a 2-dimensional array, a single list
is analogous to a 1-dimensional array.

N-Dimensional NumPy Arrays are arrays with dimensions greater than 3.

float — numeric floating point data.
int — integer data.
string — character data.
object — Python objects.

If you do any of the basic mathematical operations (/, *, -, +, ^) with an array and a value, it will apply
the operation to each of the elements in the array.

NumPy performs broadcasting to try to match up elements. Essentially, broadcasting involves a few steps:
The last dimension of each array is compared.
If the dimension lengths are equal, or one of the dimensions is of length 1, then we keep going.
If the dimension lengths aren’t equal, and none of the dimensions have length 1, then there’s an error.
Continue checking dimensions until the shortest array is out of dimensions.

NumPy makes it possible to test to see if rows match certain values using mathematical comparison operations
like <, >, >=, <=, and ==.

We can change the shape of arrays while still preserving all of their elements. This often can make it easier to
access array elements. The simplest reshaping is to flip the axes, so rows become columns, and vice versa.

