package test.logarithms;

import main.logarithms.Ln;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.ValueSource;

public class LnTest {

    private static final double epsilon = 1e-21;

    @ParameterizedTest(name = "csvTest")
    @DisplayName("Test with the data from CSV")
    @CsvFileSource(resources = "/test/logarithms/resources/ln.csv", delimiter = ';')
    public void calculateCsvTest(double x, double y) {
        Double result = y - Ln.calculate(x);
        Assertions.assertTrue(Double.isNaN(result) || result <= epsilon);
    }

    @ParameterizedTest(name = "criticalTest")
    @DisplayName("Test with critical values")
    @ValueSource(doubles = {Double.NEGATIVE_INFINITY, Double.NaN})
    public void calculateCriticalTest(double value) {
        Assertions.assertTrue(Double.isNaN(Ln.calculate(value)));
    }


    @ParameterizedTest(name = "criticalTest2")
    @DisplayName("Test with critical values2")
    @ValueSource(doubles = {Double.POSITIVE_INFINITY})
    public void calculateCriticalTest2(double value) {
        Assertions.assertTrue(Double.isInfinite(Ln.calculate(value)));
    }
}
