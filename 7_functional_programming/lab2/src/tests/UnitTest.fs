module Lab2.Tests

open NUnit.Framework
open OpenAddressHashMap

[<Test>]
let AddAndRetrieveValueShouldReturnCorrectResults() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable

    Assert.AreEqual(Some "one", collectValue 1 hashTable)
    Assert.AreEqual(Some "two", collectValue 2 hashTable)
    Assert.AreEqual(None, collectValue 3 hashTable)

[<Test>]
let RemoveShouldEraseEntryAndReturnNone() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable
    let hashTable = delete 1 hashTable

    Assert.AreEqual(None, collectValue 1 hashTable)
    Assert.AreEqual(Some "two", collectValue 2 hashTable)

[<Test>]
let MergeShouldCombineTwoHashTables() =
    let firstTable = createEmptyHashMap 5
    let firstTable = insert 1 "one" firstTable
    let firstTable = insert 2 "two" firstTable

    let secondTable = createEmptyHashMap 5
    let secondTable = insert 2 "two" secondTable
    let secondTable = insert 3 "three" secondTable

    let combinedTable = combine firstTable secondTable

    Assert.AreEqual(Some "one", collectValue 1 combinedTable)
    Assert.AreEqual(Some "two", collectValue 2 combinedTable)
    Assert.AreEqual(Some "three", collectValue 3 combinedTable)

[<Test>]
let MergeWithEmptyTableShouldReturnOriginal() =
    let mainTable = createEmptyHashMap 5
    let mainTable = insert 1 "one" mainTable
    let mainTable = insert 2 "two" mainTable

    let emptyTable = createEmptyHashMap 0

    let resultTable = combine mainTable emptyTable

    Assert.AreEqual(collectValue 1 mainTable, collectValue 1 resultTable)
    Assert.AreEqual(collectValue 2 mainTable, collectValue 2 resultTable)
    Assert.AreEqual(mainTable.Size, resultTable.Size)

[<Test>]
let FilterShouldIncludeMatchingEntriesOnly() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable
    let hashTable = insert 3 "three" hashTable

    let filteredTable = filterMap (fun (key, _) -> key % 2 = 0) hashTable

    Assert.AreEqual(None, collectValue 1 filteredTable)
    Assert.AreEqual(Some "two", collectValue 2 filteredTable)
    Assert.AreEqual(None, collectValue 3 filteredTable)

[<Test>]
let MapShouldTransformAllEntries() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable
    let hashTable = insert 3 "three" hashTable

    let transformedTable = map (fun (key, (value: string)) -> (key, value.ToUpper())) hashTable

    Assert.AreEqual(Some "ONE", collectValue 1 transformedTable)
    Assert.AreEqual(Some "TWO", collectValue 2 transformedTable)
    Assert.AreEqual(Some "THREE", collectValue 3 transformedTable)

[<Test>]
let FoldLeftShouldAccumulateStateCorrectly() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable
    let hashTable = insert 3 "three" hashTable

    let keySum = foldLeft (fun accumulator (key, _) -> accumulator + key) 0 hashTable
    Assert.AreEqual(6, keySum)

[<Test>]
let FoldRightShouldAccumulateStateCorrectly() =
    let hashTable = createEmptyHashMap 5
    let hashTable = insert 1 "one" hashTable
    let hashTable = insert 2 "two" hashTable
    let hashTable = insert 3 "three" hashTable

    let concatenatedValues = foldRight (fun (_, value) accumulator -> accumulator + " " + value) "" hashTable
    Assert.AreEqual("three two one", concatenatedValues.Trim())
