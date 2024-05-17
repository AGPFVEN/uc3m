#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(){
    int fd, dupfd;
    //REDIRECT STDOUT
    fd = open("t.txt", O_CREAT | O_WRONLY | O_TRUNC);
    close(1); // close stdout
    dupfd = dup(fd); // STDOUT = fd
    close(fd); //close file
    printf ("prueba \n");
}