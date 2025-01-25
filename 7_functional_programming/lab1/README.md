# Лабораторная работа №1

Выполнила: Савельева Диана Александровна, P34082, 388291

Вариант: 7, 26

## Задание
Цель: освоить базовые приёмы и абстракции функционального программирования: функции, поток управления и поток данных, сопоставление с образцом, рекурсия, свёртка, отображение, работа с функциями как с данными, списки.

## Описание проблемы и комментарии

### Задача №7

Для данной задачи написано несколько реализаций.
Полный код различных реализаций представлен в директории src. Ниже продемонстрированы кусочки кода, явно использующие необходимые подходы. Тесты для задач находятся в директории tests.

```
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13 we can see that the 6th prime is 13.

What is the 10001st prime number?
```

Описана вспомогательная функция для определения, простое ли число:
```
let isPrimeNumber (number: int) : bool =
    let rec check (i: int) : bool =
        if number <= 1 then false
        elif number = 2 then true
        elif i * i > number then true
        elif number % i = 0 then false
        else check (i + 1)

    check 2
```


#### Хвостовая рекурсия
```
let findNthPrime (n: int) : int =
    let rec findPrime (count: int) (candidate: int) : int =
        let isPrime = isPrimeNumber (candidate)
        let nextCount = count + boolToInt isPrime

        if nextCount = n then
            candidate
        else
            findPrime (nextCount) (candidate + 1)

    findPrime 0 2
```

#### Фильтрация
```
let findNthPrime (n: int) : int =
    let primesSeq =
        Seq.initInfinite ((+) 2)
        |> Seq.filter isPrimeNumber
        |> Seq.take n        
        |> Seq.last
    
    primesSeq
```

#### Бесконечная последовательность
```
let findNthPrime (n: int) : int =
    let primesSeq =
        Seq.initInfinite ((+) 2)
        |> Seq.filter isPrimeNumber         
    primesSeq |> Seq.item (n - 1)           
```

#### Map (для данной задачи не очень применимо)
```
let findNthPrime (n: int) : int =
    Seq.initInfinite ((+) 2)
    |> Seq.filter isPrimeNumber
    |> Seq.map (fun x -> x)           
    |> Seq.take n
    |> Seq.last
```

### Задача №26

Для данной задачи написано несколько реализаций.
Полный код различных реализаций представлен в директории src. Ниже продемонстрированы кусочки кода, явно использующие необходимые подходы. Тесты для задач находятся в директории tests.

```
A unit fraction contains in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666... and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
```

Описана вспомогательная функция для определения длины "цикла":

```
let cycleLength (d: int) : int =
    let rec findCycle (pos: int) (remainders: Map<int, int>) (rem: int) : int =
        match Map.tryFind rem remainders with
        | Some (start) -> pos - start
        | None ->
            let nextRem = (rem * 10) % d

            if nextRem = 0 then
                0
            else
                findCycle (pos + 1) (Map.add rem pos remainders) nextRem

    findCycle 0 Map.empty 1
```

#### Хвостовая рекурсия
```
let rec findMaxCycleTailRec (n: int) (d: int) (maxD: int) (maxLen: int) : int =
    if d >= n then
        maxD
    else
        let len = cycleLength d

        let newMaxD, newMaxLen =
            if len > maxLen then
                d, len
            else
                maxD, maxLen

        findMaxCycleTailRec n (d + 1) newMaxD newMaxLen
```

#### Фильтрация
```
let findMaxCycleRec (candidates: List<int>) : int =
    candidates |> List.maxBy cycleLength

[<EntryPoint>]
let main (_: string[]) : int =
    let candidates = [ 1..999 ]
    let result = findMaxCycleRec candidates
    printfn "%d" result
    0
```

#### Бесконечная последовательность
```
let recCycleSeq = Seq.initInfinite ((+) 1)

    let result =
        recCycleSeq
        |> Seq.take 999
        |> Seq.maxBy cycleLength
```

#### Map
```
[<EntryPoint>]
let main _ =
    let candidates = [1..999]
    let cycleLengthsMap = candidates |> List.map (fun d -> (d, cycleLength d))
    let result= cycleLengthsMap |> List.maxBy snd |> fst
    printfn "%d" result
    0
```

# Заключение
В процессе выполнения лабораторной работы были освоены ключевые принципы функционального программирования. Удалось поработать с рекурсией, ленивыми коллекциями, а также освоить базово тестирование в F#. Эти принципы оказались очень полезными при решении задач, связанных с вычислением циклов в дробях и поиском простых чисел (соответстующее моим задачам).

Было интересно поработать с множеством разных методов решения одной и той же проблемы, а также понаблюдать за изменением времени исполнения программы. 

Особенности, которые я отметила для себя:
- В F# понравилось работать с модулем Seq, предоставляющим методы для работы с последовательностями. Хотелось бы выделить initInfinite (генерация бесконечной последовательности), а также функцию filter.
- Удобная работа с рекурсией (даже есть ключевое слово rec).
- Довольно простая реализация тестирования для функций (NUnit).
- Довольно сложная настройка и сборка у dotnet платформы. В том числе и для тестов.
- Тяжело реализовывать алгоритмическую задачу по заданному "паттерну". Обычно хочется реализовать как можно более эффективно...

Итог:
- Самым интересным мне показался вариант с бесконечной последовательностью и фильтрацией.
- Самым простым - код на Python. Так как я на нём обычно пишу:)

