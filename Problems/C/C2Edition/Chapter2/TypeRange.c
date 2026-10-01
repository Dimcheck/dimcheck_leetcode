#include <stdio.h>

/* Write a program  that determines/prints the ranges of char, short, int, long */

// NOTE: when the overflow for a type happens the numbers will start to cycle

void charSize();
void intSize();
void shortSize();
void longSize();


int main() {
    charSize();
    // intSize();
    // shortSize();
    // longSize();
}


void longSize() {
    long int foo = 0;
    long int upperLimit = 0;
    long int lowerLimit = 0;

    while (foo <= 0) {--foo;}
    upperLimit = foo;

    foo = 0;
    while (foo >= 0) {++foo;}; 
    lowerLimit = foo;
    
    printf("LONG_INT RANGE\nFROM: %ld \nTO: %ld", lowerLimit, upperLimit);
}


void shortSize() {
    short int foo = 0;
    short int upperLimit = 0;
    short int lowerLimit = 0;

    while (foo <= 0) {--foo;}
    upperLimit = foo;

    foo = 0;
    while (foo >= 0) {++foo;}; 
    lowerLimit = foo;
    
    printf("SHORT_INT RANGE\nFROM: %i \nTO: %i", lowerLimit, upperLimit);
}

void intSize() {
    int foo = 0;
    int upperLimit = 0;
    int lowerLimit = 0;

    while (foo <= 0) {--foo;}
    upperLimit = foo;

    foo = 0;
    while (foo >= 0) {++foo;}; 
    lowerLimit = foo;
    
    printf("INT RANGE\nFROM: %i \nTO: %i", lowerLimit, upperLimit);
}


void charSize() {
    char foo = 0;
    char upperLimit = 0;
    char lowerLimit = 0;

    while (foo <= 0) {--foo;}
    upperLimit = foo;

    foo = 0;
    while (foo >= 0) {++foo;}; 
    lowerLimit = foo;
    
    printf("CHAR RANGE\nFROM: %i \nTO: %i", lowerLimit, upperLimit);
}