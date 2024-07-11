import pandas as pd

DATASET_FILE_PATH = 'dataset/diabetes.csv'
LINE_SEPARATOR = '-' * 70
SEPARATOR = '\n'
MOST_CORRELATED = ['total_bedrooms', 'households']


def print_dataset_statistics(data_frame: pd.DataFrame):
    print('\t\tDataSet statistics (by columns)')
    for column in data_frame:
        print(LINE_SEPARATOR, f'\tColumn: {column}', sep=SEPARATOR)
        print(f'Amount of tuples: {data_frame[column].count()}', sep=SEPARATOR)
        print(f'Type of column: {data_frame[column].dtype}', sep=SEPARATOR)
        print(f'Mathematical expectation (mean): {data_frame[column].mean()}', sep=SEPARATOR)
        print(f'Median: {data_frame[column].median()}', sep=SEPARATOR)
        print(f'Mode: {data_frame[column].mode()}', sep=SEPARATOR)
        print(f'Standard deviation: {data_frame[column].std()}', sep=SEPARATOR)
        print(f'Min: {data_frame[column].min()}', sep=SEPARATOR)
        print(f'Max: {data_frame[column].max()}', sep=SEPARATOR)
        print(f'Quantile 25%: {data_frame[column].quantile(0.25)}', sep=SEPARATOR)
        print(f'Quantile 50%: {data_frame[column].quantile(0.5)}', sep=SEPARATOR)
        print(f'Quantile 75%: {data_frame[column].quantile(0.75)}', sep=SEPARATOR)


def print_dataset_description(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t\tDataSet description', sep=SEPARATOR)
    print(LINE_SEPARATOR, f'\tDataSet shape: {data_frame.shape}', sep=SEPARATOR)
    print(LINE_SEPARATOR, '\tDataSet head:', data_frame.head(), sep=SEPARATOR)
    print(LINE_SEPARATOR, '\t\tDataSet info: ', LINE_SEPARATOR, sep=SEPARATOR)
    data_frame.info()
    print(LINE_SEPARATOR, sep=SEPARATOR)
