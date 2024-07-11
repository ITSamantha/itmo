import pandas as pd
import numpy as np
from dataset_description import LINE_SEPARATOR, SEPARATOR


def preprocessing_data(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t\tPreprocessing data', LINE_SEPARATOR, sep=SEPARATOR)
    data_frame = process_missing_values(data_frame)
    data_frame = code_categorical_features(data_frame)
    data_frame = normalize_data(data_frame)
    return data_frame


def process_missing_values(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t1.Check for null and nan values', LINE_SEPARATOR, sep=SEPARATOR)
    null_column_values = get_null_column_values(data_frame)
    isProcessed = False
    for column in data_frame:
        if null_column_values[column] != 0:
            data_frame[column].fillna(data_frame[column].mean(), inplace=True)
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


def code_categorical_features(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t2. Coding categorial features', LINE_SEPARATOR, sep=SEPARATOR)
    print('There are no categorical fratures in this DataFrame.')
    # В данном DataFrame отсутствуют такие признаки
    return data_frame


def normalize_data(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t3. Normalize', LINE_SEPARATOR, sep=SEPARATOR)
    min_max_scaler = lambda x: (x - np.min(x)) / (np.max(x) - np.min(x))
    data_frame = data_frame.apply(min_max_scaler, axis=0)  # Центрирование и шкалирование
    print(data_frame.head())
    return data_frame
