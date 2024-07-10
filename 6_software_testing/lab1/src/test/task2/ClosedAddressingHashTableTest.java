package test.task2;

import main.task2.ClosedAddressingHashTable;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.NullSource;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class ClosedAddressingHashTableTest {

    @Test
    @DisplayName("defaultTest")
    public void defaultTest() throws Exception {
        int expected_size = 6;
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        String[] test_strs = new String[]{"n", "dcjdf", "djfjkd", "ndndngggggggggg", "a", "nn", "b", "n"};
        for (int i = 0; i < test_strs.length; i++) {
            hash_table.insert(test_strs[i]);
        }
        hash_table.delete("nn");
        hash_table.delete("a");
        hash_table.delete("bbb");
        Assertions.assertEquals(expected_size, hash_table.getSize());
    }

    @Test
    @DisplayName("deleteTest")
    public void deleteTest() throws Exception {
        int expected_size = 3;
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        String[] test_strs = new String[]{"n", "ddm", "dh"};
        for (int i = 0; i < test_strs.length; i++) {
            hash_table.insert(test_strs[i]);
        }
        hash_table.delete("nn");
        hash_table.delete("a");
        hash_table.delete("bbb");
        Assertions.assertEquals(expected_size, hash_table.getSize());
    }

    @Test
    @DisplayName("clearTest")
    public void clearTest() throws Exception {
        int expected_insert_size = 1000;
        int expected_clear_size = 0;
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        for (int i = 0; i < expected_insert_size; i++) {
            hash_table.insert(String.valueOf(i));
        }
        Assertions.assertEquals(expected_insert_size, hash_table.getSize());
        hash_table.clear();
        Assertions.assertEquals(expected_clear_size, hash_table.getSize());
    }

    @Test
    @DisplayName("emptyTest")
    public void emptyTest() throws Exception {
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        Assertions.assertTrue(hash_table.isEmpty());
        for (int i = 0; i < 100; i++) {
            hash_table.insert(String.valueOf(i));
        }
        Assertions.assertFalse(hash_table.isEmpty());
    }

    @ParameterizedTest
    @NullSource
    public void nullTest(String s) throws Exception {
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        Assertions.assertThrows(Exception.class, () -> hash_table.insert(s));
        Assertions.assertThrows(Exception.class, () -> hash_table.delete(s));
        Assertions.assertThrows(Exception.class, () -> hash_table.contains(s));
    }

    @Test
    @DisplayName("containsTest")
    public void containsTest() throws Exception {
        ClosedAddressingHashTable<String> hash_table = new ClosedAddressingHashTable<>(10);
        for (int i = 0; i < 100; i++) {
            hash_table.insert("Name" + i);
            Assertions.assertTrue(hash_table.contains("Name" + i));
        }
        hash_table.delete("Name" + 2);
        Assertions.assertFalse(hash_table.contains("Name" + 2));
    }
}
