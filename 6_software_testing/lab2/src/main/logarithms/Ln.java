package main.logarithms;


import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

public class Ln {
    private static final Double EPSILON = 1e-21;


    public static Double calculate(Double value) {

        if (value < (double) 0 || Double.isNaN(value)) {
            return Double.NaN;
        } else if (value == Double.POSITIVE_INFINITY) {
            return Double.POSITIVE_INFINITY;
        } else if (value == (double) 0) {
            return Double.NEGATIVE_INFINITY;
        }


        int exponent = 0;
        while (value > 1) {
            value /= Math.E;
            exponent++;
        }

        Double current_value = value - 1;
        Double temp = current_value;
        Double result = temp;
        Double current_pow = current_value;

        int n = 2;
        double sign = -1;


        while (Math.abs(temp) > EPSILON) {
            current_pow *= current_value;
            temp = current_pow / n;
            result += sign * temp;
            sign = -sign;
            n += 1;
        }

        return result + exponent;
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
        Ln.writeToCSV(
                Ln.formatToCSV(-3.0, 0.5, 200.0),
                new FileWriter("src/resources/logarithms/ln.csv")
        );
    }

    public static String getName() {
        return "Ln";
    }

}
