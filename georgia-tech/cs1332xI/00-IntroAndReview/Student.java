// Create a class to represent a student

public class Student {
    String name;
    int id;

    // Constructor
    public Student(int idNumber, String fullName) {
        id = idNumber;
        name = fullName;
    }

    public String toString() {
        return id + " - " + name;
    }
}