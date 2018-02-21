Title: Machine Learning Notes : Numpy and Pandas 
Slug: MLN-Numpyandpandas1
Date: 2018-02-14 17:00
Category: Machine Learning
Tags: machinelearning, numpy, pandas, jupyter notebook 
author: Michael Li
Summary: Jupyter notebook notes for machine learning: numpy and pandas

[TOC]

## Overview
This will be a series of notes to record the thinking and learning of my Machine Learning journey. Hopefully it can serve as a place to record the learning process/progress as well as providing some reference for others just entering this field.

## Numpy Basics
Numpy is a powerful module of Python. It covers a lot of basics of Linear algebra, and are great when it comes to doing sceintific and mathematical calculations. That's why it is the 'go-to' solution for Machine Learning. There are other 'highler-level' and more dedicated modules out there like Pandas, seaborn that also utilize or even built on Numpy. Thus proves the powerfulness of Numpy in another way. Though works mostly on the fundation level, Numpy should be considered an equivelant to other more 'advanced' modules and whichever fits the most to solve the problem at hand should be used. 
Without further ado, let's jump right into some code


```python
import numpy as np   # use 'np' to represent Numpy is kind of a coding convention
print('Numpy version: ',np.__version__)
```

    Numpy version:  1.13.3


Now it's imported, let's use it to do some basic stuffs.


```python
x = np.random.rand(5,3)
x
```




    array([[ 0.06584995,  0.58936577,  0.02054667],
           [ 0.90132301,  0.62575129,  0.76350867],
           [ 0.70707616,  0.19462487,  0.35358817],
           [ 0.44329537,  0.57977487,  0.78594087],
           [ 0.76109628,  0.86614311,  0.51521077]])



Manipulate with array is what Numpy do best. Here we generated an 5 row 3 columns array of randome numbers (from 0 to 1)


```python
print(x.shape)
print(x.dtype)
```

    (5, 3)
    float64


We can look at the shape of an array and what data type it is. Obviously it's a float since it's generated from np.random.rand. 


```python
y = np.random.rand(3,4)
z = np.dot(x,y)
z
```




    array([[ 0.60055916,  0.43108417,  0.35430406,  0.32056793],
           [ 2.10608162,  0.91944706,  0.73772388,  1.22819697],
           [ 1.1554381 ,  0.48784172,  0.3088563 ,  0.63719203],
           [ 1.66918268,  0.69113499,  0.68490871,  1.04397122],
           [ 1.95288349,  0.98819028,  0.76639304,  1.09896047]])



Doing some good old dot product. 


```python
z = x @ y
z
```




    array([[ 0.60055916,  0.43108417,  0.35430406,  0.32056793],
           [ 2.10608162,  0.91944706,  0.73772388,  1.22819697],
           [ 1.1554381 ,  0.48784172,  0.3088563 ,  0.63719203],
           [ 1.66918268,  0.69113499,  0.68490871,  1.04397122],
           [ 1.95288349,  0.98819028,  0.76639304,  1.09896047]])



Or more intuitively use '@' operand. 

## How to index Numpy array

First create a sample array using np.array function. 


```python
x1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
x1
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])



Array[row, col] represent array element in 'row' and 'col'. Note that 


```python
x1[1,1]   #row 1, col 1, since Python list starts from 0, so it's 2nd row and col;
```




    5




```python
x1[:,2]   #':' means all elements, so this means all elements on 3rd column, let's see
```




    array([3, 6, 9])




```python
x1[:,1]>3  # an array condition equation will generate an array of boolean values;
```




    array([False,  True,  True], dtype=bool)




```python
x1[ x1[:,1]>3 ] # This means index the rows that the 2nd column is greater than 3;
```




    array([[4, 5, 6],
           [7, 8, 9]])



## Shape Manipulations


```python
x1.reshape(9)   #reshape x1 into one row
```




    array([1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
x1.reshape(3,3)   #reshape back to 3x3
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
x1.reshape(9,1)   #reshape into 9x1
```




    array([[1],
           [2],
           [3],
           [4],
           [5],
           [6],
           [7],
           [8],
           [9]])



## Dot and Mutiplication


```python
x2 = np.arange(9).reshape(3,3)
x2
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])




```python
multi = x1*x2
dot = np.dot(x1,x2)
print('x1 * x2 =', multi)
print('x1 dot x2 =', dot)
```

    x1 * x2 = [[ 0  2  6]
     [12 20 30]
     [42 56 72]]
    x1 dot x2 = [[ 24  30  36]
     [ 51  66  81]
     [ 78 102 126]]


## Pandas Basics


```python
# set some basic data
col_names = ['temperature','time','day']
data = np.array([[64,2100,1],
                 [50,2200,1],
                 [48,2300,1],
                 [34,0,   2],
                 [30,100, 5]])
data
```




    array([[  64, 2100,    1],
           [  50, 2200,    1],
           [  48, 2300,    1],
           [  34,    0,    2],
           [  30,  100,    5]])




```python
# explore the data using numpy, it's clumsy
data2 = data[data[:,1]>1500]
data2
```




    array([[  64, 2100,    1],
           [  50, 2200,    1],
           [  48, 2300,    1]])




```python
# now let's try use Pandas
import pandas as pd

df = pd.DataFrame(data,columns=col_names)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>time</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>64</td>
      <td>2100</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>2200</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48</td>
      <td>2300</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30</td>
      <td>100</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



Pandas DataFrame will put all the data into a much nicer form with neat labels


```python
df[df.time>1500] #Now do it again with data exploration, this time using Pandas DataFrame
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>time</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>64</td>
      <td>2100</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>2200</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48</td>
      <td>2300</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



Much nicer!


```python
# now let's get some basic info of the DataFrame
df.info()
df.describe()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 3 columns):
    temperature    5 non-null int64
    time           5 non-null int64
    day            5 non-null int64
    dtypes: int64(3)
    memory usage: 200.0 bytes





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>time</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.00000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>45.200000</td>
      <td>1340.00000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>13.608821</td>
      <td>1180.25421</td>
      <td>1.732051</td>
    </tr>
    <tr>
      <th>min</th>
      <td>30.000000</td>
      <td>0.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>34.000000</td>
      <td>100.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>48.000000</td>
      <td>2100.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>50.000000</td>
      <td>2200.00000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>64.000000</td>
      <td>2300.00000</td>
      <td>5.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# you can change the element in DataFrame like so:
df.day[df.day==1] = 'Mon'
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>time</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>64</td>
      <td>2100</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>2200</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48</td>
      <td>2300</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30</td>
      <td>100</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# or do it the Pandas way
df.day.replace(to_replace=range(7),
               value=['Su','Mon','Tues','Wed','Th','Fri','Sat'],
               inplace=True)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>time</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>64</td>
      <td>2100</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>2200</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48</td>
      <td>2300</td>
      <td>Mon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>0</td>
      <td>Tues</td>
    </tr>
    <tr>
      <th>4</th>
      <td>30</td>
      <td>100</td>
      <td>Fri</td>
    </tr>
  </tbody>
</table>
</div>




```python
# one hot encoding example
pd.get_dummies(df.day)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Fri</th>
      <th>Mon</th>
      <th>Tues</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


