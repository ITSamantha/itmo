package main.trigonometry;


import main.logarithms.Ln;
import main.utils.Factorial;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

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

    public static String formatToCSV(Double value, Double step, Double limit) {
        StringBuilder result = new StringBuilder();
        while (value <= limit) {
            result.append(value).append(';').append(calculate(value)).append("\n");
            value += step;
        }
        return result.toString();
    }

    public static void writeToCSV(String toOut, Writer out) {
        try (PrintWriter printer = new PrintWriter(out)) {
            printer.print(toOut);
        }
    }

    public static void execute() throws IOException {
        Cos.writeToCSV(
                Cos.formatToCSV(-4 * Math.PI, Math.PI / 2, 4 * Math.PI),
                new FileWriter("src/resources/trigonometry/cos.csv")
        );
    }

    public static String getName() {
        return "Cos";
    }
}


