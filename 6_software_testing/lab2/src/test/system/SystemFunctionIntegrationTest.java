package test.system;

import main.logarithms.Log;
import main.trigonometry.Cos;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.anyDouble;
import static org.mockito.Mockito.atLeastOnce;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class SystemFunctionIntegrationTest {

    static final double EPSILON = 1e-4;

    @Mock
    Cos cosMock;

    @Mock
    Log lgMock;

    @Spy
    Cos cosSpy;

    @Spy
    Log lgSpy;


    @Test
    void testMathSystemCalculationTrigonometricFunctionsCalled() {
        verify(cosSpy, atLeastOnce()).calculate(anyDouble());
        verify(lgSpy, atLeastOnce()).calculate(anyDouble(), 2.0);
        verify(lgSpy, atLeastOnce()).calculate(anyDouble(), 3.0);
        verify(lgSpy, atLeastOnce()).calculate(anyDouble(), 10.0);

    }

}
