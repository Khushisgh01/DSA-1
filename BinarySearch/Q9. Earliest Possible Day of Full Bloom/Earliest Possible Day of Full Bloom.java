import java.util.*;

class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        
        int[][] seeds = new int[n][2];
        for (int i = 0; i < n; i++) {
            seeds[i][0] = plantTime[i];
            seeds[i][1] = growTime[i];
        }
        
        // Sort by growTime descending
        Arrays.sort(seeds, (a, b) -> b[1] - a[1]);
        
        int currentPlantDays = 0;
        int maxBloomDay = 0;
        
        for (int[] seed : seeds) {
            currentPlantDays += seed[0];
            maxBloomDay = Math.max(maxBloomDay, currentPlantDays + seed[1]);
        }
        
        return maxBloomDay;
    }
}
