#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Too few arguments. \nUsage: %s <input file>\n", argv[0]);
        return -1;
    }
    int fd = open(argv[1], O_RDONLY);
    if (fd < 0) {
        printf("Error opening file read %s\n", argv[1]);
        return -1;
    }
    int fdo = open(argv[3], O_CREAT|O_RDWR, 0664);
    if (fdo < 0) {
        printf("Error opening file write %s\n", argv[3]);
        return -1;
    }

    int character;
    char *linea;
    int line_length = 0;
    ssize_t n;

    linea = malloc(2);
    strcpy(linea, "");
    n = read(fd, &character, 1);
    if (n == 0){
        printf("File is empty");
        return(-1);
    }

    while (n > 0) {
        while ((character != '\n') && (n > 0)) {
            line_length++;
            linea = realloc(linea, 1+line_length);
            strcat(linea, (const char *) &character);
            n = read(fd, &character, 1);
        }
        if (strstr(linea, argv[2]) != NULL) {
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
    close(fd);
    close(fdo);
    return 0;
}

