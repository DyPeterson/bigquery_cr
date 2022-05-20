import pandas as pd
import numpy as np

netflix_filepath = './data/netflix_titles.csv'
netflix_df = pd.read_csv(netflix_filepath, header=0, sep=',').replace('\n','', regex=True)

def csv_to_dataframe(filepath:str, index:str) -> None:
    """
    Load a csv file into a pandas dataframe

    returns inserted csv into 'df' variable

        - filepath: string of filepath to csv file
        - index: string of column to index dataframe by
    """
    df = pd.read_csv(filepath, header=0, index_col=[index])
    return df

def index_setter(dataframe, index) -> None:
    """
    Sets the index of dataframe to a desired existing column

        - dataframe: dataframe to have index changed
        - index: name of column that index will be set to
    """
    dataframe.set_index(index, inplace=True)
    
def nullfill(dataframe) -> None:
    """
    Targets empty fields of a dataframe and sets them to the string 'NULL'
    """    
    dataframe.fillna(value='NULL', axis=1, inplace=True)

def duplicate_drop(dataframe, col_list=None) -> None:
    """
    drop duplicate rows targeting a specific column(s)

    col_list: ['column1', 'column2']
    - Enter column name as a string
    - Only 1 column required, if none set uses all columns
    - Enter multiple columns as strings seperated by commas in a list
    - eg: duplicate drop(dataframe, ['col1', 'col2'])
    """
    dataframe.drop_duplicates(subset=col_list, inplace=True)

def drop_missing_row(dataframe, col_list=None) -> None:
    """
    Drops dataframe row if it is missing any data in col_list

    col_list: ['column1', 'column2']
    - Enter column name as a string or list
    - Only 1 column required, if none set uses all columns
    - Enter multiple columns as strings seperated by commas in a list
    - eg: duplicate drop(dataframe, ['col1', 'col2'])
    """
    dataframe.dropna(subset=col_list, inplace=True)

def drop_low_data(dataframe) -> None:
    """
    Drops dataframe row if missing more than 2 values 
    """
    dataframe.dropna(thresh=2, inplace=True)

def drop_extra_columns(dataframe):
    """
    Drops dataframe columns if dataframe has more than 12 columns
    """
    dataframe.drop(dataframe.columns[12:])

def write_csv(dataframe):
    """
    Writes dataframe into a new csv file located in './data/clean_netflix.csv'
    """
    new_file='./data/clean_netflix.csv'
    dataframe.to_csv(new_file)

def run(dataframe):
    nullfill(dataframe)
    duplicate_drop(dataframe, 'title')
    drop_missing_row(dataframe, ['type','title'])
    drop_low_data(dataframe)
    index_setter(dataframe,'title')
    drop_extra_columns(dataframe)
    write_csv(dataframe)
run(netflix_df)