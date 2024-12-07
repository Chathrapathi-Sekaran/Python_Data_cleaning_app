# This is a data cleaning application 

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column contains numeric values, it should replace nulls with mean else it should drop those rows
- at the end it should save the data as clean data and also return duplicates records, clean_data 
"""

# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# data_path = 'Python-Data-Cleaning---P1-main\sales.xlsx'
# data_name = 'jan_sales'

def data_cleaning_master(data_path, data_name):
    
    print("Thanks for providing the details!")
    
    sec = random.randint(1,4) # generating random numbers
    
    print(f"Please wait for {sec} seconds! checking file path!")
    time.sleep(sec)
    print("\nChecking done!")
    #checking if the path exists
    if not os.path.exists(data_path):
        print("Path not found. Please enter the correct path!")
        return 
    else:
        #checking the file type
        if data_path.endswith('.csv'):
            print("The dataset is csv file!")
            data = pd.read_csv(data_path, encoding_errors='ignore')
            
        elif data_path.endswith('.xlsx'):
            print("The dataset is an excel file!")
            data = pd.read_excel(data_path)

        else:
            print("Unknown file type!")
    
    print(f"Please wait for {sec} seconds! checking total columns and rows!")
    time.sleep(sec)
    print("\nChecking done!")

    #showing number of records

    print(f"Dataset contains: \nTotal rows: {data.shape[0]} \nTotal Columns: {data.shape[1]}")

    #Start cleaning 

    #checking duplicates

    total_duplicates = data.duplicated().sum()

    print(f"Datasets has  total duplicate records :{total_duplicates}")

    #saving duplicate records:
    if total_duplicates > 0 :
        duplicate_records = data[data.duplicated()]
        duplicate_records.to_csv(f'{data_name}_duplicated.csv',index=None)
        
    #deleting duplicates
    df = data.drop_duplicates()
    
    print(f"Please wait for {sec} seconds! checking missing values!")
    time.sleep(sec)
    print("\nChecking done!")

    #find missing values
    total_missing_value = df.isnull().sum().sum()
    missing_value_counts = df.isnull().sum()

    print(f"Dataset has Total missing value: {total_missing_value}")
    print(f"Missing values by columns: {missing_value_counts}")

    #dealing with missing values:
    #fillna
    #dropna
    columns = df.columns

    for col in columns:
        if df[col].dtype in (float,int):
            df[col].fillna(df[col].mean())
        else:
            df.dropna(subset=col,inplace=True)
    
            
    #data is cleaned
    print(f"Congrats! Dataset is cleaned! \nNumber of rows: {df.shape[0]} \nNumber of columns: {df.shape[1]}")
    
    
    print(f"Please wait for {sec} seconds! Exporting dataset")
    time.sleep(sec)
    print("\nExporting done!")
    
    df.to_csv(f'{data_name}_Clean_data.csv',index=None)
    print("Dataset is saved !")

if __name__ =="__main__":
    
    print("Welcome to Data cleaning Master!")
    #ask path and file name
    data_path =input("Please enter the dataset path :")
    data_name =input("Please enter the dataset name :")
    
    data_cleaning_master(data_path,data_name)

    