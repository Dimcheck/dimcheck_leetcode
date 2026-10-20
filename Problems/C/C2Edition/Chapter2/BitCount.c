#include <stdio.h>

/* 
 * In a two's complement number system, 
 * x &= (x-1) deletes the rightmost 1-bitin x. 
 * Explain why. 
 * Use this observation to write a faster version of bitcount. 
 */


// Explanation:
//
// During <&> operation between <x> and <x-1> we can observe the the property of binary counting system. 
// Each <1> & <0> decimals represents a number in a byte.
// The higher the number the closer the bit is to the left edge of the byte.
// The rightmost <1> in <x> will correspond to rightmost <0> in <x-1>
// So during the <x & x-1> bitwise operation the rightmost bit it will become 0
//   
// 0000 0000 0000 1100 12 (x)
// 0000 0000 0000 1011 11 (x-1)
// ------------------- &
// 0000 0000 0000 1000 8 (x)
// 0000 0000 0000 0111 7 (x-1)
// ------------------- &
// 0000 0000 0000 0000


/* bitcount: count 1 bits in x */
int bitcount(unsigned x);
int bitcountv2(unsigned x);

int main() {
    unsigned x = 25;
    printf("Binary view: %b\n", x);
    printf("Function <bitcount>: %u\n", bitcount(x));
    printf("Function <bitcountv2>: %u\n", bitcountv2(x));
}

int bitcount(unsigned x) {
    int b;

    for (b = 0; x !=0; x>>=1) {
        if (x & 01) {
            b++;
        }
    }
    return b;
}

int bitcountv2(unsigned x) {
    int b;

    for (b = 0; x !=0; x&=(x-1)) {
        b++;
    }
    return b;
}