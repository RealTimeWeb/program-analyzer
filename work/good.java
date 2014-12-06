class LinkedList {
    private Node head;
    
    public LinkedList() {
        head = null;
    }
    
    public void add(int data) {
        if (head == null) {
            head = new Node(data);
        } else {
            head.add(data);
        }
    }
}

class Node {
    private int data;
    private Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
    
    public void add(int data) {
        if (next == null) {
            this.next = new Node(data);
        } else {
            this.next.add(data);
        }
    }
}