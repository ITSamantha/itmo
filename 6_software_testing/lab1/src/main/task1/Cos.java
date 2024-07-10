package main.task1;


public class Cos {

    private static final Double EPSILON = 1e-12;


    public static Double calculate(Double value) {

        /*
        Finds the cos of double number.
        @return The value of cos for value.
         */

        if (value == null ||
                value == Double.POSITIVE_INFINITY ||
                value == Double.NEGATIVE_INFINITY) {
            return Double.NaN;
        }

        double temp = 1.0;
        double result = 1.0;

        int sign = -1;
        int n = 2;

        while (Math.abs(temp) > EPSILON) {
            double numerator = Math.pow(value, n);
            double denominator = Factorial.calculate(n);
            temp = numerator / denominator;
            result += sign * temp;
            sign = -sign;
            n += 2;
        }


        return result;
    }
}


