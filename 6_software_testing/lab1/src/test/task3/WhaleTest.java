package test.task3;

import main.task3.Awareness;
import main.task3.Whale;
import main.task3.enums.CreatureType;
import main.task3.enums.PositionType;
import main.task3.enums.StateType;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;
import org.junit.jupiter.params.provider.ValueSource;

import java.util.Objects;

public class WhaleTest {

    @ParameterizedTest
    @DisplayName("nameTest")
    @ValueSource(strings = {"Макар", "Олег", "Никита", "Артём"})
    public void nameTest(String name) {
        Whale whale = new Whale(PositionType.NOT_NATURAL, StateType.UNHAPPY, name);
        Assertions.assertTrue(Objects.equals(whale.getName(), name));
    }

    @ParameterizedTest
    @DisplayName("positionTest")
    @EnumSource(PositionType.class)
    public void positionTest(PositionType position) {
        Whale whale = new Whale(position, StateType.UNHAPPY, "Макар");
        Assertions.assertEquals(whale.getPosition(), position);
    }

    @Test
    @DisplayName("checkWhale")
    public void checkWhale() {
        Whale whale = new Whale(PositionType.NOT_NATURAL, StateType.UNHAPPY, "Макар");
        Assertions.assertEquals(whale.getType(), CreatureType.WHALE);
        Assertions.assertNotSame(whale.getType(), CreatureType.NOT_WHALE);
        whale.setType(CreatureType.NOT_WHALE);
        Assertions.assertEquals(whale.getType(), CreatureType.NOT_WHALE);
        whale.setPosition(PositionType.NATURAL);
        Assertions.assertEquals(whale.getPosition(), PositionType.NATURAL);
    }


    @ParameterizedTest
    @DisplayName("checkGetUsed}")
    @ValueSource(strings = {"я хочу кушать", "я кит", "или я не кит..."})
    public void checkGetUsed(String awareness) {
        Awareness a = new Awareness(awareness);
        Whale whale = new Whale(PositionType.NOT_NATURAL, StateType.UNHAPPY, "Макар");
        String result = whale.getUsedTo(a);
        String expected_result = String.format("свыкнуться с осознанием того, что %s", a.getAwareness());
        Assertions.assertEquals(expected_result, result);
    }
}
