# Python_For_Data_Science English and French

## Introduction

mean = moyenne 

median : the value in the midlle of a dataset (if an even number we take the two in the middle add them and divide by two)

Standard Deviation = écart type : is a measure of how spread out our data (dispersion des donées)

## NumPy Array

NumPy arrays arehomogeneous, meaning they can contain only a single data type, while lists can contain multiple different types of data.

np.array : to create an array

np.ndim returns the number of dimensions of the array.

np.size returns the total number of elements of the array.

np.shape returns a tuple of integers that indicate the number of elements stored along each dimension of the array. 

We can add, remove and sort an array using the np.append(), np.delete() and np.sort() functions. 

reshape(x,y) : x rows y column
 
flatten() : transform to 1 d array
 
sum()  : sum of elements
 
min() : the minimmum

max() : the maximum

you can multiply all the elments : npArray *= integer

 np.mean ()
 
 np.median()
 
 np.var() : variance 
 
 np.std() : 

 ## Pandas
 
 DataFrame : multi dimentional array made of Serie : column
 
 Creating DataFrame : pd.DataFrame(data) data is a dictionary type key string value is an array
 
 Creating DataFrame : pd.DataFrame(data,index=[]) : index allow to specify specific name for each row
  
 df.loc[indexname] : to acces the data of an index
 
 df.iloc[indexint]
 
 Pandas also supports reading from JSON files, as well as SQL databases.
 
 The read_csv(csv file name) function reads the data of a CSV file into a DataFrame
 
 df.head(int) : les int premiers 
 
 df.tail(int) : les int dernier
 
 df.info() : to get essential information
 
 df.drop(columnname', axis=1, inplace=True) : axis=0 delete a row
 
 The describe() function returns the summary statistics for all the numeric columns
 
 value_counts() returns how many times a value appears in the dataset, also called the frequency of the value
 
 The groupby() function is used to group our dataset by the given column. 
 
## Matplotlib

plot()
plot(kind="name of th ekind")
