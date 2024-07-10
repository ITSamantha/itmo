package main;

import main.logarithms.Log;
import main.trigonometry.Cos;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

public class SystemFunction {
    public static Double calculate(Double value) {


        if (value == Double.NaN || value == Double.NEGATIVE_INFINITY || value == Double.POSITIVE_INFINITY) {
            return Double.NaN;
        }

        Double result = Double.NaN;

        if (value <= 0) {
            Double cos = Cos.calculate(value);
            result = cos * cos;
        } else if (value > 0) {
            Double log10_value = Log.calculate(value, 10.0);
            Double log3_value = Log.calculate(value, 3.0);
            Double log2_value = Log.calculate(value, 2.0);
            Double temp = Math.pow(Math.pow((log10_value - log10_value), 2.0) - (log2_value + log3_value), 3.0);
            result = temp + log3_value;
            return result;
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
        SystemFunction.writeToCSV(
                SystemFunction.formatToCSV(-50.0, 0.5, 50.0),
                new FileWriter("src/resources/system/system_function.csv")
        );
    }

    public static String getName() {
        return "System Function";
    }
}
