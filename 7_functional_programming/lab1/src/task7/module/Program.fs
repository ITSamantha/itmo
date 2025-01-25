module task7module

let isPrimeNumber (number: int) : bool =
    let rec check (i: int) : bool =
        if number <= 1 then false
        elif number = 2 then true
        elif i * i > number then true
        elif number % i = 0 then false
        else check (i + 1)

    check 2

let findNthPrime (n: int) : int =
    let primesSeq =
        Seq.initInfinite ((+) 2)
        |> Seq.filter isPrimeNumber
        |> Seq.take n        
        |> Seq.last
    
    primesSeq

[<EntryPoint>]
let main _ =
    let result = findNthPrime 10001
    printfn "%d" result
    0