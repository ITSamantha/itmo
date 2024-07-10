package main.task3.enums;

public enum StateType {

    UNHAPPY("несчастный"),
    HAPPY("счастливый");


    private final String message;

    public String getMessage() {
        return message;
    }

    StateType(String message) {
        this.message = message;
    }
}
