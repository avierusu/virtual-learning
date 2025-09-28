// Create a class to represent a task or chore

public class Task {
    String description;
    // Lower number = higher priority
    int priority;

    public Task(String description, int priority) {
        this.description = description;
        this.priority = priority;
    }

    public String toString() {
        return "[Priority " + priority + "] " + description;
    }
}