#include <stdio.h>

int main() {
    char input[100]; // Assuming input won't exceed 100 characters

    printf("Enter your input: ");
    fgets(input, sizeof(input), stdin); // Read input from stdin

    printf("You entered: %s", input); // Print the input

    return 0;
}
