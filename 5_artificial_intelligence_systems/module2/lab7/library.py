import numpy as np
import pandas as pd

# Гипотеза (sigmoid function)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Функция потерь (log loss)
def log_loss(y, y_pred):
    return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

# Метод обучения с градиентным спуском
def train_with_gradient_descent(X, y, learning_rate, num_iterations):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0

    for i in range(num_iterations):
        z = np.dot(X, weights) + bias
        y_pred = sigmoid(z)

        # Вычисление градиента
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        # Обновление параметров с использованием градиентного спуска
        weights -= learning_rate * dw
        bias -= learning_rate * db

        if i % 100 == 0:
            # Расчет функции потерь и вывод
            cost = log_loss(y, y_pred)
            print(f"Iteration {i}: Loss = {cost:.6f}")

    theta = {"weights": weights, "bias": bias}
    return theta

# Метод обучения с использованием оптимизации Ньютона
def train_with_newton_method(X, y, num_iterations, learning_rate=0):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0

    for i in range(num_iterations):
        z = np.dot(X, weights) + bias
        y_pred = sigmoid(z)

        # Вычисление градиента
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        # Вычисление гессиана (вторые производные)
        diagonal = y_pred * (1 - y_pred)
        hessian = (1 / m) * (X.T @ (diagonal * X.T).T)

        # Обновление параметров с использованием метода Ньютона
        weights -= np.linalg.inv(hessian) @ dw
        bias -= db

        if i % 500 == 0:
            # Расчет функции потерь и вывод
            cost = log_loss(y, y_pred)
            print(f"Iteration {i}: Loss = {cost:.6f}")

    theta = {"weights": weights, "bias": bias}
    return theta

# Прогноз
# Предсказание на тестовых данных
def predict(X, theta):
    weights = theta["weights"]
    bias = theta["bias"]
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)
    return (y_pred > 0.5).astype(int)

# Вычисление точности модели
def get_accuracy(y_pred, y_test):
    return np.mean(y_pred == y_test)

# Вычисление точности (precision)
def get_precision(y_pred, y_test):
    return np.sum((y_pred == 1) & (y_test == 1)) / np.sum(y_pred == 1)

# Вычисление полноты (recall)
def get_recall(y_pred, y_test):
    return np.sum((y_pred == 1) & (y_test == 1)) / np.sum(y_test == 1)

# Вычисление F1 (F1 score)
def get_f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall)