#include <iostream>
#include <vector>

using namespace std;

/*
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Leetcode Problem Reference: https://leetcode.com/problems/two-sum/
*/

class Solution {
public:
    /* 
        Brute Force Method
        Iterate through the array and compare each element to a paired element. Check if sum of paired elements equal to target. 
        Return if satisfied, otherwise return empty vector.

        Considering that this approach incorporates two for-loops, time complexity is O(n^2). Space complexity of O(1).

        Runtime: 796 ms, faster than 5.04% of C++ online submissions for Two Sum.
        Memory Usage: 10.1 MB, less than 42.72% of C++ online submissions for Two Sum.
    */
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> sum {};
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    sum.push_back(i);
                    sum.push_back(j);
                }
            }
        }
        return sum;
    }
};

/*
    Reference: https://www.techiedelight.com/print-vector-cpp/
*/
void print(std::vector<int> const &input) {
    for (int i = 0; i < input.size(); i++) {
        std::cout << input.at(i) << ' ';
    }
}

int main() {
    Solution results;

    // Example 1
    vector <int> nums {2,7,11,15};
    int target = 9;
    vector <int> output {0,1};
    vector <int> retval = results.twoSum(nums, target);
    if(retval == output)
        cout << "Example 1: Pass" << endl;
    else 
        cout << "Example 1: Failed" << endl;

    // Example 2
    nums = {3,2,4};
    target = 6;
    output = {1,2};
    retval = results.twoSum(nums, target);
    if(retval == output)
        cout << "Example 2: Pass" << endl;
    else 
        cout << "Example 2: Failed" << endl;

    // Example 3
    nums = {3,3};
    target = 6;
    output = {0,1};
    retval = results.twoSum(nums, target);
    if(retval == output)
        cout << "Example 3: Pass" << endl;
    else 
        cout << "Example 3: Failed" << endl;

    return 0;
}