#include <stdio.h>
#include <ctype.h>

///////////////
/* EOF is -1 */
/* :getchar: takes a single input character: WORLD -> W */
/* Use Ctrl+D  to send EOF from keyboard*/
//////////////

// int main() {
//     int c;
//     c = getchar();
//     while (c != EOF) {
//         putchar(c);
//         c = getchar();
//     }
// }

/* Exit possible only with EOF */
// int main() {
//     int c;
//     c = getchar();
//     if (c != EOF) {
//         printf("You are wrong\n");
//     }
//     else {
//         printf("Dang, how did you manage?\n");
//     }
// }

/* print one word per input line */
// int main() {
//     int c;
//     c = getchar();
//     while (c != ' ' && c != '\t' && c != '\n') {
//         putchar(c);
//         c = getchar();
//     }
//     printf("\n");
// }


/* print a horizontal histogram of different entities, like digits, letters, words, etc */
int main() {
    int history[200];
    int d_counter, l_counter, w_counter, o_counter, g_counter;
    d_counter = l_counter = w_counter = o_counter = g_counter = 0;
    
    int c = getchar(); 
    while (c != EOF) {
        if (isdigit(c)) {
            ++d_counter;
        }
        else if (c == '\n' || c == '\t' || c == ' ') {
            if (history[g_counter > 2]) {
                if (isdigit(history[g_counter-2])) {
                    ;
                } 
                else if (
                    history[g_counter-2] != '\n' || 
                    history[g_counter-2] != '\t' || 
                    history[g_counter-2] != ' '
                ) {
                    ++w_counter;
                }
            }
            ++o_counter;
        }
        else {
            ++l_counter;
        }
        history[g_counter] = c;
        ++g_counter;
        c = getchar();
    }
    
    printf("\nDigits: %d \n", d_counter);
    for (int i = 0; i < d_counter; ++i) {
        printf("#");
    }
    
    printf("\nLetters: %d \n", l_counter);
    for (int i = 0; i < l_counter; ++i) {
        printf("#");
    }
    
    printf("\nWords: %d \n", w_counter);
    for (int i = 0; i < w_counter; ++i) {
        printf("#");
    }
    
    printf("\nOther: %d \n", o_counter);
    for (int i = 0; i < o_counter; ++i) {
        printf("#");
    }
    
    printf("\n");
    
}
