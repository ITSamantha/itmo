module task7rec

let isPrimeNumber (number: int) : bool =
    let rec check (i: int) : bool =
        if number <= 1 then false
        elif number = 2 then true
        elif i * i > number then true
        elif number % i = 0 then false
        else check (i + 1)

    check 2

let rec findNthPrime (n: int) (current: int) (count: int) =
    if count = n then
        current
    else
        let nextPrime = current + 1

        if isPrimeNumber nextPrime then
            findNthPrime n nextPrime (count + 1)
        else
            findNthPrime n nextPrime count

[<EntryPoint>]
let main _ =
    let result: int = findNthPrime 10001 1 0
    printfn "%d" result
    0
