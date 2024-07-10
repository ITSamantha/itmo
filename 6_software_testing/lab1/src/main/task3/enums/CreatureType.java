package main.task3.enums;

public enum CreatureType {

    WHALE("кит"),
    NOT_WHALE("не кит");

    private final String message;

    public String getMessage() {
        return message;
    }

    CreatureType(String message) {
        this.message = message;
    }
}
