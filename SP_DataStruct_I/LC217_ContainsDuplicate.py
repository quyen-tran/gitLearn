from collections import Counter

class Solution:
    def containsDuplicate(self, nums):
        """Given an integer array nums, return True if any value appears at 
        least twice in the array, and return False if every element is distinct.
        
        Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9

        Args:
            nums ([int]): Input list of numbers

        Returns:
            is_Duped [bool]: Status whether the list of numbers contain dupes
        """
        
        """ 
        # First implementation using a list with O(n) time complexity for lookup
        # Implementation failed to pass when encountered with very large arrays
        # Resulted in Time Out Error
        """
        """
        unique_nums = []
        for n in nums:
            if n not in unique_nums:
                unique_nums.append(n)
            else:
                return True
        return False
        """
        
        """
        # Second implemenation utilizing set data structure which can store 
        # unordered collection of elements with no duplicates
        #
        # Runtime: 499 ms, faster than 58.53 percent of submissions
        # Memory Usage: 26 MB, less than 54.62 percent of submissions
        """
        """
        unique_nums = set(nums)
        if len(nums) == len(unique_nums):
            return False
        else:
            return True
        """
        
        """
        # Third implementation utilizing Counter from the collection library
        # Counter is essentially a dict subclass that counts hashable objects
        #
        # Runtime: 468 ms, faster than 68.00 percent of submissions
        # Memory Usage: 26 MB, less than 29.44 percent of submissions
        """
        counted_nums = Counter(nums)
        most_common = counted_nums.most_common(1)
        if most_common[0][1] > 1:
            return True
        else:
            return False
        
def main():
    # Test Case #1
    nums = [1, 2, 3, 1]
    expected_result = True
    cdupe = Solution()
    print("Nums List: ", nums)
    if cdupe.containsDuplicate(nums) is expected_result:
        print("Output Status: ", cdupe.containsDuplicate(nums))
    else:
        print("Incorrect answer. Expecting: ", expected_result)
    
    # Test Case #2
    nums = [1,2,3,4]
    expected_result = False
    cdupe = Solution()
    print("Nums List: ", nums)
    if cdupe.containsDuplicate(nums) is expected_result:
        print("Output Status: ", cdupe.containsDuplicate(nums))
    else:
        print("Incorrect answer. Expecting: ", expected_result)
    
    # Test Case #3
    nums = [1,1,1,3,3,4,3,2,4,2]
    expected_result = True
    cdupe = Solution()
    print("Nums List: ", nums)
    if cdupe.containsDuplicate(nums) is expected_result:
        print("Output Status: ", cdupe.containsDuplicate(nums))
    else:
        print("Incorrect answer. Expecting: ", expected_result)
    
    print("End of Program")

if __name__ == "__main__":
    main()