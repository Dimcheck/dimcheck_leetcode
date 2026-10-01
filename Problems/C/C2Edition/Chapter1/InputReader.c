#include <stdio.h>
#include <ctype.h>

#define IN 1  /* inside a word */
#define OUT 0 /* otside a word */

///////////////
/* EOF is -1 */
/* :getchar: takes a single input character: WORLD -> W */
/* Use Ctrl+D  to send EOF from keyboard*/
//////////////

/* print a horizontal histogram of different entities, like digits, letters, words, etc */
int main() {
    int history[200];
    int d_counter, l_counter, w_counter, c_counter, word_state, c;
    d_counter = l_counter = w_counter = c_counter = 0;

    word_state = OUT;
    while ((c = getchar()) != EOF) {
        if (isdigit(c)) {
            ++d_counter;
        }
        else if (c == '\n') {
            ++l_counter;
            word_state = OUT;
            ++w_counter;

        }
        else if (c == ' ' || c == '\t') {
            word_state = OUT;
            ++w_counter;

        }
        else {
            word_state = IN;
            ++c_counter;
        }

    }

    printf("\nDigits: %d \n", d_counter);
    for (int i = 0; i < d_counter; ++i) {
        printf("#");
    }

    printf("\nLines: %d \n", l_counter);
    for (int i = 0; i < l_counter; ++i) {
        printf("#");
    }

    printf("\nWords: %d \n", w_counter);
    for (int i = 0; i < w_counter; ++i) {
        printf("#");
    }

    printf("\nCharacters: %d \n", c_counter);
    for (int i = 0; i < c_counter; ++i) {
        printf("#");
    }

    printf("\n");
}


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
