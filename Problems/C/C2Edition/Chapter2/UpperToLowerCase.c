#include <stdio.h>


char asciiToLowerCase(char c);



int main () {
    char c = 'U';
    int look;
    printf("MAIN FORMULA IS: %i - %i\n", (int)'a', (int)'A');
    printf("\nint view: %i\tchar view: %c", (int)c, c);
    printf("\nint view: %i\tchar view: %c", (int)asciiToLowerCase(c), asciiToLowerCase(c));
    
}

char asciiToLowerCase(char c) {
    if (c >= 'A' && c<= 'Z') {
        return c + 'a' - 'A';
    }
    else {
        return c;
    }
    
}