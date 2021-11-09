class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        // SOLVING USING UNORDERED MAP
        unordered_map<int,int>MAP;
        for(int i=0;i<nums.size();i++)
        {
            if(MAP.find(target-nums[i])!=MAP.end())
            {
                answer.push_back(i);
                answer.push_back(MAP[target-nums[i]]);
                return answer;
            }
            MAP[nums[i]]=i; // nums[i] is the key and i is its value  
        }
        return answer;
        
    }
};
/* example:
[2,7,11,15] target is 9
first we will have 2:0 in the MAP
then as we go to i=1,i.e 7
in the if condition
MAP.find(9-7)!=MAP.end() which is true
we get 1 and 0 pushed in answer vector.*/
