class Solution {

    private int sign = 1;

    public int myAtoi(String s) {
        if (s == null || s.length() == 0) return 0;

        int i = 0;
        int n = s.length();

        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        if (i == n) return 0;

        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        return helper(s, i, 0L);
    }

    private int helper(String s, int index, long result) {
        if (index >= s.length() || !Character.isDigit(s.charAt(index))) {
            return (int)(sign * result);
        }

        result = result * 10 + (s.charAt(index) - '0');

        if (sign == 1 && result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        }

        if (sign == -1 && -result < Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }

        return helper(s, index + 1, result);
    }
}

