# reading 6
source - https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python

    import random
    print random.randint(0, 5)
    This will output either 1, 2, 3, 4 or 5.

Random
If you want a larger number, you can multiply it.

For example, a random number between 0 and 100:

    import random
    random.random() * 100
Choice
Generate a random value from the sequence sequence.

    random.choice( ['red', 'black', 'green'] ).
The choice function can often be used for choosing a random element from a list.

    import random
    myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
    random.choice(myList)

Shuffle
The shuffle function, shuffles the elements in list in place, so they are in a random order.

    from random import shuffle
    x = [[i] for i in range(10)]
    shuffle(x)
    Output:
    # print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]

Randrange
Generate a randomly selected element from range(start, stop, step)

    random.randrange(start, stop[, step])
    import random
    for i in range(3):
        print random.randrange(0, 101, 5)
