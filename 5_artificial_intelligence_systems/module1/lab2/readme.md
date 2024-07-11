# Лабораторная работа 2. Создание онтологии в Protege

Целью этой лабораторной работы является знакомство со средой разработки онтологий Protege и перевод базы знаний, созданной в предыдущей лабораторной работе в онтологическую форму в Protege.

## Задание

Преобразовать факты и отношения из Prolog в концепты и свойства в онтологии. Описать классы и свойства в онтологии, которые соответствуют объектам и отношениям из базы знаний. Например, если у были классы "Человек" и "Машина" и свойство "возраст", создайте аналогичные классы и свойства в онтологии в Protege.

## Критерии оценки

- Корректное создание онтологии в Protege на основе базы знаний в Prolog.
- Качество перевода фактов, предикатов и отношений из Prolog в онтологию.
- Определение классов, свойств и иерархии классов в Protege.
- Тестирование онтологии и демонстрация ее функциональности.

## Реализация

### Отобразим факты базы знаний на предикаты онтологии (ObjectProperties/DataProperties)

*Object Properties:*
- ![1](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/a6ebf0a6-e466-41ca-998d-40e4cb071c89)
- ![2](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/0c0041d5-3ef7-46e1-887b-2fcf8d16a03d)
- ![3](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/6fe0defe-97b9-4585-b535-a2488a258815)
- ![4](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/67018a20-b23f-4f68-81bc-d9155d971a05)

*Data properties:*
- ![1](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/fe5917d2-92e8-43eb-9e63-5a8222d73945)
- ![2](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/5a0af787-ed9f-4e89-a2b4-8b2116b77ad8)
- ![3](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/8f10caf2-119e-49f6-bbc7-21cebf85aefb)
- ![4](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/52791ea7-1d5a-47bb-ae7f-83a6a6e00bc3)

### Отобразим сущности онтологии (Entities)
- ![1](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/f0157c79-aeae-4543-bac4-a1c27d1cbb78)
- ![2](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/417ffbad-5a7b-4b48-825f-74ae4fd185e2)
- ![3](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/b7bb9cd8-204f-4658-8309-b6434c90d304)
- ![4](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/8dd87052-1d7c-4f9a-b9c3-66e8be26e69f)
- ![5](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/8b759399-9833-4575-a322-98d415687d80)
- ![6](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/18ef538a-f406-43aa-9ebf-e8dd47e81a8c)
- ![7](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/69cef002-89c3-4d16-93d2-022a84b18d06)
- ![8](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/f660daec-fe97-4527-abde-47bdea41946f)

### Отобразим граф онтологии (Entities)
![photo_2023-09-28_22-49-44](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/f21b036d-89a3-4886-95d3-52007737f21f)

### Отобразим индивидуалов каждого типа онтологии (Individuals)
- ![1](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/8291f55d-8cd6-410f-9a6d-a1a7da95ded2)
- ![2](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/6025738f-0d8e-4025-b23b-e5dc66899374)
- ![3](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/bc713a9e-0b0f-4aab-ba24-2d9c5b164459)
- ![4](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/08ceaa46-e48d-4305-a40d-12d2873f16e8)
- ![5](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/a91628f4-bf3c-4a6c-b23b-668f3b0ef7ac)

### Отобразим правила (Rules)
- ![1](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/74163b48-b00a-4a37-8729-e9df60a79a5d)

### Запустим Reasoner и выполним DL Query
## Тесты (Запросы)
- MainCharacter
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/54d06ccb-7dae-4d96-940b-730b1cfbd0c9)
- hasMainCharacter value Crewmember
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/a4f6f27f-11ca-4da4-984b-1ff11a8be717)
- VideoGame
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/7af6da5b-d6c0-42c0-ae4f-68b508cb7e5a)
- hasGenre value Action-Adventure
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/29ef018d-025f-4447-ba9b-c4ce9a50861c)
- hasMechanic value Open_world
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/f4d5ab73-59f1-4e30-b7db-b4f4789a7170)
- VideoGame or Genre
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/a34b0985-12a6-4294-9962-42d2e045e475)
- VideoGame and Genre
![image](https://github.com/ITSamantha/Artificial_Intelligence_Systems/assets/100091168/358615b5-e5a3-4c85-9bff-a1d340b47e44)

## Правила (Запросы)
% Правило 1. Игра c высокой оценкой, если её рейтинг выше 8.5.
VideoGame and hasRating only xsd:float[ >= 8.5]

% Правило 2. Список всех видеоигр.
VideoGame

% Правило 3. Игра является "старой", если она была выпущена до 2010 года.
VideoGame and not (hasReleaseYear only xsd:int[ >= 2010])

% Правило 5. Игра X поддерживает определенный тип игры Y.
VideoGame and hasType value Single_player

% Правило 6. Получить список всех высоко оцененных игр
VideoGame and hasRating only xsd:float[ >= 8.5]

% Правило 7. Получить список игр определенного жанра.
VideoGame and hasGenre value RPG

% Правило 8. Список игр, рекомендуемых для взрослых (18+).
hasAgeLimit only xsd:integer[ >= 18]

% Правило 9. Список игр, которые считаются "классикой". "Классические игры" - это те, которые были выпущены более 20 лет назад и имеют высокий рейтинг.
VideoGame and (hasRating only xsd:float[ >= 8.5]) and (hasReleaseYear only xsd:int[ <= 2003])


## Вывод
В результате работы я создала онтологию в Protege на основе базы знаний в Prolog путём отображения фактов, предикатов и отношений из Prolog в онтологию. Также я выполнил запросы в онтологию для обнаружения скрытых фактов.
