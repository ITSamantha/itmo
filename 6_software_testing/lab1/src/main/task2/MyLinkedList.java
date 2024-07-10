package main.task2;

public class MyLinkedList<T> {
    private Node<T> head;

    private int size;

    public MyLinkedList() {
        this.head = null;
        this.size = 0;
    }

    public void insert(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        Node<T> node = new Node<T>(value);
        if (this.head == null) {
            this.head = node;
        } else {
            Node<T> current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = node;
        }
        this.size++;
    }

    public void addFirst(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        Node<T> node = new Node<T>(value);

        if (this.head != null) {
            node.next = this.head;
        }

        this.head = node;
        this.size++;
    }

    public boolean delete(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        if (this.head == null) {
            return false;
        }

        if (this.head.value.equals(value)) {
            this.head = this.head.next;
            this.size--;
            return true;
        }

        Node<T> current = head;

        while (current.next != null) {
            if (current.next.value.equals(value)) {
                current.next = current.next.next;
                this.size--;
                return true;
            }
            current = current.next;
        }

        return false;
    }

    public boolean contains(T value) throws Exception {
        if (value == null) {
            throw new Exception("Value can not be null.");
        }
        Node<T> current = head;
        while (current != null) {
            if (current.value.equals(value)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public void clear() {
        this.size = 0;
        this.head = null;
    }

    public int getSize() {
        return this.size;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder("MyLinkedList(");
        s.append("size=").append(this.size).append(") ");
        if (head != null) {
            s.append(head);
        } else {
            s.append("null");
        }
        return s.toString();
    }
}
