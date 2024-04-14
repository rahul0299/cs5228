import pandas as pd
import string

def clean_data(df, column):
    """
    This function removes punctuation, new line, single/double quoate etc from the specified column in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to process.
    column (str): The column name which contains the text data.

    Returns:
    pandas.DataFrame: The DataFrame with clean data
    """

    # Define a translator to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Apply the translator to the specified column of the DataFrame
    df[column] = df[column].apply(lambda x: x.translate(translator))

    # Remove single&double quotes, newline and others
    df[column] = df[column].str.replace(r"[\"\']", " ").str.replace('\n', ' ').str.replace('\r', ' ')
    df[column] = df[column].str.replace('‘', ' ').replace('’', ' ')
    df[column] = df[column].str.replace('“', ' ').replace('”', ' ')
    df[column] = df[column].str.replace('…', ' ').str.replace('–', ' ')

    # remove extra spaces between words
    df[column] = df[column].str.replace('\s+', ' ')

    return df