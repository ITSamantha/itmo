package main.task3;

import main.task3.enums.CreatureType;
import main.task3.enums.PositionType;
import main.task3.enums.StateType;

public class Whale extends Creature {

    public Whale(PositionType position, StateType state, String name) {
        super(position, state, name, CreatureType.WHALE);
    }
}
