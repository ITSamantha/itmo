package main.task2;


import static java.lang.Math.abs;

public class ClosedAddressingHashTable<T> {

    private long size;
    private final int capacity;
    private MyLinkedList<T>[] table;

    public ClosedAddressingHashTable(int capacity) {
        this.size = 0;
        this.capacity = capacity + 3;

        this.table = new MyLinkedList[this.capacity];
        for (int i = 0; i < this.capacity; i++) {
            table[i] = new MyLinkedList<T>();
        }
    }

    public void insert(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        int index = hash(value);
        this.table[index].addFirst(value);
        this.size++;
    }

    public void delete(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        int index = hash(value);
        boolean isDeleted = this.table[index].delete(value);
        if (isDeleted) {
            this.size--;
        }
    }

    public boolean contains(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        int index = hash(value);
        return this.table[index].contains(value);
    }

    public MyLinkedList<T> get(int key) throws Exception {
        if (!this.isEmpty()) {
            throw new Exception("Table is empty.");
        }
        if (key > this.capacity || key < 0) {
            return table[key];
        } else {
            throw new Exception("Incorrect key.");
        }
    }

    private int hash(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        int hash_code = abs(value.hashCode());
        return hash_code % this.capacity;
    }

    public void clear() {
        this.size = 0;
        this.table = new MyLinkedList[this.capacity];
        for (int i = 0; i < this.capacity; i++) {
            table[i] = new MyLinkedList<T>();
        }
    }

    public long getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("ClosedAddressingHashTable| ");
        s.append("size=").append(this.size).append(",");
        s.append("capacity(number of buckets)=").append(this.capacity).append("\n");
        for (int i = 0; i < this.capacity; i++) {
            if (table[i] != null) {
                s.append(i).append(". ").append(table[i]).append("\n");
            } else {
                s.append(i).append(". null").append("\n");
            }
        }
        return s.toString();
    }


}
