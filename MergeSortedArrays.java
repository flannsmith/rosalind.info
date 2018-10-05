import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class MergeSortedArrays {

    public static void main(String[] args) throws FileNotFoundException {

        System.out.println("This is Merged Sort program.");

        // 1st, read in the array from insertion.txt document;
        Scanner readScan = new Scanner(new File("sampletext.txt"));

        int Len = readScan.nextInt(); // the first integer means the number of elements in the first array;
        int[] array1 = new int[Len];

        // read in the array one by one;
        for (int i = 0; i < Len; i++) {
            array1[i] = readScan.nextInt();

        }
        System.out.println(java.util.Arrays.toString(array1));

        int Len2 = readScan.nextInt(); // size of the number of elements in the second array;

        int[] array2 = new int[Len2];

        for (int i = 0; i < Len2; i++) {
            array2[i] = readScan.nextInt();
        }
        System.out.println(java.util.Arrays.toString(array2));

        readScan.close();

        int n1 = array1.length;
        int n2 = array2.length;
        int[] arr3 = new int[n1 + n2];

        mergeArrays(array1, array2, n1, n2, arr3);
    }

    // Merge arr1[0..n1-1] and arr2[0..n2-1]
    // into arr3[0..n1+n2-1]
    public static void mergeArrays(int[] arr1, int[] arr2, int n1, int n2, int[] arr3) {
        int i = 0, j = 0, k = 0;

        // Traverse both array
        while (i < n1 && j < n2) {
            // Check if current element of first
            // array is smaller than current element
            // of second array. If yes, store first
            // array element and increment first array
            // index. Otherwise do same with second array
            if (arr1[i] < arr2[j])
                arr3[k++] = arr1[i++];
            else
                arr3[k++] = arr2[j++];
        }

        // Store remaining elements of first array
        while (i < n1)
            arr3[k++] = arr1[i++];

        // Store remaining elements of second array
        while (j < n2)
            arr3[k++] = arr2[j++];

        // System.out.println(java.util.Arrays.toString(arr3));
        File file = new File("rosalind_mers_solution.txt");

        try {
            PrintWriter printWriter = new PrintWriter(file);
            printWriter.println(java.util.Arrays.toString(arr3));
            printWriter.close();
        } catch (FileNotFoundException ex) {
            // insert code to run when exception occursc
            System.out.println("shit");
        }

    }
}