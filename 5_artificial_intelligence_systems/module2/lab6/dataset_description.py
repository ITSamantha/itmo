import pandas as pd

LINE_SEPARATOR = '-' * 70
SEPARATOR = '\n'


def print_dataset_statistics(data_frame: pd.DataFrame):
    print('\t\tDataset statistics (by columns)')
    for column in data_frame:
        print(LINE_SEPARATOR, f'\tColumn: {column}', sep=SEPARATOR)
        print(f'Amount of tuples: {data_frame[column].count()}', sep=SEPARATOR)
        print(f'Type of column: {data_frame[column].dtype}', sep=SEPARATOR)


def print_dataset_description(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t\tDataset description', sep=SEPARATOR)
    print(LINE_SEPARATOR, f'\tDataset shape: {data_frame.shape}', sep=SEPARATOR)
    print(LINE_SEPARATOR, '\tDataset head:', data_frame.head(), sep=SEPARATOR)
    print(LINE_SEPARATOR, '\t\tDataset info: ', LINE_SEPARATOR, sep=SEPARATOR)
    data_frame.info()
    print(LINE_SEPARATOR, sep=SEPARATOR)
