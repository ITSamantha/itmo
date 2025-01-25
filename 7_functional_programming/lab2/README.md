# Лабораторная работа №2

Выполнила: Савельева Диана Александровна, P34082, 388291

Вариант: oa-dict 

Интерфейс: Dict

Структура данных: OpenAddress Hashmap

## Задание

Цель: освоиться с построением пользовательских типов данных, полиморфизмом, рекурсивными алгоритмами и средствами тестирования (unit testing, property-based testing), а также разделением интерфейса и особенностей реализации.

### Требования
1. Функции:
    - добавление и удаление элементов;
    - фильтрация;
    - отображение (map);
    - свертки (левая и правая);
    - структура должна быть моноидом.
2. Структуры данных должны быть неизменяемыми.
3. Библиотека должна быть протестирована в рамках unit testing.
4. Библиотека должна быть протестирована в рамках property-based тестирования (как минимум 3 свойства, включая свойства моноида).
5. Структура должна быть полиморфной.
6. Требуется использовать идиоматичный для технологии стиль программирования. Примечание: некоторые языки позволяют получить большую часть API через реализацию небольшого интерфейса. Так как лабораторная работа про ФП, а не про экосистему языка -- необходимо реализовать их вручную и по возможности -- обеспечить совместимость.
7. Обратите внимание:
    - API должно быть реализовано для заданного интерфейса и оно не должно "протекать". На уровне тестов -- в первую очередь нужно протестировать именно API (dict, set, bag).
    - Должна быть эффективная реализация функции сравнения (не наивное приведение к спискам, их сортировка с последующим сравнением), реализованная на уровне API, а не внутреннего представления.

## Реализация

### Функция поиска hash для ключа

Входные аргументы:
- Вместимость (максимальный размер) структуры
- Ключ

Выходные аргументы:
- hash

```
let calculateHash (maxSize: int) (key: 'Key) : int =
    (hash key) % maxSize
    |> (fun x -> if x < 0 then x + maxSize else x)
```

### Функция "Поиск ячейки"

```
let rec findCell
    (key: 'Key)
    (maxSize: int)
    (storage: ('Key * 'Value) option array)
    (currentIndex: int)
    (probeAmount: int)
    : int option =
    if probeAmount >= maxSize then
        None
    else
        match storage.[currentIndex] with
        | Some (k, _) when k = key -> Some currentIndex
        | None -> Some currentIndex
        | _ -> findCell key maxSize storage ((currentIndex + 1) % maxSize) (probeAmount + 1)
```

### Функция "Добавление элемента"

```
let rec insert (key: 'Key) (value: 'Value) (map: OpenAddressHashMap<'Key, 'Value>) : OpenAddressHashMap<'Key, 'Value> =
    if float map.Size / float map.MaxSize = 1 then
        let newMaxSize = map.MaxSize * 2
        let newStorage = Array.create newMaxSize None

        let newMap =
            { MaxSize = newMaxSize
              Storage = newStorage
              Size = map.Size }

        insert key value newMap
    else
        match findCell key map.MaxSize map.Storage (calculateHash map.MaxSize key) 0 with
        | Some currentIndex ->
            let newStorage = Array.copy map.Storage
            newStorage.[currentIndex] <- Some(key, value)

            { map with
                Storage = newStorage
                Size = map.Size + 1 }
        | None -> map
```

### Функция "Удаление элемента"

```
let delete (key: 'Key) (map: OpenAddressHashMap<'Key, 'Value>) : OpenAddressHashMap<'Key, 'Value> =
    match findCell key map.MaxSize map.Storage (calculateHash map.MaxSize key) 0 with
    | Some currentIndex ->
        let newStorage = Array.copy map.Storage
        newStorage.[currentIndex] <- None

        { map with
            Storage = newStorage
            Size = map.Size - 1 }
    | None -> map
```

### Функция "Фильтрация"

```
let filterMap
    (condition: ('Key * 'Value) -> bool)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let filteredItems =
        Array.fold
            (fun accumulator element ->
                match element with
                | Some (k, v) when condition (k, v) -> (k, v) :: accumulator
                | _ -> accumulator)
            []
            map.Storage

    let newHashMap =
        { MaxSize = map.MaxSize
          Storage = Array.create map.MaxSize None
          Size = 0 }

    List.fold (fun accumulator (k, v) -> insert k v accumulator) newHashMap filteredItems

```

### Функция "Свертка (левая)"

```
let foldLeft
    (aggregator: 'State -> ('Key * 'Value) -> 'State)
    (state: 'State)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : 'State =
    Array.fold
        (fun accumulator element ->
            match element with
            | Some (k, v) -> aggregator accumulator (k, v)
            | None -> accumulator)
        state
        map.Storage
```

### Функция "Свертка (правая)"

```
let foldRight
    (aggregator: ('Key * 'Value) -> 'State -> 'State)
    (state: 'State)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : 'State =
    Array.foldBack
        (fun element accumulator ->
            match element with
            | Some (k, v) -> aggregator (k, v) accumulator
            | None -> accumulator)
        map.Storage
        state
```

### Функция "Отображение"

```
let map
    (mapper: ('Key * 'Value) -> ('Key * 'Value))
    (map: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let newStorage = Array.create map.MaxSize None

    let updatedStorage =
        Array.fold
            (fun (storage: ('Key * 'Value) option array) element ->
                match element with
                | Some (k, v) ->
                    let (newKey, newValue) = mapper (k, v)

                    match findCell newKey map.MaxSize storage (calculateHash map.MaxSize newKey) 0 with
                    | Some currentIndex ->
                        storage.[currentIndex] <- Some(newKey, newValue)
                        storage
                    | None -> storage
                | None -> storage)
            newStorage
            map.Storage

    { map with Storage = updatedStorage }
```


### Структура должна быть моноидом

1. Нейтральный элемент

Создание пустой структуры.

```
let createEmptyHashMap (maxSize: int) : OpenAddressHashMap<'Key, 'Value> =
    { MaxSize = maxSize
      Storage = Array.create maxSize None
      Size = 0 }
```


2. Бинарная операция

В качестве бинарной операции используем слияние. В программе функция слияния определена как combine. Она представлена ниже.

```
let combine
    (firstHashMap: OpenAddressHashMap<'Key, 'Value>)
    (secondHashMap: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let newMaxSize = max firstHashMap.MaxSize secondHashMap.MaxSize
    let newStorage = Array.create newMaxSize None

    let insertAll (storage: ('Key * 'Value) option array) (map: OpenAddressHashMap<'Key, 'Value>) =
        Array.fold
            (fun updatedStorage element ->
                match element with
                | Some (k, v) ->
                    match findCell k newMaxSize updatedStorage (calculateHash newMaxSize k) 0 with
                    | Some currentIndex ->
                        updatedStorage.[currentIndex] <- Some(k, v)
                        updatedStorage
                    | None -> updatedStorage
                | None -> updatedStorage)
            storage
            map.Storage

    let combinedStorage = insertAll (insertAll newStorage firstHashMap) secondHashMap

    { MaxSize = newMaxSize
      Storage = combinedStorage
      Size = firstHashMap.Size + secondHashMap.Size }

```

## Демонстрационная программа

```
open System
open OpenAddressHashMap

[<EntryPoint>]
let main argv =
    let testHashMap = createEmptyHashMap 5

    let testHashMap = insert 5 "five" testHashMap
    let testHashMap = insert 2 "two" testHashMap
    let testHashMap = insert 3 "three" testHashMap

    match collectValue 5 testHashMap with
    | Some value -> printfn "Key 5: %s" value
    | None -> printfn "Key 5 not found"

    match collectValue 2 testHashMap with
    | Some value -> printfn "Key 2: %s" value
    | None -> printfn "Key 2 not found"

    match collectValue 67 testHashMap with
    | Some value -> printfn "Key 67: %s" value
    | None -> printfn "Key 67 not found"

    let testHashMap = delete 2 testHashMap

    match collectValue 2 testHashMap with
    | Some value -> printfn "Key 2: %s" value
    | None -> printfn "Key 2 not found (as expected after removal)"

    let testHashMap2 = createEmptyHashMap 5
    let testHashMap2 = insert 3 "three" testHashMap2
    let testHashMap2 = insert 4 "four" testHashMap2

    let mergedHashMap = combine testHashMap testHashMap2


    printfn "Merged dictionary contents:"

    let targetList = [ 5; 2; 3; 4 ]

    for k in targetList do
        match collectValue k mergedHashMap with
        | Some value -> printfn "Key %d" k
        | None -> ()

    let filteredHashMap = filterMap (fun (k, _) -> k % 2 = 0) testHashMap2

    printfn "Filtered dictionary (only even keys):"

    for k in targetList do
        match collectValue k filteredHashMap with
        | Some value -> printfn "Key %d: %s" k value
        | None -> ()

    let mappedHashMap = map (fun (k, (v: string)) -> (k, v.ToLower())) testHashMap2

    printfn "Mapped dictionary (values in lowercase):"

    for k in targetList do
        match collectValue k mappedHashMap with
        | Some value -> printfn "Key %d: %s" k value
        | None -> ()

    let keySum = foldLeft (fun accumulator (k, _) -> accumulator + k) 0 testHashMap2
    printfn "Sum of keys in merged dictionary: %d" keySum

    let concatenatedValues = foldRight (fun (k, v) accumulator -> accumulator + " " + v) "" mergedHashMap
    printfn "Concatenated values in merged dictionary: %s" (concatenatedValues.Trim())

    let largeMap = createEmptyHashMap 2
    let largeMap = insert 1 "one" largeMap
    let largeMap = insert 2 "two" largeMap
    let largeMap = insert 3 "three" largeMap
    printfn "\nHashMap Resize on Overflow"
    match collectValue 1 largeMap with
    | Some value -> printfn "Key 1: %s" value
    | None -> printfn "Key 1 not found"

    let mixedMap = createEmptyHashMap 5
    let mixedMap = insert "first" 1 mixedMap
    let mixedMap = insert "second" 2 mixedMap
    let mixedMap = insert "third" 3 mixedMap

    let targerList2 = ["first"; "second"; "third"]

    printfn "\nHashMap with String Keys"
    for key in targerList2  do
        match collectValue key mixedMap with
        | Some value -> printfn "Key %s: %d" key value
        | None -> printfn "Key %s not found" key

    0
```

## Тестирование

Всего было разработано 12 тестов:
- 8 unit-тестов:
- 4 property-теста:
    - Merging with an empty map returns the original map
    - Insert should correctly insert values to the map
    - Insert should work with key-value pairs of different types
    - Merge should be associative

Результат тестирования:
```
Запуск выполнения тестов; подождите...

Пройден!   : не пройдено     0, пройдено    12, пропущено     0, всего    12, длительность 383 ms. - tests.dll (net8.0)
```

Для тестирования использовались модули: 
- Nunit - Unit тестирование
- FsCheck - Property-based тестирование

## Заключение
Я изучила информацию об открытой адресации, реализовала один из её вариантов — линейное пробирование (Linear Probing). Из преимуществ отметила простоту реализации. Однако, необходимо учитывать, что при данном варианте возможны длинные последовательности занятых ячеек.

Некоторые заметки о линейном пробировании, которые хотелось бы выделить:
- Следующая позиция ищется с фиксированным шагом.
- Если при добавлении ключа обнаруживается, что место занято, пробуем следующую ячейку.

Было интересно реализовать структуру именно на языке F#, без использования ООП. Также я познакомилась с новым пакетом FsCheck, который помог добавить property-тестирование в проект.