import pandas as pd
import numpy as np

netflix_filepath = './data/netflix_titles.csv'
netflix_df = pd.read_csv(netflix_filepath, header=0, index_col='title')

def csv_to_dataframe(filepath:str, index:str) -> None:
    """
    Load a csv file into a pandas dataframe
    returns inserted csv into 'df' variable

    *args:
        filepath: string of filepath to csv file
        index: string of column to index dataframe by
    """
    df = pd.read_csv(filepath, header=0, index_col=index)
    return df

def nullfill(dataframe):
    """
    placeholder
    """    
    dataframe.fillna(value='NULL', axis=1, inplace=True)

def dupllicate_drop(dataframe):
    """
    placeholder
    """
    dataframe.drop_duplicates(subset=['title'], inplace=True)

def drop_missing_row(dataframe) -> None:
    """
    placeholder
    """
    dataframe.dropna(subset=['type','title'], inplace=True)
    
def drop_extra_columns(dataframe):
    """
    placeholder
    """
    dataframe.drop(dataframe.columns[])
    
def write_csv(dataframe):
    """
    placeholder
    """
    new_file='./data/clean_netflix.csv'
    dataframe.to_csv(new_file,)