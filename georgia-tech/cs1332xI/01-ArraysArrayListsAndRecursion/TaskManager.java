// Create a class to represent a task manager.
// This manager will allow you to add and remove
// tasks dynamically

import java.util.ArrayList;

public class TaskManager {
    public static void main(String[] args) {
        ArrayList<Task> taskList = new ArrayList<>();

        // Add tasks in order
        taskList.add(new Task("Reply to emails", 3));
        taskList.add(new Task("Prepare meeting slides", 2));
        taskList.add(new Task("Daily standup", 1));

        System.out.println("Initial Task List:");
        printTasks(taskList);

        // Insert urgent task at index 0
        taskList.add(0, new Task("Fix production bug", 0));
        System.out.println("\nAfter inserting urgent task at index 0:");
        printTasks(taskList);

        // Remove completed task at index 1
        taskList.remove(1); // Removes "Daily standup"
        System.out.println("\nAfter removing task at index 1:");
        printTasks(taskList);
    }

    public static void printTasks(ArrayList<Task> tasks) {
        for (Task task : tasks) {
            System.out.println(task);
        }
    }
}