
# ----------------------------------------------------
# Ch 4 Numpy basics: arrays and vectorized computation
# ----------------------------------------------------

import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

data

data * 10

data + data


# -----------------------------------------------------
# 4.1 The Numpy ndarray: A multidomesional array object
# -----------------------------------------------------

# ndarray shape and data type

data.shape

data.dtype


# Creating ndarrays
# -----------------

# array() accepts any sequence-like object including other arrays

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

arr1

# nested sequences create multi-dimensional arrays

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr2 = np.array(data1)

arr2

# ndim and shape attributes

arr2.ndim

arr2.shape

# inferring data types

arr1.dtype

arr2.dtype

# other functions for creating arrays

np.zeros(10)

np.zeros((3, 6))

# below, not safe to assume return 0's

np.empty((2, 3, 2))

# range function

np.arange(15)

# default data type for these functions in float64

# array creation functions: 
# array, asarray, arange, ones, ones_like,
# empty, empty_like, full, full_like,
# eye, identity


# Data types for ndarrays
# -----------------------

# dtype is metadata

arr1 = np.array([1, 2, 3], dtype=np.float64)

arr2 = np.array([1, 2, 3], dtype=np.int32)

arr1.dtype

arr2.dtype


# NumPy data types
# int8, uint8, int16, utin16, int32, uint32, int64, uint64, 
# float16, float32, float64, float128, comnplext64, copmlex128,
# complex256, bool, object, string, unicode

arr = np.array([1, 2, 3, 4, 5])

arr.dtype

arr

float_arr = arr.astype(np.float64)

float_arr

float_arr.dtype

# example of truncating with float to int

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])

arr

arr.astype(np.int32)

# converting strings to numerics
# caution: _string type is fixed size and may trucate input

numeric_strings = np.array(["1.25", "-9.6", "42"], dtype=np.string_)

numeric_strings.astype(float)

# using another array's dtype

int_array = np.arange(10)

int_array

calibers = np.array([.22, 270, .357, .44, 50], dtype= np.float64)

int_array.astype(calibers.dtype)

# using short hand type code strings

zeros_uint32 = np.zeros(8, dtype="u4")

zeros_uint32

# Note: astype *always* creates a new copy


# Arithmetic with NubPy arrays
# ----------------------------

# vectorization via batch operations

arr = np.array([[1., 2., 3.,], [4., 5., 6.,]])

arr

arr * arr

arr - arr

# operations using scalars

1 / arr


arr ** 2

# Comparisons > or < yield booleans


arr2 = np.array([[0., 4., 1.,], [7., 2., 12.,]])

arr2 > arr

# Broadcasting - operations between differently
# sized arrays

# Basic indexing and slicing
# --------------------------

# Indexing on one dimensional arrays is similar to 
# slicing lists

arr = np.arange(10)

arr

arr[5]

arr[5:8]

arr[5:8] = 12 # here, we are broadcasting 12s in arr

arr


### array slices are VIEWS of the original source arrays - see below
### things tend to work on the original arrays rather than copies

arr_slice = arr[5:8]

arr_slice

# Note this step

arr_slice[1] = 12345

arr


arr_slice[:] = 64 # this is called a "bare" slice

arr

### Note, if you want to work on copies, then create them

arr[5:8].copy()

# in two dimensional arrays and higher, indexes are one-dimensional arrays

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d

arr2d[2]

# consequently, elements can be accessed recursively
# or alternatively, you can use csv list of indices. E.g., 

arr2d[0][2]

arr2d[0, 2]

# Think of axis 0 as rows and axis 1 as columns

# In multi-dimensional arrays, omitting later indices, uses earlier indices

arr3d = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr3d

arr3d[0]

# Assigning scalars and arrays to arr3d[0]

old_values = arr3d[0].copy()

arr3d[0] = 42

arr3d

arr3d[0] = old_values

arr3d

##

arr3d[1, 0] # gives all values with indices start with (1, 0)

# This is the same as the following individual steps

x = arr3d[1]

x

x[0]

# all of these operations return VIEWS
# multi-dimensional indexing syntax from NumPy
# does not work in regular Python, e.g., lists-of-lists

# Indexing with slices
# --------------------

# one-dimensional slicing is similar to lists

arr

arr[1:6]

# two dimensional slicing is a bit different

arr2d

arr2d[:2] # slices along the 0 axis, 
          # slices along the first two rows of arr2d
          
# passing multiple slices

arr2d[:2, 1:]

# mixing indices and slice to get lower dimensions
# here, we select second row but only 1st two columns

lower_dim_slice = arr2d[1, :2]

lower_dim_slice

lower_dim_slice.shape

# more subsample slicing

arr2d[:2, 2]

# the colon by itself means take the entire axis

arr2d[:, :1]

arr2d

arr2d[:2, 1:]


arr2d[:2, 1:] = 0

arr2d



# Boolean indexing
# ----------------


names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])

data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

names

data 

names == "Bob"

# using a Boolean array for indexing
# it has to have the same length as the axis its indexing

data[names == "Bob"]

# more complex

data[names == "Bob", 1:]


data[names == "Bob", 1]


# selecting everything but Bob either != or ~

names

names != "Bob"

~(names == "Bob")

# using as an index

data

data[~(names == "Bob")]

# ~ use to invert Boolean array

cond = names == "Bob"

cond

~cond

data[~cond]

# combining multiple Boolean conditions

names

data

mask = (names == "Bob") | (names == "Will") # 'and' and 'or' don't work, use '&' and '|'

mask

data[mask]

# NOTE - selecting data with Boolean index and assigning to new variable
# ALWAYS creates a copy of data, even if unchanged


# 
data[data < 0]  # returns values that meet the condition

# then to assign those values to 0
data[data < 0]  = 0

data

# here setting entire rows or columns 
# to a value using one-dimensional array

data[names != "Joe"] = 7

data


# Fancy indexing
# --------------

# Transposing arraus and Swapping Axes
# ------------------------------------

# -----------------------------------------------------
# 4.2 Pseudorandom Number Generation
# -----------------------------------------------------

# ----------------------------------------------------------
# 4.3 Universal Functions: Fast Element-wise Array Functions
# ----------------------------------------------------------

# --------------------------------------------------------------
# 4.4 Array-oriented Programming with Arrays
# --------------------------------------------------------------

# Expressing conditional logic as Array Operations
# ------------------------------------------------

# Mathematic and statistical methods
# ----------------------------------

# Methods for Boolean arrays
# --------------------------

# Sorting
# -------

# Unique and other set logic
# --------------------------


# --------------------------------------------------------------
# 4.5 File Inout and Output with Arrays
# --------------------------------------------------------------



# --------------------------------------------------------------
# 4.6 Linear Algebra
# --------------------------------------------------------------


# --------------------------------------------------------------
# 4.7 Linear Algebra
# --------------------------------------------------------------

# --------------------------------------------------------------
# 4.7 Example: Random walks
# --------------------------------------------------------------

# Simulating many random walks at once
# ------------------------------------


# --------------------------------------------------------------
# 4.8 Conclusion
# --------------------------------------------------------------
































