class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];

        // Loop through numbers in nums array
        for (int i = 0; i < nums.length; i++) {
            // Loop through other numbers (no repeats) and check for sum to target
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target ) {
                    indices[0] = i;
                    indices[1] = j;
                    return indices;
                }
            }
        }
        return indices;
    }
}
