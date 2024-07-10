package test.task2;

import main.task2.MyLinkedList;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class LinkedListTest {

    @Test
    @DisplayName("defaultTest")
    public void defaultTest() throws Exception {
        int expected_size = 1000;
        MyLinkedList<String> list = new MyLinkedList<>();
        for (int i = 0; i < expected_size; i++) {
            list.insert("str" + i);
        }
        Assertions.assertEquals(list.getSize(), expected_size);
    }

    @Test
    @DisplayName("deleteTest")
    public void deleteTest() throws Exception {
        int expected_size = 1000;
        int expected_clear_size = 500;
        MyLinkedList<String> list = new MyLinkedList<>();
        for (int i = 0; i < expected_size; i++) {
            list.insert("str" + i);
        }
        Assertions.assertEquals(list.getSize(), expected_size);

        for (int i = 0; i < expected_size / 2; i++) {
            list.delete("str" + i);
        }
        Assertions.assertEquals(list.getSize(), expected_clear_size);
    }

}
