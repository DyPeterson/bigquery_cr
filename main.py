import pandas as pd
import numpy as np

netflix_filepath = './data/netflix_titles.csv'
netflix_df = pd.read_csv(netflix_filepath, header=0)

def csv_to_dataframe(filepath:str, index:str) -> None:
    """
    Load a csv file into a pandas dataframe
    returns inserted csv into 'df' variable

    *args:
        filepath: string of filepath to csv file
        index: string of column to index dataframe by
    """
    df = pd.read_csv(filepath, header=0, index_col=[index])
    return df

def index_setter(dataframe, index):
    """
    Sets the index of dataframe to a desired existing column

    args*:
        dataframe: dataframe to have index changed
        index: name of column that index will be set to
    """
    dataframe.set_index(index, inplace=True)
    
def nullfill(dataframe):
    """
    Targets empty fields of a dataframe and sets them to the string 'NULL'
    """    
    dataframe.fillna(value='NULL', axis=1, inplace=True)

def dupllicate_drop(dataframe, col_check=None):
    """
    drop duplicate rows targeting a specific column(s)

    args*:
        col_check: ['column1', 'column2']
            Enter column name as a string
            Only 1 column required, if none set uses all columns
            enter multiple columns as strings seperated by commas in a list
            eg: duplicate drop(dataframe, ['col1', 'col2'])
    """
    dataframe.drop_duplicates(subset=col_check, inplace=True)

def drop_missing_row(dataframe) -> None:
    """
    placeholder
    """
    dataframe.dropna(subset=['type','title'], inplace=True)

def drop_low_data(dataframe) -> None:
    """
    Placeholder
    """
    dataframe.dropna(thresh=2, inplace=True)

def drop_extra_columns(dataframe):
    """
    placeholder
    """
    dataframe.drop(dataframe.columns[12:])

def write_csv(dataframe):
    """
    placeholder
    """
    new_file='./data/clean_netflix.csv'
    dataframe.to_csv(new_file)

def run(dataframe):
    nullfill(dataframe)
    dupllicate_drop(dataframe)
    drop_missing_row(dataframe)
    drop_low_data(dataframe)
    index_setter(dataframe,'title')
    drop_extra_columns(dataframe)
    write_csv(dataframe)
run(netflix_df)