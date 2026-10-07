#include <stdio.h>

/* setbits(x,p,n,y): returns x with the n bits that begin at
position p set to the rightmost n bits of y, leaving the other bits unchanged. */

unsigned setBits(unsigned x, int postition, int bits, unsigned y);

int main() {
    // unsigned x = 50;    // 0000 0000 0011 0010
    // int position = 3;   //
    // int bits = 4;       //
    // unsigned y = 43;    // 0000 0000 0010 1011

    // result in theory -> 0000 0000 0011 1011
    
    unsigned x = 300;   // 0000 0001 0010 1100
    int position = 7;   //
    int bits = 4;       //
    unsigned y = 35;    // 0000 0000 0010 0011

    // result in theory -> 0000 0001 0011 1100

    printf("%u\n", setBits(x, position, bits, y));
}


unsigned setBits(unsigned x, int position, int bits, unsigned y) {
    unsigned mask = ~(~0u << bits); // 0000 0000 0000 1111
    int shift = position + 1 - bits;

    // clear the target bits in x
    x = x & ~(mask << shift);
    // 0000 0001 0010 1100
    // 1111 1111 0000 1111
    // -------------------
    // 0000 0001 0000 1100
     
    // extract the rightmost bits of y
    y = y & mask;
    // 0000 0000 0010 0011
    // 0000 0000 0000 1111
    // -------------------
    // 0000 0000 0000 0011
    
    // move them into position
    y = y << shift;
    // 0000 0000 0011 0000

    // combine them
    return x | y;
    // 0000 0001 0000 1100
    // 0000 0000 0011 0000
    // -------------------
    // 0000 0001 0011 1100
}
