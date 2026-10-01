#include <stdio.h>


void squezee(char s[], int c);


int main() {
    char s[] = "ABBAA";
    int c = 'A';

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

void squezee(char s[], int c) {
    int j, i;

    for (i=j=0; s[i]!='\0'; ++i) {
        if (s[i] != c) {
            s[j++] = s[i];
        }
    }
    s[j] = '\0';
}