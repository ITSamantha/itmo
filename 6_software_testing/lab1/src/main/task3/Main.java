package main.task3;


import main.task3.enums.PositionType;
import main.task3.enums.StateType;
import main.task3.enums.TimeType;

public class Main {
    public static void main(String[] args) throws Exception {
        Whale whale = new Whale(PositionType.NOT_NATURAL, StateType.UNHAPPY, "Макар");
        String awareness1 = whale.getUsedTo(new Awareness("оно кит"));
        String awareness2 = whale.getUsedTo(new Awareness("оно не кит"));
        String catch1 = whale.catchInTime(TimeType.LITTLE, awareness1);
        String catch2 = whale.catchInTime(TimeType.LITTLE, awareness2);
        System.out.println(catch1);
        System.out.println(catch2);
    }
}