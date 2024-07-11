import random
from sklearn.model_selection import train_test_split
import library
from library import *
from visualization import *
from preprocessing import *
from dataset_description import *

MAX_VALUE = 10
TARGET_COLUMN = 'Wine'


def main():
    df = pd.read_csv(DATASET_FILE_PATH)
    print_dataset_description(df)
    print_dataset_statistics(df)
    get_correlation_matrix(df)
    df = preprocessing_data(df)

    for i in range(MAX_VALUE):
        print(f'K = {i}')

        # Model 1. Признаки случайно отбираются
        print(LINE_SEPARATOR, 'Model 1. Признаки случайно отбираются', LINE_SEPARATOR, sep=SEPARATOR)
        columns = random.sample(list(set(df.columns)), k=random.randint(3, len(df.columns)))
        if TARGET_COLUMN not in columns:
            columns += [TARGET_COLUMN]
        data_frame = df[columns]
        print('Columns: ', end='')
        print(*data_frame.columns, sep=', ')
        X_train, X_test, y_train, y_test = train_test_split(
            data_frame.drop([TARGET_COLUMN], axis=1),
            data_frame[TARGET_COLUMN],
            test_size=0.2
        )

        knn = KNNClassifier(k=2)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        confusion_matrix = my_confusion_matrix(y_pred, y_test)
        f1 = library.my_f1_score(y_pred, y_test)
        print('Confusion matrix: ', confusion_matrix)
        print('F1 score: ', f1)

        # Model 2. Фиксированный набор признаков, который выбирается заранее.
        print(LINE_SEPARATOR, 'Model 2. Фиксированный набор признаков, который выбирается заранее.', LINE_SEPARATOR,
              sep=SEPARATOR)
        X_train, X_test, y_train, y_test = train_test_split(
            df.drop([TARGET_COLUMN], axis=1),
            df[TARGET_COLUMN],
            test_size=0.2
        )

        knn = KNNClassifier(k=2)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        confusion_matrix = my_confusion_matrix(y_pred, y_test)
        f1 = library.my_f1_score(y_pred, y_test)
        print('Confusion matrix: \n', confusion_matrix)
        print('F1 score: ', f1)


if __name__ == '__main__':
    main()
