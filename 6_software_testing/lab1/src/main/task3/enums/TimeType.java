package main.task3.enums;

public enum TimeType {

    LITTLE("мало"),
    MANY("много");

    private final String message;

    public String getMessage() {
        return message;
    }

    TimeType(String message) {
        this.message = message;
    }
}
