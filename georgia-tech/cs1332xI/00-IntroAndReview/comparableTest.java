/**
 * An object that implements the comparable interface
 * can directly compare itself to another object
 * using the compare to method.
 */

class HDTV implements Comparable<HDTV> {
    private int size;
    private String brand;

    // Constructor
    public HDTV(int tvSize, String tvBrand){
        size = tvSize;
        brand = tvBrand;
    }

    public int getSize(){
        return size;
    }

    public String getBrand(){
        return brand;
    }

    // Overwrite and customize compareTo function
    public int compareTo(HDTV tv){
        // For this example, lets use size to compare HDTVs
        return size - tv.size;
    }
}

public class comparableTest {
    public static void main(String args[]){
        // Create two HDTV objects to compare
        HDTV tv1 = new HDTV(10, "Samsung");
        HDTV tv2 = new HDTV(15, "Sony");

        // Compare the TV sizes
        System.out.printf("The difference in size of the TVs is " + tv1.compareTo(tv2));
    }
}