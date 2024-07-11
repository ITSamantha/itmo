import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def get_correlation_matrix(data_frame: pd.DataFrame):
    # Рассчитываем корреляцию между признаками
    correlation_matrix = data_frame.corr()

    # Создаем тепловую карту
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Тепловая карта корреляции признаков')
    plt.show()
    # Наиболее коррелированные : total_bedrooms, households


def get_boxplotes(data_frame: pd.DataFrame):
    # Построение отдельных boxplot для каждой колонки
    plt.figure(figsize=(15, 15))

    for i, column in enumerate(data_frame.columns):
        plt.subplot(3, 3, i + 1)
        data_frame[column].plot(kind='box', vert=False)
        plt.title(f'Boxplot для {column}')

    plt.tight_layout()
    plt.show()
