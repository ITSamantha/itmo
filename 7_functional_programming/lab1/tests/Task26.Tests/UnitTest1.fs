namespace Task26.Tests

open NUnit.Framework
open task26rec

[<TestFixture>]
type Task26RecTests() =

    [<Test>]
    member this.TestCycleLengthForD7() =
        let result = task26rec.cycleLength 7
        Assert.That(result, Is.EqualTo(6), "The cycle length for d = 7 should be 6")

    [<Test>]
    member this.TestCycleLengthForD3() =
        let result = task26rec.cycleLength 3
        Assert.That(result, Is.EqualTo(1), "The cycle length for d = 3 should be 1")

    [<Test>]
    member this.TestCycleLengthForD1() =
        let result = task26rec.cycleLength 1
        Assert.That(result, Is.EqualTo(0), "The cycle length for d = 1 should be 0")

    [<Test>]
    member this.TestFindMaxCycleRec() =
        let result = task26rec.findMaxCycleRec 1 1000 1 0
        Assert.That(result, Is.EqualTo(983), "The number with the longest cycle length in the range should be 983")

    [<Test>]
    member this.TestFindMaxCycleRecWithSmallerRange() =
        let result = task26rec.findMaxCycleRec 1 10 1 0
        Assert.That(result, Is.EqualTo(7), "The number with the longest cycle length in the range should be 7")

    [<Test>]
    member this.TestFindMaxCycleRecWithLargeRange() =
        let result = task26rec.findMaxCycleRec 1 2000 1 0
        Assert.That(result, Is.EqualTo(1979), "The number with the longest cycle length in the range should be 1979")