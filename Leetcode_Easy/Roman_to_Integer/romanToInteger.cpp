#include <iostream>
#include <string>

using namespace std;

/*
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as 
    XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written 
    as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six 
    instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

    Leetcode Problem Reference: https://leetcode.com/problems/roman-to-integer/ 
*/

class Solution {
public:
    /* 
        Brute Force 
    */
    int romanToInt(string s) {
        int output = 0;
        for (int i = s.length(); i >= 0; i--) {
            if (s[i] == 'I') {
                output += 1;
            }
            else if (s[i] == 'V') {
                output += 5;
                if (s[i-1] == 'I') {
                    output -= 1;
                    i--;
                }
            }
            else if (s[i] == 'X') {
                output += 10;
                if (s[i-1] == 'I') {
                    output -= 1;
                    i--;
                }
            }
            else if (s[i] == 'L') {
                output += 50;
                if (s[i-1] == 'X') {
                    output -= 10;
                    i--;
                }
            }
            else if (s[i] == 'C') {
                output += 100;
                if (s[i-1] == 'X') {
                    output -= 10;
                    i--;
                }
            }
            else if (s[i] == 'D') {
                output += 500;
                if (s[i-1] == 'C') {
                    output -= 100;
                    i--;
                }
            }
            else if (s[i] == 'M') {
                output += 1000;
                if (s[i-1] == 'C') {
                    output -= 100;
                    i--;
                }
            }
            else {
                cout << "Invalid input." << endl;
                output = 0;
            }
        }
        return output;
    }
};

int main() {
    Solution results;

    // Example 1
    string input = "III";
    int output = 3;
    int retval = results.romanToInt(input);
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
    input = "IV";
    output = 4;
    retval = results.romanToInt(input);
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
    input = "IX";
    output = 9;
    retval = results.romanToInt(input);
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
    input = "LVIII";
    output = 58;
    retval = results.romanToInt(input);
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
    input = "MXCIV";
    output = 1094;
    retval = results.romanToInt(input);
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