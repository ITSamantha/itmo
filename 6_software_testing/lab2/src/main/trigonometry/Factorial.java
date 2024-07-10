package main.task1;

import java.math.BigDecimal;
import java.math.BigInteger;

public class Factorial {

    public static double calculate(int value) {
        /*
        Finds the factorial of integer number.
        @return The value of factorial for x. If value is incorrect (value <= 0) then returns 1.
         */

        double result = 1;

        while (value > 0) {
            result *= value;
            value--;
        }

        return result;
    }
}
