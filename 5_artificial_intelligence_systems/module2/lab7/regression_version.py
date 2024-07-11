import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from visualization import *
# from library import *
from preprocessing import *
from dataset_description import *

TARGET_COLUMN = 'Outcome'

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

    model = LogisticRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
