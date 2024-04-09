#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// execute the program with args: cat t.txt
// to see the perfect demonstation

int main(int argc, char** argv) {
    char *args[] = {"pwd", NULL};
    execvp("pwd", args);
    return 0;
}