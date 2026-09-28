#include <stdio.h>
#define LOWER 0     /*                       */
#define UPPER 300  /*   SYMBOLIC CONSTANTS  */ 
#define STEP 20   /*                       */ 


/* 1-15 Functions improvement */
float cels_to_fahr (float celsius) {
    float fahr;
    fahr = (celsius * 1.8 + 32.0);
    return fahr;
}

float fahr_to_cels (float fahr) {
    float cels;
    cels = (5.0/9.0) * (fahr-32.0);
    return cels;
}


/* Fahrenheit-Celsius Converter */
// int main() {
//     float fahr, celsius;
//     fahr = LOWER; // fahr gets 0.0 from lower

//     printf("............\n");
//     printf("  F\tC\n");
//     printf("............\n");

//     while (fahr <= UPPER) {
//         celsius = fahr_to_cels(fahr);
//         printf("%3.0f %6.1f |\n", fahr, celsius);
//         fahr = fahr + STEP;
//     }
//     printf("............\n");
// }


/* Celsius-Fahrenheit Converter */
// int main() {
//     float fahr, celsius;
//     celsius = LOWER; // celsius gets 0.0 from LOWER

//     printf("............\n");
//     printf("  C\tF\n");
//     printf("............\n");

//     while (celsius <= UPPER) {
//         fahr = cels_to_fahr(celsius);
//         printf("%3.0f %6.1f |\n", celsius, fahr);
//         celsius = celsius + STEP;
//     }
//     printf("............\n");
// }


/* Fahrenheit-Celsius Converter in reverse order */
int main() {
    float fahr;
    
    printf("............\n");
    printf("  F\tC\n");
    printf("............\n");
    
    for (fahr=UPPER; fahr>=LOWER; fahr=fahr-STEP) {
        printf("%3.0f %6.1f |\n", fahr, fahr_to_cels(fahr));
    }
    printf("............\n");
}