/* Write a program entab that replaces strings of blanks 
 * by the minimum number of tabs and blanks to achieve the same spacing. 
 * Use the same tab stops as for detab.
 * When either a tab or a single blank would suffice to reach a tab stop, which should be given preference? */


#include <stdio.h>
#define TABSTOP 4  
#define ARRAYLENGTH 20


int countSpaces(char word[]) {
    int spacesCount = 0;
    for (int i=0; word[i]!='\0'; ++i) {
        if (word[i] == ' ') {
            ++spacesCount;
        }
    }
    return spacesCount;
}


int main() {
    char spacesString[ARRAYLENGTH] = "    ";   // 4 spaces
    // char spaces_string[ARRAYLENGTH] = "      "; // 6 spaces

    char totalSpaces = countSpaces(spacesString);
    char spaceLeftovers;
    char tabs;
    char idx = 0;
    char mixedString[ARRAYLENGTH];

    tabs = totalSpaces / TABSTOP;
    spaceLeftovers = totalSpaces % TABSTOP;

    while (tabs != 0 || spaceLeftovers != 0) {
        if (tabs > 0) {
            mixedString[idx] = '\t';
            --tabs;
        } else if (spaceLeftovers > 0) {
            mixedString[idx] = ' ';
            --spaceLeftovers;
        }
        ++idx;
    }
    mixedString[idx] = '\0';
    printf("%s", mixedString);
    return 0;
}



