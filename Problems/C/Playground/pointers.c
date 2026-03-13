#include <stdio.h>

int arg1 = 5;
int arg2 = 10;

// this func increments copies of arg1 & arg2
// they are bound to function scope only!
void broken_addition(int arg1, int arg2) {
    arg1 = arg1 + 1;
    arg2 = arg2 + 2;
}

// modifng actual values with pointers
void correct_addition(int *arg1, int *arg2) {
    *arg1 = *arg1 + 1;
    *arg2 = *arg2 + 2;
}

int main() {
    broken_addition(arg1, arg2);
    printf("Incorrect results:\n");
    printf("%i, %i\n", arg1, arg2);
    
    correct_addition(&arg1, &arg2); // &arg1, &arg2 - passes actual variable
    printf("Correct results:\n");
    printf("%i, %i\n", arg1, arg2);
}
