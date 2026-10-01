#include <stdio.h>

/* 
 * Write an alternative version of squeeze(s1,s2) that deletes each character in s1 that matches any character in the string s2
 */

void squezee(char s[], char c[]);


int main() {
    char s[] = "ABBAGAMA";
    char c[] = "AG";

    printf("\nBEFORE: ");
    for (int i=0; s[i] != '\0'; ++i) {
        printf("%c", s[i]);
    }

    squezee(s, c);

    printf("\nAFTER: ");
    for (int i=0; s[i] != '\0'; ++i) {
        printf("%c", s[i]);
    }
    return 0;
}


void squezee(char s[], char c[]) {
    int j, i;
    int lIdx = 0;
    
    while (c[lIdx] != '\0') {
        for (i=j=0; s[i]!='\0'; ++i) {
            if (s[i] != c[lIdx]) {
                s[j++] = s[i];
            }
        }
        s[j] = '\0';
        ++lIdx;
    }

}