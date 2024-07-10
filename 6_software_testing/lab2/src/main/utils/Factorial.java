package main.utils;


import main.trigonometry.Cos;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Writer;

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

    public static String formatToCSV(int value, int step, int limit) {
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
        Factorial.writeToCSV(
                Factorial.formatToCSV(-5, 1, 20),
                new FileWriter("src/resources/utils/factorial.csv")
        );
    }

    public static String getName() {
        return "Factorial";
    }
}
