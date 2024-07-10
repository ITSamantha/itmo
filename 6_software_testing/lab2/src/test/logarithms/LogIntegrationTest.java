package test.logarithms;

import main.logarithms.Ln;
import main.logarithms.Log;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.anyDouble;
import static org.mockito.Mockito.atLeastOnce;
import static org.mockito.Mockito.when;

import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.junit.jupiter.MockitoExtension;


@ExtendWith(MockitoExtension.class)
public class LogIntegrationTest {

    static final double EPSILON = 1e-10;
    @Mock
    Ln lnMock;
    @Spy
    Ln lnSpy;

    @Test
    void testLog2CalculationLnFunctionCalled() {
        Log.calculate(8.0, 2.0);
        verify(lnSpy, atLeastOnce()).calculate(anyDouble());
    }

    @Test
    void testLog2CalculationWithMockedLnValues() {
        when(lnMock.calculate(2.0)).thenReturn(0.69314);
        when(lnMock.calculate(8.0)).thenReturn(2.07944);
        assertEquals(3.0, Log.calculate(8.0, 2.0), EPSILON);
    }
}