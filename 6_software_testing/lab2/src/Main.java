

import main.SystemFunction;
import main.logarithms.Ln;
import main.logarithms.Log;
import main.trigonometry.Cos;
import main.utils.Factorial;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        System.out.println(Ln.getName());
        Ln.execute();

        System.out.println(Log.getName());
        Log.execute();

        System.out.println(Factorial.getName());
        Factorial.execute();

        System.out.println(Cos.getName());
        Cos.execute();

        System.out.println(SystemFunction.getName());
        SystemFunction.execute();
    }
}