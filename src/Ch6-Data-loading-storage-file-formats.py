
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



# Making the mesage column the indexed column


names = ["a", "b", "c", "d", "message"]

names




# Reading text files in pieces
# ----------------------------


# Writing data to text format
# ---------------------------


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












