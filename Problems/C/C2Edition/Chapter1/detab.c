/* Write a program detab that replaces tabs in the input 
 * with the proper number of blanks to space to the next tab stop. 
 * Assume a fixed set of tab stops, say every n columns.
 * Should n be a variable or a symbolic parameter? */

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
    char word[ARRAYLENGTH] = "A\tBC123";               // 3 space total
    // char word[ARRAYLENGTH] = "ABC\t123";               // 1 space total
    char spaces;

    // printf("BEFORE: %s", word);
    
    for (int i=0; word[i]!='\0'; ++i) {
        if (word[i] == '\t') {
            spaces = TABSTOP - (i % TABSTOP);
            if (spaces == 0) {spaces = TABSTOP;}
            while (spaces != 0) {
                word[i] = ' ';
                --spaces;
                ++i;
            }
        }
    }
    // printf("\nAFTER: %s", word);
    printf("\nSPACES AFTER: %i", countSpaces(word));
}



