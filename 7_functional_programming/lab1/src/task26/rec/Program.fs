module task26rec

let cycleLength d =
    let rec findCycle pos remainders rem =
        match Map.tryFind rem remainders with
        | Some (start) -> pos - start
        | None ->
            let nextRem = (rem * 10) % d

            if nextRem = 0 then
                0
            else
                findCycle (pos + 1) (Map.add rem pos remainders) nextRem

    findCycle 0 Map.empty 1


let rec findMaxCycleRec  d limit maxD maxLen =
    if d >= limit then maxD
    else
        let cycle = cycleLength d
        if cycle > maxLen then findMaxCycleRec  (d + 1) limit d cycle
        else findMaxCycleRec  (d + 1) limit maxD maxLen

[<EntryPoint>]
let main _ =
    let result = findMaxCycleRec 1 1000 1 0
    printfn "%d" result
    0
