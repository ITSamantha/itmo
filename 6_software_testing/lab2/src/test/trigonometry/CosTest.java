package test.trigonometry;

import main.trigonometry.Cos;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.ValueSource;


public class CosTest {

    private static final double epsilon = 1e-12;

    @ParameterizedTest(name = "defaultTest")
    @DisplayName("Test with default values")
    @ValueSource(doubles = {-2 * Math.PI, -1.5 * Math.PI, -Math.PI, -0.5 * Math.PI, 0, 0.5 * Math.PI, Math.PI, 1.5 * Math.PI, 2 * Math.PI})
    public void calculateDefaultTest(double value) {
        Assertions.assertTrue(Math.abs(Math.cos(value) - Cos.calculate(value)) <= epsilon);
    }

    @ParameterizedTest(name = "criticalTest")
    @DisplayName("Test with critical values")
    @ValueSource(doubles = {Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, Double.NaN})
    public void calculateCriticalTest(double value) {
        Assertions.assertTrue(Double.isNaN(Cos.calculate(value)));
    }

    @ParameterizedTest(name = "csvTest")
    @DisplayName("Test with the data from CSV")
    @CsvFileSource(resources = "/test/trigonometry/resources/cos.csv", delimiter = ';')
    public void calculateCsvTest(double x, double y) {
        Assertions.assertTrue(y - Cos.calculate(x) <= epsilon);
    }
}