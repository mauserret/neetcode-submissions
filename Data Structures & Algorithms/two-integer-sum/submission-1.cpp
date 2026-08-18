class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complement;
        for (int i = 0; i < nums.size()-1; i++) {
            int remain = target - nums[i];
            if (complement.contains(remain)) {
                return {complement[remain], i};
            }
            complement[nums[i]] = i;
        }
    }
};
