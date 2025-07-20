import pandas as pd

print(f"pandas version: {pd.__version__}")
my_dataset_1 = {
    'cars' : ['BMW', 'Volvo', 'Ford', 'Toyota'],
    'passings' : [3, 7, 2, 5],
    'year' : [2012, 2015, 2017, 2018]
}

print(f"creatring a pandas DataFrame from a dictionary: my_dataset_1")
my_pandas_df = pd.DataFrame(my_dataset_1)
print(my_pandas_df)

#Series in pandas is like a single column in a DataFrame/table
print(f"creating a pandas Series from a dictionary: my_dataset_1")
my_dataset_1_series_1 = pd.Series(my_dataset_1)
print(my_dataset_1_series_1)
print(f"first value in the series: {my_dataset_1_series_1[0]}")
