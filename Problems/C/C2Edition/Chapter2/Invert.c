#include <stdio.h>

/* invert(x,p,n): returns x with the n bits that begin at
position p invrted(1-0, 0->1), leaving the other bits unchanged. */

unsigned invertBits(unsigned x, int postition, int bits);

int main() {
    unsigned x = 50;    // 0000 0000 0011 0010
    int position = 3;   //
    int bits = 4;       //
    // result in theory -> 0000 0000 0011 1101
    
    // unsigned x = 300;   // 0000 0001 0010 1100
    // int position = 7;   //
    // int bits = 4;       //
    // result in theory    -> 0000 0001 1101 1100

    printf("%u\n", invertBits(x, position, bits));
}

unsigned invertBits(unsigned x, int position, int bits) {
    unsigned mask = ~(~0u << bits); // 0000 0000 0000 1111
    int shift = position + 1 - bits;

    // invert x & maks it through target bits
    unsigned xInvertedBits = ~x & (mask << shift);
    // 1111 1110 1101 0011
    // 0000 0000 1111 0000
    // -------------------
    // 0000 0000 1101 0000

    unsigned xClearedBits = x & ~(mask << shift);
    // 0000 0001 0010 1100
    // 1111 1111 0000 1111
    // ------------------
    // 0000 0001 0000 1100

    return xClearedBits | xInvertedBits;
}