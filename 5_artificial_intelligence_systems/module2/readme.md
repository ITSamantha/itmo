# Лабораторная работа 1. Метод линейной регрессии
[Отчёт по лабораторной работе № 4](https://github.com/ITSamantha/artificial_intelligence_systems/blob/main/module2/lab4/report_readme.md)

# *Лабораторная работа 2. Метод k-ближайших соседей (k-NN)*
[Отчёт по лабораторной работе № 5](https://github.com/ITSamantha/artificial_intelligence_systems/blob/main/module2/lab5/report_readme.md)

# *Лабораторная работа 3. Деревья решений*
[Отчёт по лабораторной работе № 6](https://github.com/ITSamantha/artificial_intelligence_systems/blob/main/module2/lab6/report_readme.md)

# *Лабораторная работа 4. Логистическая регрессия*
[Отчёт по лабораторной работе № 7](https://github.com/ITSamantha/artificial_intelligence_systems/blob/main/module2/lab7/report_readme.md)

# *Сравнение методов*
## Сравнительный анализ методов
1. *Линейная регрессия*

   _Преимущества:_
      - Простота и интерпретируемость: Линейная регрессия легко понимается и интерпретируется, что делает ее полезной для начального анализа данных.
      - Эффективность при линейных зависимостях: Хорошо работает, когда зависимость между признаками и целевой переменной линейная.
   
   _Ограничения:_
      - Ограничение на сложность: Не способна моделировать сложные нелинейные зависимости в данных.
      - Чувствительность к выбросам: Выбросы могут сильно влиять на результаты линейной регрессии.
  

   _Результаты:_
      - Линейная регрессия хорошо справляется с задачами, где существует линейная зависимость между признаками и целевой переменной.
      - Она может предсказывать непрерывные значения, что полезно для задач регрессии.

   _Производительность:_
      - Линейная регрессия имеет низкую вычислительную сложность и может работать быстро, даже с большими объемами данных.
      - Ее интерпретируемость позволяет анализировать вклад каждого признака в предсказания.
        
  *Производительность модели, обученной по данному алгоритму, является значением модели со средним уровнем обученности для задачи данных о жилье в Калифорнии (0.6-0.7).*

2. *Метод k-ближайших соседей*

    _Преимущества:_
      - Не требует предположений о структуре данных: k-NN не делает предположений о распределении данных и может хорошо работать для различных типов задач.
      - Простота реализации: Легко реализуется и понимается.
   
   _Ограничения:_
      - Вычислительная сложность: При больших объемах данных и больших значениях k (количество соседей) алгоритм может стать медленным.
      - Чувствительность к выбору метрики и значения k: Выбор подходящей метрики и значения k важен и может сильно влиять на результаты.


   _Результаты:_
      - k-NN может быть эффективным методом для задач классификации, особенно в случаях, когда классы имеют сложную структуру и нелинейные зависимости.
      - Он может хорошо справляться с аномалиями в данных.

   _Производительность:_
      - k-NN может быть вычислительно затратным при большом количестве признаков и/или больших объемах данных.
      - Выбор значения k и метрики расстояния важен и требует настройки.

*Производительность модели, обученной по данному алгоритму, является значением модели с высоким уровнем обученности для задачи данных о вине (1.0).*
  
3. *Деревья решений*

   _Преимущества:_
      - Способность учитывать нелинейные зависимости: Деревья решений могут хорошо моделировать сложные нелинейные зависимости в данных.
      - Интерпретируемость: Деревья решений можно визуализировать и интерпретировать, что позволяет объяснить принятое решение.
   
   _Ограничения:_
      - Склонность к переобучению: Деревья могут легко переобучаться на обучающих данных, что может снизить их обобщающую способность.
      - Нестабильность: Малые изменения в данных могут привести к существенным изменениям в структуре дерева.


   _Результаты:_
      - Деревья решений хорошо моделируют сложные, нелинейные зависимости в данных.
      - Они могут использоваться для задач классификации и регрессии.
   
   _Производительность:_
      - Деревья решений могут быть подвержены переобучению, особенно если они слишком глубокие. Необходимо использовать методы для контроля глубины дерева.
      - Деревья могут быть нестабильными и чувствительными к небольшим изменениям в данных.
        
   *Производительность модели, обученной по данному алгоритму, является значением модели с высоким уровнем обученности для задачи данных о классификации грибов (1.0). Возможно переобучение модели.*
        
5. *Логистическая регрессия*

   _Преимущества:_
      - Подходит для задач классификации: Логистическая регрессия хорошо подходит для бинарной и многоклассовой классификации.
      - Работает с вероятностями: Модель предсказывает вероятности принадлежности к классам.
    
    _Ограничения:_
      - Подразумевает линейность: Логистическая регрессия предполагает линейные зависимости между признаками и логарифмом отношения вероятностей, поэтому не подходит для данных с сильными нелинейными зависимостями.
      - Чувствительность к мультиколлинеарности: Если признаки сильно коррелируют, модель может быть нестабильной.
   

   _Результаты:_
      - Логистическая регрессия является мощным методом для задач классификации, особенно в бинарной классификации.
      - Она предсказывает вероятности принадлежности к классам, что полезно для ранжирования и оценки уверенности в классификации.

   _Производительность:_
      - Логистическая регрессия обычно имеет низкую вычислительную сложность и работает быстро.
      - Она может быть чувствительной к мультиколлинеарности между признаками.

   *Производительность модели, обученной по данному алгоритму, является значением модели со средним уровнем обученности для задачи данных о диабете (0.8-0.85).*

*Точность классификации:*

![image](https://github.com/ITSamantha/artificial_intelligence_systems/assets/100091168/a509b425-e591-401f-92fa-74e74a5b31cd)

*Время обучения:*

![image](https://github.com/ITSamantha/artificial_intelligence_systems/assets/100091168/187fefdc-e693-484d-8fd1-638f72b402db)

*_http://www.vestnik.vsu.ru/pdf/analiz/2018/03/2018-03-19.pdf_

## Примеры лучшего использования каждого метода

1. Линейная регрессия наиболее эффективна, когда существует линейная зависимость между признаками и целевой переменной, и когда простота и интерпретируемость модели важны. Например, это может быть использовано для прогнозирования цен на недвижимость, дохода населения, объема продаж товаров и услуг, а также анализа финансовых данных и эконометрики.

2. Метод k-ближайших соседей (k-NN) часто наиболее эффективен в задачах классификации, особенно при сложной структуре классов и отсутствии четкой линейной зависимости между признаками. Примеры включают распознавание образцов, системы рекомендаций, детекцию аномалий и медицинские диагностику.

3. Деревья решений хорошо подходят, когда данные содержат сложные нелинейные зависимости и правила, которые можно извлечь из них. Это может быть использовано для прогнозирования тенденций в рынке, выявления факторов, влияющих на клиентскую лояльность, анализа медицинских данных и разработки систем рекомендаций.

4. Логистическая регрессия эффективна в задачах классификации, особенно бинарной, и когда важно иметь возможность оценивать вероятности принадлежности к классам. Примеры включают медицинские диагностику, фильтрацию спама в электронной почте, кредитный скоринг и анализ тональности текстов.

*Важно адаптировать выбор метода к конкретным характеристикам задачи и данных, чтобы добиться наилучших результатов.*

# Заключение
Каждый метод имеет свои сильные и слабые стороны, и выбор метода зависит от характера данных и задачи классификации.

- Линейная регрессия и логистическая регрессия подходят для задач с линейной зависимостью между признаками и целевой переменной.

- Метод k-ближайших соседей может использоваться в случаях нелинейных зависимостей.

- Деревья решений могут быть полезны для задач, где интерпретируемость играет важную роль и необходимо учитывать разнообразные признаки.

Итак, выбор метода должен базироваться на конкретных особенностях задачи и данных, а также на требованиях к интерпретируемости и производительности модели.

# Приложения 

- *[Лабораторная работа № 1](https://github.com/ITSamantha/artificial_intelligence_systems/tree/main/module2/lab4)*
- *[Лабораторная работа № 2](https://github.com/ITSamantha/artificial_intelligence_systems/tree/main/module2/lab5)*
- *[Лабораторная работа № 3](https://github.com/ITSamantha/artificial_intelligence_systems/tree/main/module2/lab6)*
- *[Лабораторная работа № 4](https://github.com/ITSamantha/artificial_intelligence_systems/tree/main/module2/lab7)*
