class Solution:
    def maxSubArray(self, nums):
        """Given an integer array nums, find the contiguous subarray 
        (containing at least one number) which has the largest sum and return 
        its sum. A subarray is a contiguous part of an array.
        
        Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4

        Args:
            nums ([int]): Input list of numbers

        Returns:
            sum [int]: sum of contiguous subarray
        """
        
        """
        # First brute-force implementation. Reached time limit. Must re-eval
        # approach
        """
        """
        best_sum = sum(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                temp_sum = sum(nums[i:j])
                if temp_sum > best_sum:
                    best_sum = temp_sum
        return max(best_sum, max(nums))
        """

        """
        # Third attempt. Trying to achieve O(n). This method checks the sum as
        # array is incremented, but discard the previous subset sum if that is
        # less than current value. Results successful.
        #
        # Runtime: 1149 ms, faster than 31.83 percent of submissions
        # Memory Usage: 28 MB, less than 81.54 percent of submissions
        #
        """
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_value = nums[i]
            current_sum = max(current_value, current_sum + current_value)
            max_sum = max(current_sum, max_sum)
        return max_sum
    
    """
    # Second approach using recursion. Still reached time limit.
    """
    """
    def maxSubArray(self, nums):
        subset = self.get_subset(nums)
        best_sum = sum(nums)
        for s in subset:
            temp_sum = sum(s)
            if temp_sum > best_sum:
                best_sum = temp_sum
        return max(best_sum, max(nums))
    
    def get_subset(self, nums):
        if not nums:
            return []
        return [nums[i:] for i in range(len(nums))] + self.get_subset(nums[:-1])
    """ 
                
def main():
    # Test Case #1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected_result = 6
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)
    # Test Case #2
    nums = [1]
    expected_result = 1
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)
    # Test Case #3 
    nums = [5,4,-1,7,8]
    expected_result = 23
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)
    # Test Case #4
    nums = [-2,1]
    expected_result = 1
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)      
    # Test Case #5
    nums = [-2,-3,-1]
    expected_result = -1
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)    
    # Test Case #6
    nums = [8,-19,5,-4,20]
    expected_result = 21
    mSub = Solution()
    result = mSub.maxSubArray(nums)
    if result is expected_result:
        print("Success! Output Status: ", result)
    else:
        print("Incorrect answer. ", "Received: ", result, 
              " | Expecting: ", expected_result)   
                
    print("\n*** End of Program ***")

if __name__ == "__main__":
    main()