module task26map

let cycleLength d =
    let rec findCycle pos remainders rem =
        match Map.tryFind rem remainders with
        | Some(start) -> pos - start
        | None ->
            let nextRem = (rem * 10) % d
            if nextRem = 0 then 0
            else findCycle (pos + 1) (Map.add rem pos remainders) nextRem
    findCycle 0 Map.empty 1

[<EntryPoint>]
let main _ =
    let candidates = [1..999]
    let cycleLengthsMap = candidates |> List.map (fun d -> (d, cycleLength d))
    let result= cycleLengthsMap |> List.maxBy snd |> fst
    printfn "%d" result
    0