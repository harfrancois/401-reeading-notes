# Hashtable

source -

Hashtables are a data structure that utilize key value pairs. This means every Node or bucket has
both a key, and a value.

    ["Greenwood:98103", "Downtown:98101", "Alki Beach:98116", "Bainbridge Island:98110", ...]

Hash - A hash is the result of some algorithm taking an incoming string and converting it into a value that could be
used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the
array.

Buckets - A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An
index could potentially contain multiple key/value pairs if a collision occurs.

Collisions - A collision is what happens when more than one key gets hashed to the same location of the hashtable.

The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value.
This is done through what we call a hash. A hash is the ability to encode the key that will eventually map to a
specific location in the data structure that we can look at directly to retrieve the value.

Creating a Hash
A hashtable traditionally is created from an array. I always like the size 1024. this is important for index placement.
After you have created your array of the appropriate size, do some sort of logic to turn that “key” into a numeric
number value. Here is a possible suggestion:

Add or multiply all the ASCII values together.
Multiply it by a prime number such as 599.
Use modulo to get the remainder of the result, when divided by the total size of the array.
Insert into the array at that index.

Example:

Key = "Cat"
Value = "Josie"

67 + 97 + 116 = 280

280 * 599 = 69648

69648 % 1024 = 16

Key gets placed in index of 16.