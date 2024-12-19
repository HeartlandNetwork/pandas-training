
# ----------------------------------------------------
# Ch 6 Data loading, storage and file formats
# ----------------------------------------------------

# Categories of input and output
# reading text files and other more efficient on-disk formats
# load data from databases
# interacting with network sources like web APIs



# ----------------------------------------------------
# 6.1 Reading and writing data in text format
# ----------------------------------------------------

# pandas.read_csv most frequently used method
# Text and binary data loading functions in pandas
# read_csv, read_fwf, read_clipboard, read_excel
# read_hdf, read_html, read_json, read_feather,
# read_orc, read_parquet, read_pickle, read_sas,
# read_spss, read_sql, read_sql_table, read_stata,
# read_xml

# option arguments - general categories as follows
# Indexing, Type inference and data conversion
# Date and time parsing, Iterating, 
# Unclear data issues

# pandas.read_csv has about 50 optional arguments!!
# be sure to checkout pandas documentation


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# loading a comma delimited file

df = pd.read_csv("examples/ex1.csv")

df

# reading a file without a header

pd.read_csv("examples/ex2.csv", header=None)


# specifying the header separately

pd.read_csv("examples/ex2.csv", names=["a", "b", "c", "d", "message"])


# Making the message column the indexed column


names = ["a", "b", "c", "d", "message"]

names

pd.read_csv("examples/ex2.csv", names=names, index_col="message")

# Forming hierarchical index from multiple columns

parsed = pd.read_csv("examples/csv_mindex.csv", index_col=["key1", "key2"])

parsed

# examples/ex3.txt - a table with variable whitespace. 
# No fixed delimiter - used "\s+"

result = pd.read_csv("examples/ex3.txt")

result

# Spacial case - one fewer column names than number of data rows
# read_csv infers first column as index

# Other arguments - e.g., skipping lines

all_lines = pd.read_csv("examples/ex4.csv")

all_lines

skipping_lines = pd.read_csv("examples/ex4.csv", skiprows=[0, 2, 3])

skipping_lines

# Missing values or with placeholders "sentinel" values
# example sentinels are NA and NULL

result = pd.read_csv("examples/ex5.csv")

result

# masking the NA condition, gives True for the NA

pd.isna(result)

# Using the na_values argument to include strings
# besides the default recognized by read_csv

result = pd.read_csv("examples/ex5.csv", na_values=["NULL"])

result

# disabling the default NA

result2 = pd.read_csv("examples/ex5.csv", keep_default_na=False)

result2

# then masking the NA condition gives all falses


pd.isna(result)

pd.isna(result2)

# Specifying to use only the NAs

result3 = pd.read_csv("examples/ex5.csv", keep_default_na=False,
                        na_values=["NA"])
 
result3

# Masking for na's gives a true

pd.isna(result3)

# Different NA sentinels can be spedified for each column in a dictionary"

sentinels = {"message":["foo", "NA"], "something":["two"]}

sentinels

pd.read_csv("examples/ex5.csv")

pd.read_csv("examples/ex5.csv", na_values=sentinels, keep_default_na=False)

# Some pandas.rad_csv function arguments
# path, sep or delimiter, header, index_col, names, skiprows, na_values
# keep_default_na, comment, parse_dates, keep_date_col, converters
# dayfirst, date_parser, nrows, itnerator, chunksize, skip_footer
# verbose, encoding, squeeze, thousandes, decimal, engine


# Reading text files in pieces
# ----------------------------

# For large files, may want to just read first few lines
# or interate through smaller chunks of a file

pd.options.display.max_rows = 10

result = pd.read_csv("examples/ex6.csv")

result

# reading a small number of rows

result = pd.read_csv("examples/ex6.csv", nrows=5)

result

# read a file in pieces  using chunksize

chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)

type(chunker)

# TextFileReader object allows you to interate
# parts of the file according to chunksize


tot = pd.Series([], dtype='int64')

for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
    
tot = tot.sort_values(ascending=False)

tot[:10]

# TextFileReader also has get_chunk method to read variable size chunks


# Writing data to text format
# ---------------------------

data = pd.read_csv("examples/ex5.csv")

data

# Using DataFrame's to_csv method

data.to_csv("examples/out.csv")










# Working with other delimited formsts
# ------------------------------------

# JSON data
# ---------



# XML and HTML: Web scraping
# --------------------------



# ----------------------------------------------------
# 6.2 Binary Data Formats
# ----------------------------------------------------


# Reading Microsoft Excel files
# -----------------------------


# Using HDF5 Format
# -----------------


# ----------------------------------------------------
# 6.3 Interacting with Web APIs
# ----------------------------------------------------


# ----------------------------------------------------
#  6.4 Interacting with databases
# ----------------------------------------------------



# ----------------------------------------------------
#  6.5 Conclusion
# ----------------------------------------------------












