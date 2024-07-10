package test.logarithms;

import main.logarithms.Log;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.ValueSource;

public class Log10Test {
    private static final double epsilon = 1e-21;

    @ParameterizedTest(name = "csvTest")
    @DisplayName("Test with the data from CSV")
    @CsvFileSource(resources = "/test/logarithms/resources/log10.csv", delimiter = ';')
    public void calculateCsvTest(double x, double y) {
        Double result = y - Log.calculate(x, 10.0);
        Assertions.assertTrue(Double.isNaN(result) || result <= epsilon);
    }

    @ParameterizedTest(name = "criticalTest")
    @DisplayName("Test with critical values")
    @ValueSource(doubles = {Double.NEGATIVE_INFINITY, Double.NaN, Double.POSITIVE_INFINITY})
    public void calculateCriticalTest(double value) {
        Assertions.assertTrue(Double.isNaN(Log.calculate(value, 10.0)));
    }

}
