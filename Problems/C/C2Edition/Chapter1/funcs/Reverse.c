#include <stdio.h>
#define ARRAYLENGTH 40

void reverseCharArray(char line[]);

int main() {
    // char target_word[ARRAYLENGTH] = " HEY MOTHERLOVER   !  "; 
    char target_word[ARRAYLENGTH] = ".HEY\n"; 
    printf("BEFORE:%s\n", target_word);
    reverseCharArray(target_word);
    printf("AFTER:%s\n", target_word);
}
    
void reverseCharArray(char line[]) {
    char swap, start, end;
    start = end = 0;

    while (line[end] != '\0') {end++;}
    end--;
    
    while (start <= end) {
        swap = line[start];
        line[start] = line[end];
        line[end] = swap;
        start++;
        end--;
    } 
}