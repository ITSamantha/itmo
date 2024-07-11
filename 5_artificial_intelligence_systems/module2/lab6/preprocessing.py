import pandas as pd
import numpy as np
from dataset_description import LINE_SEPARATOR, SEPARATOR


def preprocessing_data(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t\tPreprocessing data', LINE_SEPARATOR, sep=SEPARATOR)
    data_frame = process_missing_values(data_frame)
    return data_frame


def process_missing_values(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t1.Check for null and nan values', LINE_SEPARATOR, sep=SEPARATOR)
    null_column_values = get_null_column_values(data_frame)
    isProcessed = False
    for column in data_frame:
        if null_column_values[column] != 0:
            most_common_value = data_frame[column].mode()[0]
            data_frame[column].fillna(most_common_value, inplace=True)
            isProcessed = True
    if isProcessed:
        print('There are some null or nan values in DataFrame. Now it is OK!')
        get_null_column_values(data_frame)
    else:
        print('There are no null or nan values in DataFrame.')
    return data_frame


def get_null_column_values(data_frame: pd.DataFrame):
    null_column_values = data_frame.isnull().sum()
    print('The amount of null or nan values for columns:', null_column_values, sep=SEPARATOR)
    return null_column_values
