namespace Task7.Tests

open NUnit.Framework
open task7inf
open task7module
open task7rec
open task7tailrec
open task7map

[<TestFixture>]
type Task7Tests() =

    [<Test>]
    member this.TestFindNthPrimeInTask7Inf() =
        let result = task7inf.findNthPrime 6
        Assert.That(result, Is.EqualTo(13), "The 6th prime should be 13")

    [<Test>]
    member this.TestFindNthPrimeInTask7Module() =
        let result = task7module.findNthPrime 6
        Assert.That(result, Is.EqualTo(13), "The 6th prime should be 13")

    [<Test>]
    member this.TestFindNthPrimeInTask7Rec() =
        let result = task7rec.findNthPrime 6 1 0
        Assert.That(result, Is.EqualTo(13), "The 6th prime should be 13")

    [<Test>]
    member this.TestFindNthPrimeInTask7TailRec() =
        let result = task7tailrec.findNthPrime 6
        Assert.That(result, Is.EqualTo(13), "The 6th prime should be 13")

    [<Test>]
    member this.TestFindNthPrimeInTask7Map() =
        let result = task7map.findNthPrime 6
        Assert.That(result, Is.EqualTo(13), "The 6th prime should be 13")

    [<Test>]
    member this.TestIsPrimeNumberForPrimeNumber() =
        let result = task7module.isPrimeNumber 29
        Assert.That(result, Is.True, "29 should be prime")

    [<Test>]
    member this.TestIsPrimeNumberForNonPrimeNumber() =
        let result = task7module.isPrimeNumber 100
        Assert.That(result, Is.False, "100 should not be prime")