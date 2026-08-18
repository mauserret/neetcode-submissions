class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;
        for (int num : numSet) {
            if (!numSet.contains(num-1)) {
                int current = num;
                int streak = 1;

                while (numSet.contains(current+1)) {
                    streak++;
                    current++;
                }
            longest = max(streak, longest);
            }
        }
        return longest;
    }
};
