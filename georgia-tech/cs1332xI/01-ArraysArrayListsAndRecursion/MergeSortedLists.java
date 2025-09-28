// Use merge sort to merge two sorted array lists
// into one sorted array list

import java.util.ArrayList;

public class MergeSortedLists {
    public static ArrayList<Integer> mergeSortedLists(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        // Create a new empty array list to store the merged lists
        ArrayList<Integer> mergedList = new ArrayList<>();
        // Define indices for list1 and list2
        int list1Index = 0, list2Index = 0;

        // Add each integer from each list to the merged list
        while (list1Index < list1.size() && list2Index < list2.size()) {
            // Add the next smallest integer into the merged array list
            if (list1.get(list1Index) <= list2.get(list2Index)) {
                mergedList.add(list1.get(list1Index));
                list1Index++;
            } else {
                mergedList.add(list2.get(list2Index));
                list2Index++;
            }
        }

        // Append remaining elements of list1 when done with list2
        while (list1Index < list1.size()) {
            mergedList.add(list1.get(list1Index));
            list1Index++;
        }

        // Append remaining elements of list2 when done with list1
        while (list2Index < list2.size()) {
            mergedList.add(list2.get(list2Index));
            list2Index++;
        }

        return mergedList;
    }

    public static void main(String[] args) {
        // Create two sorted array lists to test functionality
        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(1); list1.add(3); list1.add(5);

        ArrayList<Integer> list2 = new ArrayList<>();
        list2.add(2); list2.add(4); list2.add(6);

        // Create a merged array list and merge the two array lists
        ArrayList<Integer> mergedList = mergeSortedLists(list1, list2);
        // Display results
        // Output: [1, 2, 3, 4, 5, 6]
        System.out.println("Merged List: " + mergedList);
    }
}