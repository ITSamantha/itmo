module task26module

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

let findMaxCycleRec (candidates: List<int>) : int =
    candidates |> List.maxBy cycleLength

[<EntryPoint>]
let main (_: string[]) : int =
    let candidates = [ 1..999 ]
    let result = findMaxCycleRec candidates
    printfn "%d" result
    0