#include <stdio.h>

void loop1() {
    int array[5] = {1, 2, 3, 4, 5};
    int counter = 0;
    
    while (counter < 5) {
        printf("Array element: %i\n", array[counter]);
        counter = counter + 1;
    }
}


void loop2() {
    int array[5] = {1, 2, 3, 4, 5};
    int counter = 0;

    do {
        printf("Array element: %i\n", array[counter]);
        counter = counter + 1;
    }
    while (counter < 5);
}

void loop3() {
    int array[5] = {1, 2, 3, 4, 5};
    for (int counter = 0; counter < 5; counter++) {
        printf("Array element: %i\n", array[counter]);
    }
}


int main() {
    loop3();
}