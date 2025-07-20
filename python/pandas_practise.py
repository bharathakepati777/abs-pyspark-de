# Databricks notebook source
# DBTITLE 1,Initializing the libraries
import pandas as pd
print(f"pandas version: {pd.__version__}")

# COMMAND ----------

# DBTITLE 1,Sample DataFrame Creation
my_dataset_1 = {
    'cars' : ['BMW', 'Volvo', 'Ford', 'Toyota'],
    'passings' : [3, 7, 2, 5],
    'year' : [2012, 2015, 2017, 2018]
}

print(f"creatring a pandas DataFrame from a dictionary: my_dataset_1")
my_pandas_df = pd.DataFrame(my_dataset_1)
print(my_pandas_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Series in pandas is like a single column in a DataFrame/table

# COMMAND ----------

# DBTITLE 1,Series in Pands
print(f"creating a pandas Series from a dictionary: my_dataset_1")
my_dataset_1 = {
    'cars' : ['BMW', 'Volvo', 'Ford', 'Toyota'],
    'passings' : [3, 7, 2, 5],
    'year' : [2012, 2015, 2017, 2018]
}

my_dataset_1_series_1 = pd.Series(my_dataset_1)
print(my_dataset_1_series_1)
print()
print(f"first value in the series: {my_dataset_1_series_1[0]}")
print(f"second value in the series: {my_dataset_1_series_1[1]}")
print()
print("chosing particluar particular value form my_dataset_1 like my_dataset_1['cars']")
my_dataset_1_sereies_cars = pd.Series(my_dataset_1['cars'])
print(my_dataset_1_sereies_cars)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Index
# MAGIC ######With the index argument, you can name your own labels.
# MAGIC ######When you have created labels, you can access an item by referring to the label.

# COMMAND ----------

dataset_2 = [1,7,2,4]
my_lables_1 = pd.Series(dataset_2,index =['a','b','c','d'])
print(my_lables_1)

print(f"accessing the data using lables")
print(my_lables_1["c"])

# COMMAND ----------

# MAGIC %md
# MAGIC ###Key/Value Object as Series
# MAGIC ######You can also use a key/value object, like a dictionary, when creating a Series.
# MAGIC ######To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# COMMAND ----------

calories = {"day1": 304, "day2": 413, "day3": 284, "day4": 383}
my_dataset = pd.Series(calories)
print(my_dataset)
print()
my_dataset_2 = pd.Series(calories, index = ["day1","day2"])
print(my_dataset_2)

# COMMAND ----------

# MAGIC %md
# MAGIC ###DataFrame
# MAGIC #####Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# MAGIC #####A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# MAGIC Series is like a column, a DataFrame is the whole table.

# COMMAND ----------

raw_data = {
    "calories" : [414,383,401,390],
    "duration" : [50,40,45,40]
}

my_pandas_df = pd.DataFrame(raw_data)
print(my_pandas_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Locate Row
# MAGIC ######As you can see from the result above, the DataFrame is like a table with rows and columns.
# MAGIC ######Pandas use the loc attribute to return one or more specified row(s)
# MAGIC ######loc[] --> retrun series
# MAGIC ######loc[[]] --> retrund DataFrame

# COMMAND ----------

print(my_pandas_df.loc[2])
print()
print(my_pandas_df.loc[[2]])
print()
print(my_pandas_df.loc[[0,2]])

# COMMAND ----------

# DBTITLE 1,Using Named Index
raw_data = {
    "calories" : [414,383,401,390],
    "duration" : [50,40,45,40]
}

my_pandas_df = pd.DataFrame(raw_data, index = ['day1','day2','day3','day4'])
print(my_pandas_df)

print()
print(my_pandas_df.loc["day2"])
print()
print(my_pandas_df.loc[["day2"]])
print()
print(my_pandas_df.loc[["day1","day2"]])

# COMMAND ----------

# MAGIC %md
# MAGIC ##CSV File Read
# MAGIC ######A simple way to store big data sets is to use CSV files (comma separated files).
# MAGIC
# MAGIC ##to_string()
# MAGIC ######If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# MAGIC ######use to_string() to print the entire DataFrame.
# MAGIC

# COMMAND ----------

file_path= "/Volumes/python/pandas/sample_pandas_data/data.csv"

df = pd.read_csv(file_path)
print(df)
print(df.to_string())

# COMMAND ----------

# MAGIC %md
# MAGIC ###max_rows
# MAGIC The number of rows returned is defined in Pandas option settings.
# MAGIC
# MAGIC You can check your system's maximum rows with the pd.options.display.max_rows statement.

# COMMAND ----------

print(pd.options.display.max_rows)

pd.options.display.max_rows = 99
df = pd.read_csv(file_path)
print(df)
print(df.to_string())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read JSON
# MAGIC #####Big data sets are often stored, or extracted as JSON.
# MAGIC #####JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# COMMAND ----------

json_df = pd.read_json("/Volumes/python/pandas/sample_pandas_data/json_data.json")
print(json_df.to_string())

# COMMAND ----------

# MAGIC %md
# MAGIC ###Pandas - Analyzing DataFrames
# MAGIC ######head() - The head() method returns the headers and a specified number of rows, starting from the top.
# MAGIC ######tail() - The tail() method returns the headers and a specified number of rows, starting from the bottom.
# MAGIC ######info() - The DataFrames object has a method called info(), that gives you more information about the data set.

# COMMAND ----------

raw_df = pd.read_csv("/Volumes/python/pandas/sample_pandas_data/data.csv")
print(raw_df.head())
print()
print(raw_df.head(10))
print()
print(raw_df.tail())
print()
print(raw_df.tail(10))
print()
print(raw_df.info())

# COMMAND ----------

# MAGIC %md
# MAGIC ##Data Cleaning
# MAGIC ####Data cleaning means fixing bad data in your data set.
# MAGIC ####Bad data could be:
# MAGIC #####1. Empty cells
# MAGIC #####2. Data in wrong format
# MAGIC #####3. Wrong data
# MAGIC #####4. Duplicates

# COMMAND ----------

# MAGIC %md 
# MAGIC ###Pandas - Cleaning Empty Cells
# MAGIC #####Remove Rows --> One way to deal with empty cells is to remove rows that contain empty cells.
# MAGIC #####dropna() --> dropna() method returns a new DataFrame, and will not change the original.
# MAGIC #####If you want to change the original DataFrame, use the inplace = True 

# COMMAND ----------

df = pd.read_csv(file_path)
df.dropna(inplace = True)
print(df.to_string())

# COMMAND ----------
