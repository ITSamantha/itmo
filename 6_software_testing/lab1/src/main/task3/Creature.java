package main.task3;

import main.task3.enums.CreatureType;
import main.task3.enums.PositionType;
import main.task3.enums.StateType;
import main.task3.interfaces.ICatchable;


public class Creature implements ICatchable {

    private PositionType position;

    private StateType state;

    private String name;


    private CreatureType type;

    public Creature(PositionType position, StateType state, String name, CreatureType type) {
        this.position = position;
        this.state = state;
        this.name = name;
        this.type = type;
    }

    public StateType getState() {
        return state;
    }

    public void setState(StateType state) {
        this.state = state;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PositionType getPosition() {
        return position;
    }

    public void setPosition(PositionType position) {
        this.position = position;
    }

    public void setType(CreatureType type) {
        this.type = type;
    }

    public CreatureType getType() {
        return type;
    }

    public String getUsedTo(Awareness awareness) {
        return String.format("свыкнуться с осознанием того, что %s", awareness.getAwareness());
    }

}
