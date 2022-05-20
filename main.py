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
    placeholder
    """
    dataframe.set_index(index, inplace=True)

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
    
def drop_low_data(dataframe) -> None:
    """
    Placeholder
    """
    
def drop_extra_columns(dataframe):
    """
    placeholder
    """
    dataframe.drop(dataframe.columns[13:])

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
    index_setter(dataframe,'title')
    drop_extra_columns(dataframe)
    write_csv(dataframe)
run(netflix_df)