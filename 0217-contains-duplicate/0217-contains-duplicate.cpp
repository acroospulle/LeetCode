class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        // sorting
        sort(nums.begin(), nums.end());
        // for loop for i, i<nums.size()-1
        for(int i = 0; i<nums.size()-1;i++) {
            // if statement, nums[i + 1]
            if(nums[i]== nums[i + 1]) {
                // return true
                return true;
            }
            
        }
            //return false for else statement
            return false;
        
    }
};