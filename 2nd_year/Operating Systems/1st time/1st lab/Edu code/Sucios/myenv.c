#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    // Check if the program was called with at least one argument (the input file).
    if (argc < 2) {
        printf("Too few arguments. \nUsage: %s <input file>\n", argv[0]);
        return -1;
    }
    // Open the input file for reading.
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        printf("Error opening file %s\n", argv[1]);
        return -1;
    }
    // Open the output file, and if it already exists, it only opens it (O_CREAT)
    int fdo = open(argv[3], O_CREAT|O_RDWR, 0664);
    if (fdo < 0) {
        printf("Error opening file %s\n", argv[3]);
        return -1;
    }

    int character; // Where the character from the file is stored temporarily
    char *linea; // Each of the lines individually processed
    int line_length = 0;
    ssize_t n;
    linea = malloc(2);
    //linea2 = malloc(2);
    //printf("#%p#\n", linea);
    //printf("antes del copy\n");
    strcpy(linea, "");
    //printf("#%s#\n", linea);

    n = read(fd, &character, 1);
    if (n == 0){
        printf("File is empty");
        return(-1);
    }
    while (n > 0) {
        while ((character != '\n') && (n > 0)) {
            line_length++;
            linea = realloc(linea, 1+line_length);
            //printf("%p. In the line %d\n", linea, __LINE__);
            strcat(linea, (const char *) &character);
            //printf("%s\n", linea);
            // Prepared for the next character
            n = read(fd, &character, 1);
        }
        //printf("%s, %d\n", linea, __LINE__);

        //Add the \n character to the end of the line:
        //linea = realloc(linea, 1);
        //strcat(linea, "\n");

        //printf("Pre-Trace, %d\n", __LINE__);
        // Compare with argv[1]
        //printf("Line: %s -- Argument: %s -- %d", linea, argv[2], __LINE__);
        if (strstr(linea, argv[2]) != NULL) {
            //printf("Trace \nLine being #%s#\n", linea);
            // write(fdo, linea, line_length);
            if (write(fdo, linea, line_length) < line_length) {
                perror("Writing File");
                close(fd);
                close(fdo);
                exit(-1);
            }
            write(fdo, "\n", 1);
        }
        free(linea);
        linea = malloc(2);
        line_length = 0;
        n = read(fd, &character, 1);
    }
    // printf("Traza_final\n");
    close(fd);
    close(fdo);
    return 0;
}

