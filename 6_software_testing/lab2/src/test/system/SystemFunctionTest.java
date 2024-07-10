package test.system;

import main.SystemFunction;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.ValueSource;

public class SystemFunctionTest {
    private static final double epsilon = 1e-12;

    @ParameterizedTest(name = "csvTest")
    @DisplayName("Test with the data from CSV")
    @CsvFileSource(resources = "/test/system/resources/system_function.csv", delimiter = ';')
    public void calculateCsvTest(double x, double y) {
        Double result = y - SystemFunction.calculate(x);
        Assertions.assertTrue(Double.isNaN(result) || result <= epsilon);
    }

    @ParameterizedTest(name = "criticalTest")
    @DisplayName("Test with critical values")
    @ValueSource(doubles = {Double.NEGATIVE_INFINITY, Double.NaN, Double.POSITIVE_INFINITY})
    public void calculateCriticalTest(double value) {
        Assertions.assertTrue(Double.isNaN(SystemFunction.calculate(value)));
    }

    @ParameterizedTest(name = "defaultTest")
    @DisplayName("Test with default values")
    @ValueSource(doubles = {0, -1, -2, -4, 1})
    public void calculateDefaultTest(double value) {
        Double cos = Math.cos(value);
        Double cos_result = cos * cos;
        Double result = SystemFunction.calculate(value);
        Assertions.assertTrue(Math.abs(cos_result - result) <= epsilon);
    }

}
