#ifndef PETICION_H
#define PETICION_H

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <sys/time.h>

    struct peticion{
        long id;
        /*Resto de campos*/
        int tipo;
        /*...*/
    };
    
    typedef struct peticion peticion_t;

    // mensaje para el proceso ligero
    struct message_thread
    {
        int (*operacion)(void);
    };
    typedef struct message_thread message_thread_t;

    void recibir_peticion   (peticion_t *p);
    void responder_peticion (peticion_t *p);
#endif