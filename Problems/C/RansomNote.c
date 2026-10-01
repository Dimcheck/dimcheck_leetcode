#include <stdbool.h> 
#include <stdio.h>

 /*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105;
ransomNote and magazine consist of lowercase English letters.
*/


bool canConstruct(char *ransomNote, char *magazine);

int main() {
    char ransomNote[] = "aa";
    char magazine[] = "baa";
    bool result = canConstruct(ransomNote, magazine);
    printf("%d", result);
    return 0;
}


bool canConstruct(char *ransomNote, char *magazine) {
    int alphabet[26];
    int letterId;

    // Fill the array with 0
    for (int i=0; i < 26; i++) {
        alphabet[i] = 0;
    }
    for (int i=0; magazine[i]!='\0'; ++i) {
        letterId = magazine[i] - 'a';
        alphabet[letterId]++;
    }
    for (int i=0; ransomNote[i]!='\0'; ++i) {
        letterId = ransomNote[i] - 'a';
        alphabet[letterId]--;
        if (alphabet[letterId] < 0) {
            return false;
        }
    }
    return true;

    
        
}

