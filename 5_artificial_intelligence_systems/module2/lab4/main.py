import random
from sklearn.model_selection import train_test_split
from visualization import *
from library import *
from preprocessing import *
from dataset_description import *

NUMBER_OF_MODELS = 3
TARGET_COLUMN = 'median_house_value'
PCA_COLUMN = 'bedrooms_households'


def main():
    df = pd.read_csv(DATASET_FILE_PATH)
    print_dataset_description(df)
    print_dataset_statistics(df)
    get_boxplotes(df)
    get_correlation_matrix(df)
    df = preprocessing_data(df)

    for i in range(NUMBER_OF_MODELS):
        print(LINE_SEPARATOR, f'\t\tMODEL {i + 1}', LINE_SEPARATOR, sep=SEPARATOR)

        columns = random.sample(list(set(df.columns)), k=random.randint(3, len(df.columns)))

        if TARGET_COLUMN not in columns:
            columns += [TARGET_COLUMN]

        data_frame = df[columns]
        print('Columns: ', end='')
        print(*data_frame.columns, sep=', ')

        if set(MOST_CORRELATED).issubset(set(columns)):
            print(LINE_SEPARATOR, '\t4. PCA', LINE_SEPARATOR, sep=SEPARATOR)
            data_frame[PCA_COLUMN] = pca(data_frame, MOST_CORRELATED)
            data_frame = df.drop(MOST_CORRELATED, axis=1)

        X_train, X_test, y_train, y_test = train_test_split(
            data_frame.drop([TARGET_COLUMN], axis=1),
            data_frame[TARGET_COLUMN],
            test_size=0.2
        )

        y_pred = linear_regression(X_train, y_train, X_test)
        print(LINE_SEPARATOR, '\tR2 value', LINE_SEPARATOR, sep=SEPARATOR)
        print(r2_score(y_test, y_pred))


if __name__ == '__main__':
    main()
