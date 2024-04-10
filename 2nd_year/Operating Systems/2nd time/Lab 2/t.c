#include <stddef.h>			/* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

// execute the program with args: cat t.txt
// to see the perfect demonstation

int main(int argc, char** argv) {
    char *p;
    char *k;
    p = (char *) malloc (10);
    p = "k";
    printf("%s\n", p);
    p = (char *) realloc(p, 100);
    printf("%s\n", k);
    k = "jjjj";
    printf("%s\n", k);
    return 0;
}