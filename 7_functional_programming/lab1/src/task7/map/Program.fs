module task7map

let isPrimeNumber (number: int) : bool =
    let rec check (i: int) : bool =
        if number <= 1 then false
        elif number = 2 then true
        elif i * i > number then true
        elif number % i = 0 then false
        else check (i + 1)

    check 2

let findNthPrime (n: int) : int =
    Seq.initInfinite ((+) 2)
    |> Seq.filter isPrimeNumber
    |> Seq.map (fun x -> x)           
    |> Seq.take n
    |> Seq.last

[<EntryPoint>]
let main _ =
    let result = findNthPrime 10001
    printfn "%d" result
    0
