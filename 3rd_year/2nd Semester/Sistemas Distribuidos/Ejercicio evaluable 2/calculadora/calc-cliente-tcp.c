  #include <unistd.h>
  #include <stdio.h>
  #include <string.h>
  #include <stdlib.h>
  #include "comm.h"

  int suma_remota ( int sd, int *r, int x, int y )
  {
      int ret;
      char    op;
      int32_t a, b, res ;

      op = 0; // operación sumar
      ret = sendMessage(sd, (char *) &op, sizeof(char));  // envía operación
      if (ret == -1) {
          printf("Error envío op\n");
          return -1;
      }

      a = htonl(x); // marshalling: a <- host to network long(x)
      ret = sendMessage(sd, (char *) &a, sizeof(int32_t)); // envía a
      if (ret == -1) {
          printf("Error envío a\n");
          return -1;
      }

      b = htonl(y); // marshalling: b <- host to network long(y)
      ret = sendMessage(sd, (char *) &b, sizeof(int32_t)); // envía b
      if (ret == -1) {
          printf("Error envío b\n");
          return -1;
      }

      ret = recvMessage(sd, (char *) &res, sizeof(int32_t)); // recibe respuesta
      if (ret == -1) {
          printf("Error en recepción\n");
          return -1;
      }
      *r = ntohl(res); // unmarshalling: *r <- network to host long(res)

      return 0 ;
  }

  int main ( int argc, char **argv )
  {
      int sd, ret, res;

      if (argc != 3) {
          printf("Uso: %s <dirección servidor> <puerto servidor>\n", argv[0]);
          printf("Ejemplo -> %s localhost 4200\n\n", argv[0]);
          return(0);
      }

      char *host = argv[1] ;
      int   port = atoi(argv[2]) ;

      sd = clientSocket(host, port) ;
      if (sd < 0) {
          printf("Error en clientSocket with %s:%d\n", host, port);
          return -1;
      }

      ret = suma_remota(sd, &res, 5, 2) ;
      if (ret < 0) {
          closeSocket(sd);
          return -1;
      }

      printf("Resultado de a+b es: %d\n", res);

      closeSocket(sd);
      return 0;
  }