#include <stdio.h>

/* getbits: get n bits from position p */
unsigned getBits(unsigned x, int p, int b);


int main() {
    unsigned x = 25;  // 0000 0000 0001 1001
    int position = 4; //              ^
    int bits = 2;     // 11

    printf("%u\n", getBits(x, position, bits));
    
}

unsigned getBits(unsigned x, int p, int b) {
    // create a negation of 0, which will get filled with 111.. as 0 in binary is 000..
    // left shift this negated 0 by "b" amount so we will get 1111 1111 1111 1100 & then negate again so we will get 0000 0000 0000 0011
    // right shift existing binary number "x" representation by p+1-b, so we will get 0000 0000 0000 0011
    // do a bit mask with "&" bit operator: 
    // 0000 0000 0000 0011
    // 0000 0000 0000 0011
    // -------------------
    // 0000 0000 0000 0011
    return (x >> (p+1-b)) & ~(~0 << b);
}