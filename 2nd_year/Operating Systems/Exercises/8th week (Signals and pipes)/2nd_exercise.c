#include<stdio.h>
#include<signal.h>

//---------------------------Teacher solution----------------------
void capture_signal(int signal_){
    printf("It has been produced an error trying to occupy invalid memory\n");
    signal(SIGSEGV, SIG_DFL);
}

int main(int argc, char *argv[]){
    int *p;
    signal(SIGSEGV, capture_signal);
    printf("I have put the manager\n");
    p = 0; // Put pointer in memory position 0
    printf("I will put a 5 inside the pointer\n");
    *p = 5;
}