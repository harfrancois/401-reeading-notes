# Reading 5
source - https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d
## link List

A linked list is made up of a series of nodes, which are the elements of the list.
The end of the list isn’t a node, but rather a node that points to null, or an empty value.
A single node is also pretty simple. It has just two parts: data, or the information that 
the node contains, and a reference to the next node.

Singly linked lists is a single track that we can traverse the list in; we start at the 
head node, and traverse from the root until the last node, which will end at an empty null value.

doubly linked list, because there are two references contained within each node: a reference to 
the next node, as well as the previous node.

A circular linked list doesn’t end with a node pointing to a null value. Instead, it has a node 
that acts as the tail of the list and the node after the tail node is the beginning of the list.

First, we find the head node of the linked list.
Next, we’ll make our new node, and set its pointer to the current first node of the list.
Lastly, we rearrange our head node’s pointer to point at our new node. 

### Resources 
Link list - https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html

Big O - https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/big_oh.html