#include <stdio.h>
#include <stdlib.h>
#include "message.h"

// Global variables
CLIENT *clnt;

int init()
{
    enum clnt_stat retval;
    int ret;

    char *host = getenv("IP_TUPLAS");
    if (host = NULL){
        perror("IP_TUPLAS no declarado");
        exit(-1);
    }

    // inicializar RPC
    clnt = clnt_create(host, EJERCICIO3, EJERCICIO3_VERSION, "tcp");
    if (clnt == NULL){
        clnt_pcreateerror(host);
        return(-1);
    }

    // init 
    retval = d_init_1(&ret, clnt);
    if (retval != RPC_SUCCESS){
        clnt_perror(clnt, "d_init_1: ");
        return (-1);
    }

    return 1;
}