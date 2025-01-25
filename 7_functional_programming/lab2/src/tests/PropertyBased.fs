module OpenAddressHashMapPropertyTests

open NUnit.Framework
open FsCheck
open OpenAddressHashMap
open System.IO

// Helper function to compare two calculateHash maps for equality
let areDictsEqual (map1: OpenAddressHashMap<int, int>) (map2: OpenAddressHashMap<int, int>) =
    if map1.Size <> map2.Size then
        false
    else
        let compareFilledSlots =
            Array.forall
                (fun entry ->
                    match entry with
                    | Some (key, value) ->
                        match collectValue key map2 with
                        | Some value2 when value = value2 -> true
                        | _ -> false
                    | None -> true)
                map1.Storage

        compareFilledSlots

// Generator for creating random calculateHash maps
let generateMap =
    Gen.sized (fun size ->
        gen {
            let! keyValuePairs = Gen.listOfLength size (Arb.generate<int * int>)
            let map = createEmptyHashMap (size * 2)

            let filledMap =
                List.fold (fun (accumulator: OpenAddressHashMap<int, int>) (key, value) -> insert key value accumulator) map keyValuePairs

            return filledMap
        })

let testMap = Arb.fromGen generateMap

// Property test: Merging with an empty map returns the original map
[<Test>]
let ``Monoid Property - Merge with Empty Map Returns Original Map``() =
    let property (map: OpenAddressHashMap<int, int>) =
        let emptyMap = createEmptyHashMap 0
        let mergedMap = combine map emptyMap
        areDictsEqual map mergedMap

    Prop.forAll testMap property
    |> Check.QuickThrowOnFailure

// Property test: Insert should correctly insert values to the map
[<Test>]
let ``Insert Property - Inserting Values Returns Correct Value``() =
    let property (values: int list) =
        let map = createEmptyHashMap (List.length values * 2)
        let mutable currentMap = map

        List.forall
            (fun value ->
                currentMap <- insert value value currentMap
                collectValue value currentMap = Some value)
            values

    Check.QuickThrowOnFailure property

// Property test: Insert should work with key-value pairs of different types
[<Test>]
let ``Insert Property - Inserting Key-Value Pairs with Strings``() =
    let property (pairs: (int * string) list) =
        let map = createEmptyHashMap (List.length pairs * 2)
        let mutable currentMap = map

        List.forall
            (fun (key, value) ->
                currentMap <- insert key value currentMap
                collectValue key currentMap = Some value)
            pairs

    Check.QuickThrowOnFailure property

// Property test: Merge should be associative
[<Test>]
let ``Associative Property - Merge Should Be Associative``() =
    let property
        (
            map1: OpenAddressHashMap<int, int>,
            map2: OpenAddressHashMap<int, int>,
            map3: OpenAddressHashMap<int, int>
        ) =
        let mergedLeft = combine (combine map1 map2) map3
        let mergedRight = combine map1 (combine map2 map3)
        areDictsEqual mergedLeft mergedRight

    let testTripleMap = Arb.fromGen (Gen.zip3 generateMap generateMap generateMap)

    Prop.forAll testTripleMap property
    |> Check.QuickThrowOnFailure

// SetUp method to prepare the environment before running tests
[<OneTimeSetUp>]
let initialize() =
    let stringWriter = new StringWriter()
    System.Console.SetOut(stringWriter)