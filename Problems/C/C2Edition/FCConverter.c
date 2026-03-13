#include <stdio.h>
#define LOWER 0     /*                       */
#define UPPER 300  /*   SYMBOLIC CONSTANTS  */ 
#define STEP 20   /*                       */ 


/* Fahrenheit-Celsius Converter */
// int main() {
//     float fahr, celsius;
//     fahr = LOWER; // fahr gets 0.0 from lower
    
//     printf("............\n");
//     printf("  F\tC\n");
//     printf("............\n");

//     while (fahr <= UPPER) {
//         celsius = (5.0/9.0) * (fahr-32.0);
//         printf("%3.0f %6.1f |\n", fahr, celsius);
//         fahr = fahr + STEP;
//     }
//     printf("............\n");
// }


/* Celsius-Fahrenheit Converter */
// int main() {
//     float fahr, celsius;
//     celsius = LOWER; // celsius gets 0.0 from lower

//     printf("............\n");
//     printf("  C\tF\n");
//     printf("............\n");

//     while (celsius <= UPPER) {
//         fahr = (celsius * 1.8 + 32.0);
//         printf("%3.0f %6.1f |\n", celsius, fahr);
//         celsius = celsius + STEP;
//     }
//     printf("............\n");
// }


/* Fahrenheit-Celsius Converter in reverse order */
int main() {
    int fahr;
    
    printf("............\n");
    printf("  C\tF\n");
    printf("............\n");
    
    for (fahr=UPPER; fahr>=LOWER; fahr=fahr-STEP) {
        printf("%3d %6.1f |\n", fahr, (5.0/9.0) * (fahr-32.0));
    }
    printf("............\n");
}