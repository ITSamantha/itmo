package test.utils;

import main.utils.Factorial;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

public class FactorialTest {
    private static final double epsilon = 1e-12;

    @ParameterizedTest(name = "csvTest")
    @DisplayName("Test with the data from CSV")
    @CsvFileSource(resources = "/test/utils/resources/factorial.csv", delimiter = ';')
    public void calculateCsvTest(int x, double y) {
        Assertions.assertTrue(y - Factorial.calculate(x) <= epsilon);
    }
}
