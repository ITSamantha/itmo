package main.task3.enums;

public enum PositionType {
    NOT_NATURAL("не самое естественное"),
    NATURAL("естественное дело");


    private final String message;

    public String getMessage() {
        return message;
    }

    PositionType(String message) {
        this.message = message;
    }
}
