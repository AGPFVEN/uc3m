 #include <unistd.h>
 #include <stdio.h>
 #include <strings.h>
 #include <signal.h>
 #include "comm.h"

 int servicio ( int sc )
 {
     int ret ;
     char op;
     int32_t a, b, res;

     ret = recvMessage(sc, (char *) &op, sizeof(char)); // operación
     if (ret < 0) {
         printf("Error en recepción op\n");
         return -1 ;
     }

     ret = recvMessage(sc, (char *) &a, sizeof(int32_t)); // recibe a
     if (ret == -1) {
         printf("Error en recepción a\n");
         return -1 ;
     }
     a = ntohl(a); // unmarshalling

     ret = recvMessage(sc, (char *) &b, sizeof(int32_t)); // recibe b
     if (ret == -1) {
         printf("Error en recepción b\n");
         return -1 ;
     }
     b = ntohl(b); // unmarshalling

     res = 0;
     if (0 == op) res = a + b;
     if (1 == op) res = a - b;
     if (2 == op) res = a * b;
     if (3 == op) res = a / b;

     res = htonl(res); // marshalling
     ret = sendMessage(sc, (char *)&res, sizeof(int32_t));
     if (ret == -1) {
         printf("Error en envío\n");
         return -1 ;
     }

     return 0 ;
 }

 int the_end = 0;

 void sigHandler ( int signo )
 {
      the_end = 1 ;
 }

 int main ( int argc, char *argv[] )
 {
     int sd, sc;
     struct sigaction new_action, old_action;

     // crear socket
     sd = serverSocket(INADDR_ANY, 4200, SOCK_STREAM) ;
     if (sd < 0) {
         printf("SERVER: Error en serverSocket\n");
         return 0;
     }

     // si se presiona Ctrl-C el bucle termina
     new_action.sa_handler = sigHandler ;
     sigemptyset (&new_action.sa_mask) ;
     new_action.sa_flags = 0 ;
     sigaction (SIGINT, NULL, &old_action) ;
     if (old_action.sa_handler != SIG_IGN) {
         sigaction (SIGINT, &new_action, NULL);
     }

     while (0 == the_end)
     {
             // aceptar conexión con cliente
             sc = serverAccept(sd) ;
             if (sc < 0) {
                 printf("Error en serverAccept\n");
                 continue ;
             }

             // procesar petición
             servicio(sc) ;

             // cerrar conexión con cliente
             closeSocket(sc);
     }

     closeSocket(sd);
     return 0;
 }