#include <iostream>

using namespace std;

/*
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

    Leetcode Problem Reference: https://leetcode.com/problems/palindrome-number/
*/

class Solution {
public:
    /* 
        Brute Force 
        Convert int to string, reverse string, then compare to original string.

        Runtime: 36 ms, faster than 6.30% of C++ online submissions for Palindrome Number.
        Memory Usage: 5.8 MB, less than 68.95% of C++ online submissions for Palindrome Number.
    */
    bool isPalindrome(int x) {
        string newX = to_string(x);
        string reversedX = "";
        for (int i = newX.length()-1; i >= 0; i--) {
            reversedX += newX[i];
        }
        return reversedX == newX;
    }
};

int main() {
    Solution results;
    // Example 1
    int input = 121;
    bool output = true;
    int retval = results.isPalindrome(input);
    if(retval == output) {
        cout << "Example 1: Pass" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }
    else {
        cout << "Example 1: Failed" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }

    // Example 2
    input = -121;
    output = false;
    retval = results.isPalindrome(input);
    if(retval == output) {
        cout << "Example 2: Pass" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }
    else {
        cout << "Example 2: Failed" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }

    // Example 3
    input = 10;
    output = false;
    retval = results.isPalindrome(input);
    if(retval == output) {
        cout << "Example 3: Pass" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }
    else {
        cout << "Example 3: Failed" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }

    // Example 4
    input = -101;
    output = false;
    retval = results.isPalindrome(input);
    if(retval == output) {
        cout << "Example 4: Pass" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }
    else {
        cout << "Example 4: Failed" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }

    // Example 5
    input = 1534236469;
    output = false;
    retval = results.isPalindrome(input);
    if(retval == output) {
        cout << "Example 5: Pass" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }
    else {
        cout << "Example 5: Failed" << endl;
        cout << "Expected output : " + to_string(output) << endl;
        cout << "Received output : " + to_string(retval) << endl;
    }

    return 0;
}