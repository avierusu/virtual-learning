/**
 * An object that implements the comparator interface
 * can take in two objects and compare them using the
 * compare method.
 */

// Import Comparator
import java.util.Comparator;

class HDTV {
    private int size;
    private String brand;

    // Constructor
    public HDTV(int TVSize, String TVBrand){
        size = TVSize;
        brand = TVBrand;
    }

    public int getSize(){
        return size;
    }

    public String getBrand(){
        return brand;
    }
}

// Create a separate comparator class to compare HDTV objects
class SizeComparator implements Comparator<HDTV> {
    public int compare(HDTV tv1, HDTV tv2){
        return tv1.getSize() - tv2.getSize();
    }
}

public class comparatorTest {
    public static void main(String args[]){
        // Create two HDTV objects to compare
        HDTV tv1 = new HDTV(10, "Samsung");
        HDTV tv2 = new HDTV(15, "Sony");
        SizeComparator comparer = new SizeComparator();

        // Compare the TV sizes
        System.out.printf("The difference in size of the TVs is " + comparer.compare(tv1, tv2));
    }
}