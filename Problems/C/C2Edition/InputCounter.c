#include <stdio.h>




int main () {
    int user_input;
    double char_counter = 0;
    double blank_counter = 0;
    double tab_counter = 0;
    double newline_counter = 0;
    
    while ((user_input = getchar()) != EOF) {
        if (user_input == '\n') {
            ++newline_counter;        
        }
        else if (user_input == '\t') {
            ++tab_counter;        
        }
        else if (user_input == ' ') {
            ++blank_counter;        
        }
        else {
            ++char_counter;        
        }
        putchar(user_input);
    }
    printf("Chars | Blanks | Tabs | Newlines\n");
    printf("%3.0f %7.0f %7.0f %8.0f \n", char_counter, blank_counter, tab_counter, newline_counter);
}



