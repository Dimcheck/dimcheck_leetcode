#include <stdio.h>




char findTheDifference(char *s[], char *t[]);

int main () {
    char s[5] = 'abcd';
    char t[6] = 'abcde';

    findTheDifference(&s, &t);
    return 0;
    
}


char findTheDifference(char *s[], char *t[]) {
    int str1 = 0;
    int str2 = 0;
    int result;

    for (int i=0; s[i]!= '\0'; ++i) {
        str1 = str1 + (int)s[i];
        printf("%i", (int)s[i]);
    }
    for (int i=0; t[i]!= '\0'; ++i) {
        str2 = str2 + (int)t[i];
    }
    
    result = str2 - str1;
    return (char)result;
}