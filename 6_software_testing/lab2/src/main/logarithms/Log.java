package main.logarithms;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

public class Log {

    private static final Double EPSILON = 1e-21;

    public static Double calculate(Double value, Double rate) {

        if (rate == (double) 1) {
            return Double.NaN;
        }

        Double lnRate = Ln.calculate(rate);

        Double lnValue = Ln.calculate(value);

        Double result = lnValue / lnRate;

        if (result == Double.NEGATIVE_INFINITY || result == Double.POSITIVE_INFINITY) {
            return Double.NaN;
        }

        return result;

    }

    public static String formatToCSV(Double value, Double rate, Double step, Double limit) {
        StringBuilder result = new StringBuilder();
        while (value <= limit) {
            result.append(value).append(';').append(calculate(value, rate)).append("\n");
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
        Log.writeToCSV(
                Log.formatToCSV(0.5, 2.0, 0.5, 50.5),
                new FileWriter("src/resources/logarithms/log2.csv")
        );
        Log.writeToCSV(
                Log.formatToCSV(0.0, 10.0, 1.0, 100.0),
                new FileWriter("src/resources/logarithms/log10.csv")
        );
        Log.writeToCSV(
                Log.formatToCSV(-3.0, 3.0, 0.5, 50.5),
                new FileWriter("src/resources/logarithms/log3.csv")
        );
    }

    public static String getName() {
        return "Log";
    }
}




