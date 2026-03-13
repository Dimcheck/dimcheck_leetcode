#include <stdio.h>
#include <stdlib.h>

const int ARRAY_LENGTH = 5;

void showElement(int i) {
    printf("%i\n", i);
}

int main() {
    /*  
     :malloc: returns a pointer to the allocated memory
     :args: number of bytes to allocate
     :sizeof: is used to calculate how much bytes the data type needs
    */
    int *dynamicArray = malloc(sizeof(int) * ARRAY_LENGTH);
    for (int counter = 0; counter < ARRAY_LENGTH; counter++) {
        dynamicArray[counter] = counter * 2;
        showElement(dynamicArray[counter]);
    }
}