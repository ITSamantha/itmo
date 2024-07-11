import numpy as np


def r2_score(y_true, y_pred):
    SS_res = np.sum(
        np.square(y_true - y_pred))  # Сумма квадратов остатков (разница между фактическими и предсказанными значениями)
    mean = np.mean(y_true)  # Среднее значение
    SS_tot = np.sum(
        np.square(y_true - mean))  # Сумма квадратов разницы между фактическими значениями и их средним значением
    r2 = 1 - (SS_res / SS_tot)  # Коэффициент детерминации
    return r2


def get_regression_parameters(x_train, y_train):
    x_train = np.hstack(
        [np.ones((x_train.shape[0], 1)), x_train])  # Добавляем столбец с единицами для учета свободного члена
    theta = np.dot(np.linalg.inv(np.dot(x_train.T, x_train)),
                   np.dot(x_train.T, y_train))  # Вычисление оптимальных коэффициентов
    return theta


def linear_regression(x_train, y_train, x_test):
    theta = get_regression_parameters(x_train, y_train)
    y_pred = predict(x_test, theta)
    return y_pred


def predict(x_test, theta):
    return np.dot(np.column_stack((np.ones(len(x_test)), x_test)), theta)


def pca(data_frame, columns, n_components=1):
    # Центрирование данных (вычитание среднего значения)
    centered_data = data_frame[columns] - np.mean(data_frame[columns], axis=0)

    # Вычисление ковариационной матрицы
    cov_matrix = np.cov(centered_data, rowvar=False)

    # Вычисление собственных значений и собственных векторов ковариационной матрицы
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Сортировка собственных значений и собственных векторов по убыванию
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Выбор первой главной компоненты
    n_components = 1
    top_eigenvectors = eigenvectors[:, :n_components]

    # Преобразование данных
    new_var = np.dot(centered_data, top_eigenvectors)
    return new_var
