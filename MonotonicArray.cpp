class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int dec=0,inc=0;
        for(int i=0;i<nums.size()-1;i++)
        {
            if(nums[i]>=nums[i+1])
                dec++;
        }
        for(int i=0;i<nums.size()-1;i++)
        {
            if(nums[i]<=nums[i+1])
                inc++;
        }
        if(inc==nums.size()-1 || dec==nums.size()-1)
            return true;
        else 
            return false;
