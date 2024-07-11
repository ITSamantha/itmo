from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

from visualization import *
from dataset_description import *
from preprocessing import *


def pca(data_frame: pd.DataFrame):
    print(LINE_SEPARATOR, '\t4. PCA', LINE_SEPARATOR, sep=SEPARATOR)
    pca_model = PCA(n_components=1, svd_solver='full')
    new_var = pca_model.fit_transform(data_frame[MOST_CORRELATED])
    print("Explained variance:", np.sum(pca_model.explained_variance_ratio_))
    data_frame["bedrooms_households"] = new_var
    data_frame = data_frame.drop(MOST_CORRELATED, axis=1)
    return data_frame


def main():
    df = pd.read_csv(DATASET_FILE_PATH)

    print_dataset_description(df)
    print_dataset_statistics(df)
    get_boxplotes(df)
    get_correlation_matrix(df)

    df = preprocessing_data(df)

    df = pca(df)

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(["median_house_value"], axis=1),
        df["median_house_value"],
        test_size=0.2
    )
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    print("R^2 score:", reg.score(X_test, y_test))


if __name__ == '__main__':
    main()
