
public class quickSort {
	int[] Array;
	
	public quickSort(int[] Array) {
		this.Array = Array;
		
	}
	
	public int partition(int low, int high) {
		int pivot = Array[high];
		int leftWall = low - 1;
		
		for (int i = low; i < high; i++) {
			if (Array[i] <= pivot) {
				leftWall++;
				
				int temp = Array[i];
				Array[i] = Array[leftWall];
				Array[leftWall] = temp;
				
			}
		}
		
		int temp = Array[leftWall+1];
		Array[leftWall+1] = Array[high];
		Array[high] = temp;
		
		return leftWall;
		
	}
	
	public void intSort(int low, int high) {
		if (low < high) {
			int pivotLocation = partition(low, high);
			intSort(low, pivotLocation);
			intSort(pivotLocation + 1, high);
			
		}
	}
	
	public int size() {
		return Array.length;
		
	}
	
	public int[] getArray() {
		return Array;
		
	}
	
    public String toString() { 
        int n = Array.length; 
        String rep = "Sorted Array: ";
        for (int i=0; i<n; ++i) {
            rep += Integer.toString(Array[i]);
            
            if (i < n-1) {
            	rep += ", ";
            	
            }
        }
        
        return rep;
        
    } 
  
    public static void main(String args[]) {
    	int[] arr = {363, 844, 819, 819, 257, 591, 893, 387, 289, 421, 419, 67, 409, 448, 450, 781, 723, 536, 295, 634, 166, 795, 758, 763, 234, 922, 579, 461, 198, 793, 481, 889, 610, 894, 77, 612, 88, 715, 970, 541, 492, 33, 191, 661, 550, 222, 3, 27, 442, 22, 684, 555, 261, 149, 507, 673, 821, 793, 985, 169, 320, 484, 454, 534, 327, 886, 249, 482, 383, 420, 960, 151, 726, 516, 593, 560, 968, 629, 136, 856, 231, 94, 975, 915, 16, 58, 423, 720, 516, 889, 41, 421, 278, 925, 728, 41, 652, 779, 667, 338};
        quickSort test  = new quickSort(arr); 
        
        test.intSort(0, test.size()-1);
  
        System.out.println(test.toString());

        
    } 
}
