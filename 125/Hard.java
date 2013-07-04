

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;

public class Hard{
 
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] rc = sc.nextLine().split(" ");
        int width = Integer.parseInt(rc[0]);
        int height = Integer.parseInt(rc[1]);
        int[][] layout = new int[height][width];
        Set<Integer> added = new TreeSet<Integer>();
        for(int i = 0 ; i < height ; i++) {
            rc = sc.nextLine().split(" ");
            for(int j = 0; j < width; j++){
                layout[i][j] = Integer.parseInt(rc[j]);
                if(layout[i][j] == 0)
                    added.add(j + (width * i));
            }
        }
       printLayout(layout);
        
        List<TreeSet<Integer>> polygonRooms = new ArrayList<TreeSet<Integer>>();
        for(int i = 0; i < height ; i++) {
            for(int j = 0; j < width; j++) {
                if(added.contains(flatten(i,j,width)))
                    continue;
                TreeSet<Integer> tree = new TreeSet<Integer>();
                HashSet<Integer> visited = new HashSet<Integer>();
                Stack<Integer> open = new Stack<Integer>();
                
                int roomType = layout[i][j];
                tree.add(flatten(i,j,width));
                open.add(flatten(i,j,width));
                
                while(!open.isEmpty()) {
                    Integer curr = open.pop();
                    if(visited.contains(curr))
                        continue;
                    visited.add(curr);
                    int ii = getI(curr, width);
                    int jj = getJ(curr, width);
                    if(roomType != layout[ii][jj])
                        continue;
                    tree.add(curr);
                    added.add(curr);
                    if( inBounds(layout, ii-1, jj) )
                        open.add(flatten(ii-1, jj, width));
                    if( inBounds(layout, ii+1, jj) )
                        open.add(flatten(ii+1, jj, width));
                    if( inBounds(layout, ii, jj - 1))
                        open.add(flatten(ii, jj - 1, width));
                    if( inBounds(layout, ii, jj + 1))
                        open.add(flatten(ii, jj + 1, width));
                }
                polygonRooms.add(tree);
            }
        }
        dumpPoly(polygonRooms, layout, width);
        // to-do: implement an axis-parallel polygon splitting [into similarly aligned rectangles] algorithm
    }
    
    public static boolean inBounds(int[][] matrix, int i, int j){
        return i >= 0 && j >= 0 && i < matrix.length && j < matrix[0].length;
    }
    
    public static int flatten(int i, int j, int width){
        return j + (width * i );
    }
    public static int getI(int num, int width){
        return num / width;
    }
    public static int getJ(int num, int width){
        return num % width;
    }
    
    public static void dumpPoly(List<TreeSet<Integer>> polygonRooms, int[][] layout, int width){
        for(TreeSet<Integer> tree : polygonRooms){
            int roomType = -1;
            for(Integer curr : tree) {
                int ii = getI(curr, width);
                int jj = getJ(curr, width);
                if(roomType == -1)
                    roomType = layout[ii][jj];
                System.out.println("" + ii +", " + jj);
            }
            System.out.println("roomtype: " + roomType);
        }
    }
    public static void printLayout(int[][] layout){
        for(int i = 0 ; i < layout.length; i++){
            for(int j = 0 ; j < layout[0].length; j++)
                System.out.print(layout[i][j] + " ");
            System.out.println();
        }
    }
    
}