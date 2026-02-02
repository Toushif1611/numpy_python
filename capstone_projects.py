#import necessary libraries
import numpy as np
import pandas as pd

#loading the dataset
df = pd.read_csv('C:\\Users\\MacAir\\OneDrive\\Desktop\\GITDEMO\\numpy_python\\mobile_customers.csv') # path to your dataset
print(df.head())

#checking for missing values
print('Missing values in each column:')
print(df.isnull().sum())

df['salary (INR)'].fillna(df['salary (INR)'].mean(), inplace=True)
df['performance_score'].fillna(df['performance_score'].median(), inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(), inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)

#replace negative salary
df['salary (INR)'] = np.where(df['salary (INR)'] < 0, df['salary (INR)'].mean(), df['salary (INR)'])

salary_mean = df['salary (INR)'].mean()
salary_std = df['salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

#remove rows where salary is too high or too low
df = df[(df['salary (INR)'] >= lower_bound) & (df['salary (INR)'] <= upper_bound)]

df.to_csv('C:\\Users\\MacAir\\OneDrive\\Desktop\\GITDEMO\\numpy_python\\mobile_customers_cleaned.csv', index=False)
print('Data cleaning completed! Saved as mobile_customers_cleaned.csv')