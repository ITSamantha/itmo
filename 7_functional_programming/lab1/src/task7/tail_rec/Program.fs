module task7tailrec

let isPrimeNumber (number: int) : bool =
    let rec check (i: int) : bool =
        if number <= 1 then false
        elif number = 2 then true
        elif i * i > number then true
        elif number % i = 0 then false
        else check (i + 1)

    check 2

let boolToInt (value: bool) : int = if value then 1 else 0

let findNthPrime (n: int) : int =
    let rec findPrime (count: int) (candidate: int) : int =
        let isPrime = isPrimeNumber (candidate)
        let nextCount = count + boolToInt isPrime

        if nextCount = n then
            candidate
        else
            findPrime (nextCount) (candidate + 1)

    findPrime 0 2


[<EntryPoint>]
let main _ =
    let result: int = findNthPrime 10001
    printfn "%d" result
    0
