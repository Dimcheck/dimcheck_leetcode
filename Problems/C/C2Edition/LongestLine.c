#include <stdio.h>
#define MAXLINE 1000  /* maximum input line size */

int getLine(char line[], int maxlinelength);
void copy(char to[], char from[]);

int main () {
    int len;
    int max = 0;
    char line[MAXLINE];    // current line
    char longest[MAXLINE]; // longest line
    
    while ((len = getLine(line, MAXLINE)) > 0) {
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    }
    if (max > 0) {
        printf("\nLONGEST LINE IS: %s", longest);
        printf("\nLONGEST LINE COUNT: %d", max - 1);
    }
    return 0;
}

int getLine(char line[], int maxlinelength) {
    int c, i;
    for (i = 0; i < maxlinelength-1 && (c=getchar()) != EOF && c != '\n'; ++i) {
        line[i] = c;
    }
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;   
}

void copy(char to[], char from[]) {
    /* ASSIGMENT EXPRESSION WITH CHECK 
    1. from[i] is read & that value is assigned to to[i]
    2. Assignment expression returns the assigned value
    3. That value is compared with '\n'
    */
    int i = 0;
    while ((to[i] = from[i]) != '\n') {
        ++i;
    }
}
