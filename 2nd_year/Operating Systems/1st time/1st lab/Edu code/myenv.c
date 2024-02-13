#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    // Check if the program was called with at least one argument (the input file).
    if (argc < 2) {
        printf("Too few arguments. \nUsage: %s <string> <output file>\n", argv[0]);
        return -1;
    }
    // Open the input file for reading, if the parameter is an argument:
    //int fd = open(argv[1], O_RDONLY);
    //if (fd < 0) {
    //printf("Error opening file for reading %s\n", argv[1]);
    //return -1;
    //}
    //As it is not:
    int fd = open("env.txt", O_RDONLY);
    if (fd < 0) {
        printf("Error opening file for reading env.txt\n");
        return -1;
    }


    // Open the output file, and if it already exists, it only opens it (O_CREAT)
    int fdo = open(argv[2], O_CREAT|O_WRONLY|O_TRUNC, 0664);
    if (fdo < 0) {
        printf("Error opening file to write %s\n", argv[2]);
        return -1;
    }

    char character; // Where the character from the file is stored temporarily
    char *linea; // Each of the lines individually processed
    char *pointer;
    int line_length = 0;
    int j;
    int correct;

    char *needle;
    needle = malloc(strlen(argv[1])+2);
    strncpy(needle, argv[1], strlen(argv[1]));
    strncat(needle, "=",1);

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
        correct = 0;
        while ((character != '\n') && (n > 0)){
            //printf("character => #%s#\n", &character);
            //while ((character != '\n') && (n > 0)) {
            line_length++;
            pointer = realloc(linea, strlen(linea)+2);
            linea = pointer;
            strncat(linea, (const char *) &character, 1);
            n = read(fd, &character, 1);
        }
        //printf("Antes de comparar en la linea %i\n", __LINE__);
        if ((strstr(linea, needle) != NULL) && (linea[0] == needle[0])){
            correct = 1;
            for(j = 0; j < strlen(needle); j++){
                if (needle[j] != linea[j]){
                    correct = 0;
                }
            }
            if (correct == 1) {
                //printf("Match, con linea -> #%s#\n", linea);
                if (write(fdo, linea, line_length) < line_length) {
                    perror("Writing File");
                    close(fd);
                    close(fdo);
                    exit(-1);
                }
                //Adds a new line, as the exercise was undestood as all the ocurrences of the pattern
                write(fdo, "\n", 1);
                // This return helps to speed up the process as if an occurrence is found, it is written,
                // and it will exit immediately. This works if we only wanted one instance of the variable,
                // as it is not the case, we can't use this approach
                //close(fd);
                //close(fdo);
                //exit(0);
            }
        }
        free(linea);
        linea = malloc(2);
        strcpy(linea, "");
        line_length = 0;
        n = read(fd, &character, 1);
    }
    close(fd);
    close(fdo);
    return 0;
}

