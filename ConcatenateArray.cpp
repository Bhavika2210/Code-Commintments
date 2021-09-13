class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        int n=nums.size(),i=0;
        
        vector<int>nums2(2*n);
       for(i=0;i<n;i++)
        {
            nums2[i]=nums[i];
        }
        
    for(int j=0;j<n;j++)
    {
        nums2[n+j]=nums[j];
    }
        
        
    return nums2;
    }
};
