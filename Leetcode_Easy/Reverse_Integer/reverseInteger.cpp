#include <iostream>
#include <string>

using namespace std;

/*
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
    then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Leetcode Problem Reference: https://leetcode.com/problems/reverse-integer/
*/

class Solution {
public:
    /* 
        Brute Force - String Reverse Method
        Convert int to str, reverse, and then convert str to int. Must check for negative and overflow cases.
        
        Runtime: 0 ms, faster than 100.00% of C++ online submissions for Reverse Integer.
        Memory Usage: 6.5 MB, less than 6.40% of C++ online submissions for Reverse Integer.
    */
    int reverse(int x) {
        string newX = to_string(x);
        string reversedX = "";
        if (x < 0) {
            reversedX += "-";
        }
        for (int i = newX.length()-1; i >= 0; i--) {
            reversedX += newX[i];
        }
        try{
            return stoi(reversedX);
        }
        catch(const std::out_of_range& e) { 
            return 0;
        }
    }
};

int main() {
    Solution results;

    // Example 1
    int input = 123;
    int output = 321;
    int retval = results.reverse(input);
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
    input = -123;
    output = -321;
    retval = results.reverse(input);
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
    input = 120;
    output = 21;
    retval = results.reverse(input);
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
    input = 0;
    output = 0;
    retval = results.reverse(input);
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
    output = 0;
    retval = results.reverse(input);
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