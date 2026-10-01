#include <stdio.h>
#define MAXLINE 1000  /* maximum input line size */
#define PRINTCAP 10  /* minimum line size to trigger print (1-17 excercise) */
#define ARRAYLENGTH 40

int getLine(char line[]);
void copy(char to[], char from[]);
void printCap(int len, char line[]); /* 1-17 */
void trimCharArray(char line[]); /* 1-18 */
void reverseCharArray(char line[]); /* 1-19 */

int main () {
    int len;
    int max = 0;
    char line[MAXLINE];    // current line
    char longest[MAXLINE]; // longest line
    
    while ((len = getLine(line)) > 0) {
        // printCap(len, line);
        // trimCharArray(line, len);
        reverseCharArray(line);
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


void reverseCharArray(char line[]) {
    char swap, start, end;
    start = end = 0;

    while (line[end] != '\0') {end++;}
    end--;
    if (line[end] == '\n') {end--;} // if end points to \n, then copy() won't happen
    
    while (start <= end) {
        swap = line[start];
        line[start] = line[end];
        line[end] = swap;
        start++;
        end--;
    } 
}

void trimCharArray(char line[]) {
    for (int i = 0; i < ARRAYLENGTH; ++i) {
        if (line[i] == ' ') {
            for (int j = i; j < ARRAYLENGTH; ++j){
                line[j] = line[j+1];
            }
            --i;
        }
        else if (line[i] == '\0') {
            break;
        }
    }
}

void printCap(int line_len, char line[]) {
   if (line_len > PRINTCAP) {
        printf("\nmessage is big enough: %s", line);
    }
}

int getLine(char line[]) {
    int c, i;
    for (i = 0; i < MAXLINE-1 && (c=getchar()) != EOF && c != '\n'; ++i) {
        line[i] = c;
    }
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    printf("%i", i);
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
