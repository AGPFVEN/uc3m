#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdarg.h>
#include"peticiones.h"

int kk(int j){
    printf("va %i\n", j);
    return 1;
}

int main(){
    message_thread_t msg;
    msg.operacion = kk;
    msg.operacion(14);
}