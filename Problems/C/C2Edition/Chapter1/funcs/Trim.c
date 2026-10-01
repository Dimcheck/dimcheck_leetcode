#include <stdio.h>
#define ARRAYLENGTH 40

void trimCharArray(char line[]);

int main() {
    char target_word[ARRAYLENGTH] = " HEY MOTHERLOVER   !  "; 
    printf("BEFORE:%s\n", target_word);
    trimCharArray(target_word);
    printf("AFTER:%s\n", target_word);
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
