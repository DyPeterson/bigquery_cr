import pandas as pd

netflix_filepath = './data/netflix_titles.csv'
netflix_df = pd.read_csv(netflix_filepath, header=0, index_col='show_id')

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

def write_csv(dataframe):
    """
    placeholder
    """
    dataframe.to_csv()