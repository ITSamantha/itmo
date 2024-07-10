package main.task3.interfaces;

import main.task3.enums.TimeType;

import java.util.Random;

public interface ICatchable {

    default String catchInTime(TimeType time, String action) {
        Random random = new Random();
        String isSuccess = random.nextBoolean() ? "И успел" : "И не успел";
        return String.format("%s времени на то, чтобы успеть %s. %s.", time.getMessage(), action, isSuccess);
    }
}
