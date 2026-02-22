class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        HashMap<Character, Integer> hm = new HashMap<>();

        int l = 0; // left pointer

        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);

            // If character already exists and is inside window
            if (hm.containsKey(ch) && hm.get(ch) >= l) {
                l = hm.get(ch) + 1;
            }

            // Update latest index of character
            hm.put(ch, r);

            // Update max length
            maxLen = Math.max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
