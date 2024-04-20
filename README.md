# 1: Numpy | Array creation
1. Array creation using List: Arrays are used to store multiple values in one single variable.Python does not have built-in support for Arrays, but Python lists can be used instead.

2. Array creation using array functions: array(data type, value list)function is used to create an array with data type and value list specified in its arguments.

3. Array creation using numpy methods: NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.
+ numpy.empty(shape, dtype = float, order = ‘C’) -> Return a new array of given shape and type, with random values.
+ numpy.zeros(shape, dtype = None, order = ‘C’) -> Return a new array of given shape and type, with zeros.

=> Methods for array creation in Numpy: https://www.geeksforgeeks.org/numpy-array-creation/?ref=lbp