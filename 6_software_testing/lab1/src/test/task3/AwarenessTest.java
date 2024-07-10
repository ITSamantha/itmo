package test.task3;

import main.task3.Awareness;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class AwarenessTest {

    @ParameterizedTest
    @DisplayName("checkAwareness")
    @ValueSource(strings = {"я хочу кушать", "я кит", "или я не кит..."})
    public void checkAwareness(String awareness) {
        Awareness a = new Awareness(awareness);
        Assertions.assertEquals(a.getAwareness(), awareness);
    }

}
