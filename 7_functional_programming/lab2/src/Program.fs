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