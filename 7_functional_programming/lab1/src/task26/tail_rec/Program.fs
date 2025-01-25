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

[<EntryPoint>]
let main (_: string[]) : int =
    let result = findMaxCycleTailRec 1000 1 1 0
    printfn "%d" result
    0