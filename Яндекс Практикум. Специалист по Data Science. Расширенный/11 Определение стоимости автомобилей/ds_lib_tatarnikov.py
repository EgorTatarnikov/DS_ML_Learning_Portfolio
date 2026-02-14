import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
import math

# Приведение названий к змеиному стилю
def to_snake_case(s):
    s = s.strip()
    s = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', s)  # вставляем _ между строчной и заглавной
    s = s.lower()
    s = s.replace('-', '_')
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', '_', s)
    return s

# Функция для визуализации распределения и разброса данных
def show_plot(df, feature, type='hist', new_bins=0, new_hue=None, 
                main_title=None, new_stat='count', new_common_norm=True, new_kde=True):
    """
    Выводит график для визуализации распределения и разброса данных.

    Параметры:
    df (pd.DataFrame): DataFrame с данными.

    feature (str): Название признака для визуализации.
    type (str, optional): 'hist' - Выводит гистограмму и горизонтальную диаграмму размаха.
                                   Используется по умолчанию.
                          'bars' - Выводит cтолбчатую диаграмму частот и горизонтальную диаграмму размаха.
    new_bins (int, optional): Количество корзин для гистограммы. 
                              Если 0, используется значение по умолчанию
                              и происходит автоматический подбор количества корзин.
    new_hue (str, optional): Название признака для категоризации.
                             По умолчанию - None
    title (str, optional): Общий заголовок.
    new_stat (str, optional): По умолчанию - 'count'
    new_common_norm (bool, optional): По умолчанию - True
    new_kde (bool, optional): По умолчанию - True
    """
    
    # Задаем количество знаков после запятой в зависимости
    if abs(df[feature].max()) > 1000:
        rnd = 0
    elif abs(df[feature].max()) > 100:
        rnd = 1
    elif abs(df[feature].max()) > 10:
        rnd = 2
    elif abs(df[feature].max()) > 1:
        rnd = 3
    else:
        rnd = 4
   
    fig = plt.figure(figsize=(12, 10))
    gs = fig.add_gridspec(2)

    if main_title != None:
        fig.text(0.5, 1, main_title, ha='center', fontsize=12)

    if type=='hist':
        # Гистограмма
        ax1 = fig.add_subplot(gs[0, 0])
        if new_bins == 0:
            sns.histplot(x=feature, data=df.dropna(subset=[feature]), kde=new_kde, color='#a1c9f4', hue=new_hue, 
                         alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
        else:
            sns.histplot(x=feature, data=df.dropna(subset=[feature]), kde=new_kde, color='#a1c9f4', hue=new_hue, 
                         bins=new_bins, alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
        ax1.set_title(f'Гистограмма для {feature}')
        ax1.set_xlabel(feature)
        if new_stat=='count':
            ax1.set_ylabel('Количество')
        else:
            ax1.set_ylabel('Плотность распределения')
        #ax1.legend()

    elif type=='bars':
        # Столбчатая диаграмма частот
        ax1 = fig.add_subplot(gs[0, 0])
        sns.countplot(x=feature, data=df.dropna(subset=[feature]), edgecolor="black", color='#a1c9f4', 
                      hue=new_hue, alpha=0.6, ax=ax1)
        ax1.set_title(f'Диаграмма частот для {feature}')
        ax1.set_xlabel(feature)
        ax1.set_ylabel('Количество')
        
        ### Округляем значения по оси X
        labels = [item.get_text() for item in ax1.get_xticklabels()] # Получаем текущие метки по оси X (строки)
        new_labels = []
        for label in labels:
            try:
                num = float(label) # Преобразуем строки в float
                if rnd == 0:
                    new_labels.append(str(int(round(num, rnd))))
                else:
                    new_labels.append(str(round(num, rnd))) # округляем до rnd знаков
            except ValueError:
                new_labels.append(label)  # если не число — оставляем как есть
                
        if len(df[feature].unique()) < 10:
            ax1.set_xticklabels(new_labels)
        else:
            ax1.set_xticklabels(new_labels, rotation=90)
    
        ###
        
        #ax1.legend()

    else:
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.set_title('Неправильно задан параметр type')


    
    # Горизонтальная диаграмма размаха (Boxplot) Тренировочная выборка
    ax2 = fig.add_subplot(gs[1, 0])
    sns.boxplot(x=df[feature].dropna(), 
                orient='h', 
                color='#b5d9ff', 
                width=0.2,
                ax=ax2)
    ax2.set_title(f'Диаграмма размаха для {feature}')
    ax2.set_xlabel(feature)

    data = df[feature].dropna()

    # Извлечение статистики
    quartiles = np.percentile(data, [25, 50, 75])  # Q1, медиана, Q3
    q1, median, q3 = quartiles
    iqr = q3 - q1
    lower_whisker = max(min(data), q1 - 1.5 * iqr)
    upper_whisker = min(max(data), q3 + 1.5 * iqr)
    outliers = [x for x in data if x < lower_whisker or x > upper_whisker]

    # Подписываем значения через annotate с поворотом текста
    values = []
    for value, label in zip([q1, median, q3, lower_whisker, upper_whisker],
                            ['Q1', 'Медиана', 'Q3', 'Мин', 'Макс']):
        if value in values:
            shift = -0.15
        else:
            shift = 0.45
        values.append(value)
        ax2.annotate(f"{label}: {value:.{rnd}f}",
                    xy=(value, 0),
                    xytext=(value, shift),
                    textcoords='data',
                    ha='center',
                    fontsize=9,
                    rotation=90)

    # Отметка выбросов
    if len(outliers)<10:
        for outlier in outliers:
            ax2.annotate(f"Выброс: {outlier:.{rnd}f}",
                        xy=(outlier, 0),
                        xytext=(outlier, -0.15),
                        textcoords='data',
                        ha='center',
                        fontsize=9,
                        color='red',
                        rotation=90)

    # Добавление среднего значения
    mean_value = data.mean()
    ax2.annotate(f"Среднее: {mean_value:.{rnd}f}",
                xy=(mean_value, 0),
                xytext=(mean_value, -0.15),
                textcoords='data',
                ha='center',
                fontsize=9,
                color='blue',
                rotation=90)

    # Добавление количества выбросов
    ax2.annotate(f'Количество выбросов: {len(outliers)}',
                xy=(data.min(), -0.45),
                xytext=(data.min(), -0.45),
                textcoords='data',
                ha='left',
                fontsize=10,
                color='purple')

    # Настройка цветов линий коробки через Matplotlib
    for line in ax2.artists:
        line.set_edgecolor('blue')  # Цвет линий коробки
    
  
    # Показ графика
    plt.tight_layout()
    plt.show()

# Функция для визуализации распределения и разброса данных двух таблиц в одних координатах
def show_2_plots(df, df2, feature, type='hist', new_bins=0, new_hue=None, 
                df_label='Тренировочная выборка', df2_label='Тестовая выборка',
                main_title=None, new_stat='count', new_common_norm=True, new_kde=True):
    """
    Выводит в общем окне два графика для визуализации распределения и разброса данных.

    Параметры:
    df (pd.DataFrame): DataFrame с данными.
    df2 (pd.DataFrame): Второй DataFrame для сравнения.
    feature (str): Название признака для визуализации.
    type (str, optional): 'hist' - Выводит гистограмму и горизонтальную диаграмму размаха.
                                   Используется по умолчанию.
                          'bars' - Выводит cтолбчатую диаграмму частот и горизонтальную диаграмму размаха.
    new_bins (int, optional): Количество корзин для гистограммы. 
                              Если 0, используется значение по умолчанию
                              и происходит автоматический подбор количества корзин.
    new_hue (str, optional): Название признака для категоризации.
                             По умолчанию - None
    df_label (str, optional): Метка для первого DataFrame на графике.
    df2_label (str, optional): Метка для второго DataFrame на графике.
    title (str, optional): Общий заголовок.
    new_stat (str, optional): По умолчанию - 'count'
    new_common_norm (bool, optional): По умолчанию - True
    new_kde (bool, optional): По умолчанию - True
    """
    
    # Задаем количество знаков после запятой в зависимости
    if abs(df[feature].max()) > 1000:
        rnd = 0
    elif abs(df[feature].max()) > 100:
        rnd = 1
    elif abs(df[feature].max()) > 10:
        rnd = 2
    elif abs(df[feature].max()) > 1:
        rnd = 3
    else:
        rnd = 4
   
    fig = plt.figure(figsize=(12, 10))
    gs = fig.add_gridspec(2, 2)

    if main_title != None:
        fig.text(0.5, 1, main_title, ha='center', fontsize=12)

    if type=='hist':
        # Гистограмма
        ax1 = fig.add_subplot(gs[ : , 0])
        if new_bins == 0:
            sns.histplot(x=feature, data=df.dropna(subset=[feature]), kde=new_kde, color='#a1c9f4', hue=new_hue, 
                         label=df_label, alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
            sns.histplot(x=feature, data=df2.dropna(subset=[feature]), kde=new_kde, color='#ffb482', hue=new_hue, 
                         label=df2_label, alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
        else:
            sns.histplot(x=feature, data=df.dropna(subset=[feature]), kde=new_kde, color='#a1c9f4', hue=new_hue, 
                         bins=new_bins, label=df_label, alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
            sns.histplot(x=feature, data=df2.dropna(subset=[feature]), kde=new_kde, color='#ffb482', hue=new_hue, 
                         bins=new_bins, label=df2_label, alpha=0.6, ax=ax1, stat=new_stat, common_norm=new_common_norm)
        ax1.set_title(f'Гистограмма для {feature}')
        ax1.set_xlabel(feature)
        if new_stat=='count':
            ax1.set_ylabel('Количество')
        else:
            ax1.set_ylabel('Плотность распределения')
        ax1.legend()

    elif type=='bars':
        # Столбчатая диаграмма частот
        ax1 = fig.add_subplot(gs[ : , 0])
        sns.countplot(x=feature, data=df.dropna(subset=[feature]), edgecolor="black", color='#a1c9f4', 
                      hue=new_hue, label=df_label, alpha=0.6, ax=ax1)
        sns.countplot(x=feature, data=df2.dropna(subset=[feature]), edgecolor="black", color='#ffb482', 
                      hue=new_hue, label=df2_label, alpha=0.6, ax=ax1)
        ax1.set_title(f'Диаграмма частот для {feature}')
        ax1.set_xlabel(feature)
        ax1.set_ylabel('Количество')
        
        ### Округляем значения по оси X
        labels = [item.get_text() for item in ax1.get_xticklabels()] # Получаем текущие метки по оси X (строки)
        new_labels = []
        for label in labels:
            try:
                num = float(label) # Преобразуем строки в float
                new_labels.append(str(round(num, 3))) # округляем до 3х знаков
            except ValueError:
                new_labels.append(label)  # если не число — оставляем как есть
        ax1.set_xticklabels(new_labels)
        ###
        
        ax1.legend()

    else:
        ax1 = fig.add_subplot(gs[ : , 0])
        ax1.set_title('Неправильно задан параметр type')

    # Горизонтальная диаграмма размаха (Boxplot) Тренировочная выборка
    ax2 = fig.add_subplot(gs[0, 1])
    sns.boxplot(x=df[feature].dropna(), 
                orient='h', 
                color='#b5d9ff', 
                width=0.2,
                ax=ax2)
    ax2.set_title(f'Диаграмма размаха для {feature}. {df_label}')
    ax2.set_xlabel(feature)

    data = df[feature].dropna()

    # Извлечение статистики
    quartiles = np.percentile(data, [25, 50, 75])  # Q1, медиана, Q3
    q1, median, q3 = quartiles
    iqr = q3 - q1
    lower_whisker = max(min(data), q1 - 1.5 * iqr)
    upper_whisker = min(max(data), q3 + 1.5 * iqr)
    outliers = [x for x in data if x < lower_whisker or x > upper_whisker]

    # Подписываем значения через annotate с поворотом текста
    values = []
    for value, label in zip([q1, median, q3, lower_whisker, upper_whisker],
                            ['Q1', 'Медиана', 'Q3', 'Мин', 'Макс']):
        if value in values:
            shift = -0.15
        else:
            shift = 0.45
        values.append(value)
        ax2.annotate(f"{label}: {value:.{rnd}f}",
                    xy=(value, 0),
                    xytext=(value, shift),
                    textcoords='data',
                    ha='center',
                    fontsize=9,
                    rotation=90)

    # Отметка выбросов
    for outlier in outliers:
        ax2.annotate(f"Выброс: {outlier:.{rnd}f}",
                    xy=(outlier, 0),
                    xytext=(outlier, -0.15),
                    textcoords='data',
                    ha='center',
                    fontsize=9,
                    color='red',
                    rotation=90)

    # Добавление среднего значения
    mean_value = data.mean()
    ax2.annotate(f"Среднее: {mean_value:.{rnd}f}",
                xy=(mean_value, 0),
                xytext=(mean_value, -0.15),
                textcoords='data',
                ha='center',
                fontsize=9,
                color='blue',
                rotation=90)

    # Добавление количества выбросов
    ax2.annotate(f'Количество выбросов: {len(outliers)}',
                xy=(data.min(), -0.45),
                xytext=(data.min(), -0.45),
                textcoords='data',
                ha='left',
                fontsize=10,
                color='purple')

    # Настройка цветов линий коробки через Matplotlib
    for line in ax2.artists:
        line.set_edgecolor('blue')  # Цвет линий коробки


    # Горизонтальная диаграмма размаха (Boxplot) Тестовая выборка
    ax3 = fig.add_subplot(gs[1, 1])
    sns.boxplot(x=df2[feature].dropna(), 
                orient='h', 
                color='#b5d9ff', 
                width=0.2,
                ax=ax3)
    ax3.set_title(f'Диаграмма размаха для {feature}. {df2_label}')
    ax3.set_xlabel(feature)

    data = df2[feature].dropna()

    # Извлечение статистики
    quartiles = np.percentile(data, [25, 50, 75])  # Q1, медиана, Q3
    q1, median, q3 = quartiles
    iqr = q3 - q1
    lower_whisker = max(min(data), q1 - 1.5 * iqr)
    upper_whisker = min(max(data), q3 + 1.5 * iqr)
    outliers = [x for x in data if x < lower_whisker or x > upper_whisker]

    # Подписываем значения через annotate с поворотом текста
    values = []
    for value, label in zip([q1, median, q3, lower_whisker, upper_whisker],
                            ['Q1', 'Медиана', 'Q3', 'Мин', 'Макс']):
        if value in values:
            shift = -0.15
        else:
            shift = 0.45
        values.append(value)
        ax3.annotate(f"{label}: {value:.{rnd}f}",
                    xy=(value, 0),
                    xytext=(value, shift),
                    textcoords='data',
                    ha='center',
                    fontsize=9,
                    rotation=90)

    # Отметка выбросов
    for outlier in outliers:
        ax3.annotate(f"Выброс: {outlier:.{rnd}f}",
                    xy=(outlier, 0),
                    xytext=(outlier, -0.15),
                    textcoords='data',
                    ha='center',
                    fontsize=9,
                    color='red',
                    rotation=90)

    # Добавление среднего значения
    mean_value = data.mean()
    ax3.annotate(f"Среднее: {mean_value:.{rnd}f}",
                xy=(mean_value, 0),
                xytext=(mean_value, -0.15),
                textcoords='data',
                ha='center',
                fontsize=9,
                color='blue',
                rotation=90)

    # Добавление количества выбросов
    ax3.annotate(f'Количество выбросов: {len(outliers)}',
                xy=(data.min(), -0.45),
                xytext=(data.min(), -0.45),
                textcoords='data',
                ha='left',
                fontsize=10,
                color='purple')

    # Настройка цветов линий коробки через Matplotlib
    for line in ax3.artists:
        line.set_edgecolor('blue')  # Цвет линий коробки
    
    
    # Показ графика
    plt.tight_layout()
    plt.show()
    
# Функция для вывода круговой диаграммы
def show_pie(df, feature, df_label='Круговая диаграмма'):
    df[feature].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        colors=sns.color_palette('pastel'),
        figsize=(6, 6),
        ylabel=''  # убирает подпись оси Y
    )
    plt.title(df_label)
    plt.show()
    
# Функция для вывода круговых диаграмм для категориальных признаков по две в ряд
def show_pies(df1, features, threshold = 0.01):
    """
    Выводит круговые диаграммы для категориальных признаков по две в ряд.

    Параметры:
    df (pd.DataFrame): 
        DataFrame с данными.
    features (list): 
        Список категориальных признаков, для которых строятся круговые диаграммы
    threshold (int): 
        Порог для объединения в кетегорию 'Другое'
    """
    
    lines = math.ceil(len(features) / 2.0)
    
    fig = plt.figure(figsize=(12, 5.5 * lines))
    gs = fig.add_gridspec(lines, 2)

    fig.text(0.5, 1 + 0.05 / lines, f'Круговые диаграммы для категориальных признаков', ha='center', fontsize=12)
    
    line = 0
    column = False

    for feature in features:
        
        ax1 = fig.add_subplot(gs[line, int(column)])
        
        column = not column
        if column == False:
            line += 1
        
        # Круговая диаграмма
        value_counts = df1[feature].value_counts(normalize=True)

        # Определяем редкие категории
        rare_categories = value_counts[value_counts < threshold].index

        # Заменяем редкие категории на 'другое'
        temp_df = df1[feature].copy()
        temp_df[feature] = df1[feature].apply(lambda x: 'Другое' if x in rare_categories else x)
        
        #df1[feature].value_counts().plot(
        temp_df[feature].value_counts().plot(
        #value_counts.plot(
            kind='pie',
            autopct='%1.1f%%',
            colors=sns.color_palette('pastel'),
            ax=ax1
        )
        ax1.set_title(feature)
        ax1.set_ylabel(None)
        
    # Показ графика
    plt.tight_layout()
    plt.show()

    
# Функция для вывода круговых диаграмм двух таблиц с одинаковыми признаками
def show_2_pies(df1, df2, features, df_label='Тренировочная выборка', df2_label='Тестовая выборка'):
    """
    Выводит парные круговые диаграммы для категориальных признаков из двух датафреймов.

    Параметры:
    df (pd.DataFrame): 
        DataFrame с данными.
    df2 (pd.DataFrame): 
        Второй DataFrame для сравнения.
    features (list): 
        Список категориальных признаков, для которых строятся круговые диаграммы
    df_label (str, optional): 
        Метка для первого DataFrame на графике 
        по умолчанию 'Тренировочная выборка'
    df2_label (str, optional): 
        Метка для второго DataFrame на графике 
        по умолчанию 'Тестовая выборка'
    """
    
    lines = len(features)
    
    fig = plt.figure(figsize=(12, 5 * lines))
    gs = fig.add_gridspec(lines, 2)
    
    count = 0
    for feature in features:
        
        ax1 = fig.add_subplot(gs[count, 0])
        ax2 = fig.add_subplot(gs[count, 1])

        fig.text(0.5, 1 - (count) / (lines), f'Круговые диаграммы для {feature}', ha='center', fontsize=12)
        
        count += 1
        
        # Круговая диаграмма для первого датафрейма
        df1[feature].value_counts().plot(
            kind='pie',
            autopct='%1.1f%%',
            colors=sns.color_palette('pastel'),
            ax=ax1
        )
        ax1.set_title(df_label)
        ax1.set_ylabel(None)

        # Круговая диаграмма для второго датафрейма
        df2[feature].value_counts().plot(
            kind='pie',
            autopct='%1.1f%%',
            colors=sns.color_palette('pastel'),
            ax=ax2
        )
        ax2.set_title(df2_label)
        ax2.set_ylabel(None) 
        
    # Показ графика
    plt.tight_layout()
    plt.show()
    
# Функция для вывода текстового описания уровней корреляции между признакими по убыванию
def print_corr_levels(corr_matrix, threshold = 0.0):
    corr_list = []
    for row in corr_matrix.columns:
        for col in corr_matrix.columns:
            if row < col:
                corr_value = corr_matrix.loc[row, col]
                if abs(corr_value) > 0.9 and abs(corr_value) > threshold:
                    temp_tuple = (f"Весьма высокая корреляция между {row} и {col}:", round(corr_value, 3))
                    corr_list.append(temp_tuple)
                elif abs(corr_value) > 0.7 and abs(corr_value) > threshold:
                    temp_tuple = (f"Высокая корреляция между {row} и {col}:", round(corr_value, 3))
                    corr_list.append(temp_tuple)
                elif abs(corr_value) > 0.5 and abs(corr_value) > threshold:
                    temp_tuple = (f"Заметная корреляция между {row} и {col}:", round(corr_value, 3))
                    corr_list.append(temp_tuple)
                elif abs(corr_value) > 0.3 and abs(corr_value) > threshold:
                    temp_tuple = (f"Умеренная корреляция между {row} и {col}:", round(corr_value, 3))
                    corr_list.append(temp_tuple)
                elif abs(corr_value) > 0.1 and abs(corr_value) > threshold:
                    temp_tuple = (f"Слабая корреляция между {row} и {col}:", round(corr_value, 3))
                    corr_list.append(temp_tuple)
    corr_list = sorted(corr_list, key=lambda x: x[1], reverse=True)
    return corr_list