// Create a class to define a class roster of Students
// using an Array List. We can traverse, add and remove
// Students
import java.util.ArrayList;

public class ClassRoster {
    public static void main(String[] args) {
        // Create an empty array list of students
        ArrayList<Student> students = new ArrayList<>();

        // Add students
        students.add(new Student(101, "Alice"));
        students.add(new Student(102, "Bob"));
        students.add(new Student(103, "Charlie"));

        System.out.println("Initial Roster:");
        printList(students);

        // Insert a new student at index 1
        students.add(1, new Student(104, "Diana"));
        System.out.println("\nAfter inserting Diana at index 1:");
        printList(students);

        // Remove a student by index
        students.remove(2); // Removes Bob
        System.out.println("\nAfter removing student at index 2:");
        printList(students);
    }

    public static void printList(ArrayList<Student> list) {
        for (Student student : list) {
            System.out.println(student);
        }
    }
}