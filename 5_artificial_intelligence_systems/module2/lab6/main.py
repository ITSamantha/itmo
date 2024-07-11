import random

import pandas as pd
from library import *
from preprocessing import *
from dataset_description import *
DATASET_PATH = 'dataset/mushrooms.csv'
TARGET_COLUMN = 'poisonous'


def read_data(dataset_path):
    print('\t---Reading data from file---')
    with open(dataset_path, 'r') as file:
        temp_lenses = [inst.strip().split(',') for inst in file.readlines()]
    return temp_lenses


if __name__ == '__main__':

    lenses = read_data(DATASET_PATH)

    df = pd.DataFrame(lenses, columns=lenses[0])[1:]

    print_dataset_description(df)
    print_dataset_statistics(df)

    print('\t---Preprocessing data---')
    df = process_missing_values(df)

    X = df.drop([TARGET_COLUMN], axis=1)
    y = df[TARGET_COLUMN]

    # Случайный отбор sqrt(n) признаков
    n_features = int(np.sqrt(X.shape[1]))
    print(LINE_SEPARATOR, f'\t\tОтобрано признаков:{n_features}', LINE_SEPARATOR, sep=SEPARATOR)

    selected_features = random.sample(list(set(X.columns)), k=n_features)
    print(LINE_SEPARATOR, f'\t\tОтобранные признаки:', *selected_features, LINE_SEPARATOR, sep=SEPARATOR)

    X = X[selected_features]
    X[TARGET_COLUMN] = y

    lensesLabels = list(X.columns)
    lensesTree = create_tree(X.to_numpy(), lensesLabels)

    print('\t---Classifying values---')
    result = []

    for x in X.to_numpy():
        result.append(classify(lensesTree, list(X.columns), x))

    print('\t---Result of classifying---\n', *result)

    y = list(y)

    accuracy = accuracy(y, result)
    print('---Accuracy---\n', accuracy)

    precision_p = precision(y, result, 'p')
    print('---Precision for class "p"---\n', precision_p)

    precision_e = precision(y, result, 'e')
    print('---Precision for class "e"---\n', precision_e)

    recall_e = recall(y, result, 'e')
    print('---Recall for class "e"---\n', recall_e)

    recall_p = recall(y, result, 'p')
    print('---Recall for class "p"---\n', recall_p)

    auc_roc = calculate_auc_roc(y, result)
    print('---AUC-ROC---\n', auc_roc)

    auc_pr = calculate_auc_pr(y, result)
    print('---AUC-PR---\n', auc_pr)
