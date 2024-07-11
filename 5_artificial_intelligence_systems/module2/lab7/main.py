import pandas as pd

from sklearn.model_selection import train_test_split
from visualization import *
from library import *
from preprocessing import *
from dataset_description import *

TARGET_COLUMN = 'Outcome'
LEARNING_RATES = [0.01, 0.1, 0.2, 0.25, 0.5]
NUM_ITERATIONS_LIST = [100, 500, 1000]
METHODS = [train_with_newton_method, train_with_gradient_descent]

if __name__ == '__main__':
    df = pd.read_csv(DATASET_FILE_PATH)
    print_dataset_description(df)
    print_dataset_statistics(df)
    # get_boxplotes(df)
    # get_correlation_matrix(df)

    df = preprocessing_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop([TARGET_COLUMN], axis=1),
        df[TARGET_COLUMN],
        test_size=0.2
    )

    best_num_iter = NUM_ITERATIONS_LIST[0]
    best_learning_rate = LEARNING_RATES[0]
    best_method = None
    best_accuracy = 0

    for iteration in NUM_ITERATIONS_LIST:
        for rate in LEARNING_RATES:
            for method in METHODS:
                print(
                    f'\t|Model with params: num_iterations = {iteration}, learning rate = {rate}, method = {method.__name__}|')

                theta = method(X_train, y_train, learning_rate=rate, num_iterations=iteration)

                y_pred = predict(X_test, theta)

                accuracy = get_accuracy(y_pred, y_test)
                precision = get_precision(y_pred, y_test)
                recall = get_recall(y_pred, y_test)
                f1_score = get_f1_score(precision, recall)

                if best_accuracy < accuracy:
                    best_accuracy = accuracy
                    best_method = method
                    best_num_iter = iteration
                    best_learning_rate = rate

                print(f"Accuracy: {accuracy:.4f}")
                print(f"Precision: {precision:.4f}")
                print(f"Recall: {recall:.4f}")
                print(f"F1-Score: {f1_score:.4f}")

    print(f'\n\t\tBest parameters:\n'
          f'Learning rate: {best_learning_rate if best_method.__name__ != "train_with_newton_method" else "-"}\n'
          f'Method: {best_method.__name__}\n'
          f'Iterations: {best_num_iter}\n'
          f'Accuracy: {best_accuracy}')
