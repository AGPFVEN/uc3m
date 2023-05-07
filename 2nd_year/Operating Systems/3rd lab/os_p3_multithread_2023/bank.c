//OS-P3 2022-2023

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <stddef.h>
#include <sys/stat.h>
#include <pthread.h>
#include "queue.h"
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>

#define MAX_OPERATIONS 200

/**
 * Entry point
 * @param argc
 * @param argv
 * @return
 */

int main (int argc, const char * argv[] ) {
    //Check if arguments number is correct
    if (argc != 6){
        printf("Invalid number of arguments\n");
        return -1;
    }

    //Open file with file descriptor
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1){
        printf("Error opening %s\n", argv[1]);
        return -1;
    }

    //Get file size
    struct stat st;
    stat(argv[1], &st);

    //Map file
    char *addr;
    addr = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);

    //Close file
    close(fd);

    //String and char to read file
    char file_reader = addr[0];
    char *command_reader;

    command_reader = (char*) malloc(st.st_size);

    //Find out number of commands
    int number_of_commands;

    for (int i = 0; file_reader != '\n'; i++) {
        file_reader = addr[i];
        printf("%c", file_reader);
    }



    printf("\n");
    return 0;
}
