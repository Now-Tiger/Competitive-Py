# Hash data structure :
A hash is a value that has a fixed length, and it is generated using a mathematical formula. Hash values are used in data compression, cryptology, etc. In data indexing, hash values are used because they have fixed length size regardless of the values that were used to generate them. It makes hash values to occupy minimal space compared to other values of varying lengths.

A hash function employs a mathematical algorithm to convert the key into a hash. A collision occurs when a hash function produces the same hash value for more than one key.

## Hash Table :
A __HASH TABLE__ is a data structure that stores values using a pair of keys and values. Each value is assigned a unique key that is generated using a hash function.

The name of the key is used to access its associated value. This makes searching for values in a hash table very fast, irrespective of the number of items in the hash table.

Hash functions

- For example, if we want to store employee records, and each employee is uniquely identified using an employee number.

- We can use the employee number as the key and assign the employee data as the value.

- The above approach will require extra free space of the order of (m * n2) where the variable m is the size of the array, and the variable n is the number of digits for the employee number. This approach introduces a storage space problem.

- A hash function solves the above problem by getting the employee number and using it to generate a hash integer value, fixed digits, and optimizing storage space. The purpose of a hash function is to create a key that will be used to reference the value that we want to store. The function accepts the value to be saved then uses an algorithm to calculate the value of the key.

The following is an example of a simple hash function : 

```  h(k) = k1 % m  ```

__HERE__

- h(k) is the hash function that accepts a parameter k. The parameter k is the value that we want to calculate the key for.
- k1 % m is the algorithm for our hash function where k1 is the value we want to store, and m is the size of the list. We use the modulus operator to calculate the key.

## Qualities of a good hash function :

A good hash function should have the following qualities.

- The formula for generating the hash should use the data’s value to be stored in the algorithm.
- The hash function should generate unique hash values even for input data that has the same amount.
- The function should minimize the number of collisions. Collisions occur when the same value is generated for more than one value.
- The values must be distributed consistently across the whole possible hashes.

## Collision : 

A collision occurs when the algorithm generates the same hash for more than one value.

Let’s look at an example.

Suppose we have the following list of values

__[3, 2, 9, 11, 7]__

Let’s assume that the size of the hash table is 7, and we will use the formula (k1 % m) where m is the size of the hash table.

The following table shows the hash values that will be generated.

Key      |    Hash Algorithm (k1 % m) |  Hash Value |
---------|----------------------------|--------------
3	       |        3 % 7               |     3       
2	       |        3 % 7	              |     2       
9	       |        3 % 7               |	    2
11       |        3 % 7               |	    4
7	       |        3 % 7               |	    0

- As we can see from the above results, the values 2 and 9 have the same hash value, and we cannot store more than one value at each position.

- The given problem can be solved by either using chaining or probing. The following sections discuss chaining and probing in detail.

(_more to come_)
