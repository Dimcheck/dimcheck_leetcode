#include <stdlib.h>
#include <stdio.h>

int in(int *sequence, int sequenceSize, int targetNumber) {
    /*  C doesn't have its own :in: operator  */
    for (int i = 0; i < sequenceSize; i++) {
        if (sequence[i] == targetNumber) {
            printf("1\n");
            return 1;
        }
    }
    printf("0\n");
    return 0;
}

// returns a pointer to some memory address
int* arrayGenerator(int size, int multiplier) {
    int *vla = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        vla[i] = i * multiplier;
    }
    return vla;
}

int main() {
    int size = 5;
    int multiplier = 2;
    int target = 3;
    
    int *a1 = arrayGenerator(size, multiplier); // go to the memory address and store an array created by func
    in(a1, size, target);
    free(a1);                                   // free allocated memory from array
    return 0;
}