from math import log
import operator
import numpy as np


def calculate_shannon_entropy(data_set):
    """ Расчет информационной энтропии."""

    num_entries = len(data_set)
    label_counts = {}  # Ключ - метка категории, значение - это количество выборок, принадлежащих этой категории.
    for feat_vec in data_set:
        feat_vec = feat_vec
        current_label = feat_vec[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1
    shannon_entropy = 0.0

    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_entropy -= prob * log(prob, 2)

    return shannon_entropy


def split_dataset(data_set, axis, value):
    """Разделение данных по характеристикам."""

    ret_dataset = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:  #
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec = np.append(reduced_feat_vec, feat_vec[axis + 1:])
            ret_dataset.append(reduced_feat_vec)
    return ret_dataset


def choose_best_feature_to_split(data_set):
    """Выбор лучшего признака для разделения."""

    num_features = len(data_set[0]) - 1
    base_entropy = calculate_shannon_entropy(data_set)  # Рассчитать информационную энтропию
    best_info_gain = 0.0
    best_feature = -1

    for i in range(num_features):

        feat_list = [example[i] for example in data_set]
        unique_vals = set(feat_list)  # Уникальные значения признака

        new_entropy = 0.0

        for value in unique_vals:  # Рассчитать информационную энтропию каждого значения признака
            # Разделяем набор данных по текущему признаку и значению
            sub_dataset = split_dataset(data_set, i, value)
            # Рассчитываем вероятность этого разделения
            prob = len(sub_dataset) / float(len(data_set))
            # print(f'Prob: {prob}')
            # Рассчитываем новую энтропию для данного разделения и усредняем
            new_entropy += prob * calculate_shannon_entropy(sub_dataset)

        info_gain = base_entropy - new_entropy  # Прирост информации

        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature


def majority_class_count(class_list):
    """Определение класса с наибольшей частотой в списке классов."""

    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1

    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    """ Метод для генерации дерева решений по входным данным."""

    class_list = [example[-1] for example in data_set]

    # Когда категории совпадают, прекращаем деление, возвращаемся непосредственно к метке категории
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # После прохождения всех функций набор данных по-прежнему не может быть разделен на группы, содержащие только уникальные категории
    if len(data_set[0]) == 1:
        return majority_class_count(class_list)  # Категория с наибольшим количеством вхождений

    best_feat = choose_best_feature_to_split(data_set)  # Лучший индекс признака классификации
    best_feat_label = labels[best_feat]  # Названии признака

    my_tree = {best_feat_label: {}}  # Выбор лучших признаков

    del (labels[best_feat])  # Удалить уже выбранные признаки

    feat_values = [example[best_feat] for example in data_set]
    unique_vals = set(feat_values)

    for value in unique_vals:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_dataset(data_set, best_feat, value), sub_labels)

    return my_tree


def classify(input_tree, feat_labels, test_vec):
    """Классификация класса по входным данным. Для одного экземпляра."""

    first_str = list(input_tree.keys())[0]  # Получаем метку признака для текущей вершины дерева
    second_dict = input_tree[first_str]  # Получаем словарь разветвлений для данной метки признака
    feat_index = feat_labels.index(first_str)
    key = test_vec[feat_index]
    # Получаем результат классификации для данного значения признака
    value_of_feat = second_dict[key]

    if isinstance(value_of_feat, dict):
        # Если значение признака - словарь, рекурсивно классифицируем дальше
        class_label = classify(value_of_feat, feat_labels, test_vec)
    else:
        # Если значение признака - конечная метка класса
        class_label = value_of_feat

    # print(
    # f'Data: test_values - {test_vec} \nkey - {key},\nvalue of feat - {value_of_feat}. \nThe result of classifying is {class_label}. \n')
    return class_label


def accuracy(true_labels, predicted_labels):
    """Вычисление точности (accuracy)"""

    correct = 0
    total = len(true_labels)

    for i in range(total):
        if true_labels[i] == predicted_labels[i]:
            correct += 1

    accuracy = correct / total
    return accuracy


def precision(true_labels, predicted_labels, target_class):
    """Вычисление точности (precision) для заданного класса"""

    true_positives = 0
    false_positives = 0

    for i in range(len(true_labels)):
        if predicted_labels[i] == target_class:
            if true_labels[i] == predicted_labels[i]:
                true_positives += 1
            else:
                false_positives += 1

    if true_positives + false_positives == 0:
        return 0  # Избегаем деления на ноль

    precision = true_positives / (true_positives + false_positives)
    return precision


def recall(true_labels, predicted_labels, target_class):
    """Вычисление полноты (recall) для заданного класса"""

    true_positives = 0
    false_negatives = 0

    for i in range(len(true_labels)):
        if true_labels[i] == target_class:
            if predicted_labels[i] == target_class:
                true_positives += 1
            else:
                false_negatives += 1

    if true_positives + false_negatives == 0:
        return 0  # Избегаем деления на ноль

    recall = true_positives / (true_positives + false_negatives)
    return recall


def calculate_auc_roc(true_labels, predicted_scores):
    sorted_predictions = [p for _, p in sorted(zip(predicted_scores, true_labels), reverse=True)]
    true_positive_count = 0
    false_positive_count = 0
    total_positive = true_labels.count('p')
    total_negative = len(true_labels) - total_positive

    for label in sorted_predictions:
        if label == 'p':
            true_positive_count += 1
        else:
            false_positive_count += 1

    area_under_curve = (true_positive_count / total_positive) * (false_positive_count / total_negative)

    return area_under_curve


def calculate_auc_pr(true_labels, predicted_scores):
    sorted_predictions = [p for _, p in sorted(zip(predicted_scores, true_labels), reverse=True)]
    precision = 0
    recall = 0
    area_under_curve = 0.0

    total_positive = true_labels.count('p')

    for label in sorted_predictions:
        if label == 'p':
            precision += 1
            recall += 1
        else:
            recall += 1
            area_under_curve += (precision / recall) * (1 / total_positive)

    return area_under_curve
