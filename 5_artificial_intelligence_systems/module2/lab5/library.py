import numpy as np
from collections import Counter

from sklearn.metrics import confusion_matrix


def my_confusion_matrix(y_true, y_pred):
    y_pred = y_pred.to_numpy()
    # Получаем уникальные классы в y_true
    classes = np.unique(y_true)
    num_classes = len(classes)

    # Инициализируем матрицу ошибок нулями
    confusion = np.zeros((num_classes, num_classes), dtype=np.float64)

    # Заполняем матрицу ошибок
    for i in range(len(y_true)):
        true_class = np.where(classes == y_true[i])[0][0]
        pred_class = np.where(classes == y_pred[i])[0][0]
        confusion[true_class][pred_class] += 1

    return confusion


def my_f1_score(y_true, y_pred):
    # Вычисляем матрицу ошибок
    confusion = my_confusion_matrix(y_true, y_pred)

    # Извлекаем TP, FP и FN из матрицы ошибок
    TP = confusion[1, 1]  # Истинно положительные
    FP = confusion[0, 1]  # Ложноположительные
    FN = confusion[1, 0]  # Ложноотрицательные

    # Вычисляем точность и полноту
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    # Вычисляем F1-меру
    f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X.to_numpy()
        self.y_train = y.to_numpy()

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X):
        X = X.to_numpy()
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Рассчитываем расстояния между x и всеми точками в обучающем наборе данных
        distances = [self.euclidean_distance(x, x_train) for x_train in self.X_train]
        # Получаем индексы k ближайших точек
        k_indices = np.argsort(distances)[:self.k]
        # Получаем метки классов ближайших точек
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # Находим наиболее часто встречающийся класс среди ближайших точек
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
