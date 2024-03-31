#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <arpa/inet.h>

int read_all ( int sd, char *buffer, size_t total )
{
    size_t  leidos = 0 ;
    ssize_t result = 0 ;

    while (leidos != total) // mientras queda por leer...
    {
       // puede que read NO lea todo lo solicitado de una vez
       result = read(sd, buffer+leidos , total-leidos ) ;
       if (-1 == result) {
           return -1 ;
       }

       leidos = leidos + result ;
    }

    return leidos ;
}

int main ( int argc, char **argv )
{
    char *maquina; short puerto;
    struct sockaddr_in server_addr;
    struct hostent *hp;
    int sd, ret;

    if (argc != 3) {
        printf("Uso: %s <IP máquina> <puerto>\n", argv[0]);
        return 0;
    }

    maquina = argv[1] ;
    puerto  = (short) atoi(argv[2]);
    hp = gethostbyname(maquina);
    if (NULL == hp) {
        printf("ERROR en gethostbyname con '%s'\n", maquina) ;
        return -1 ;
    }

    // (1) creación del socket (NO tiene dirección asignada aquí)
    sd = socket(AF_INET, SOCK_STREAM, 0);
    if (sd < 0) {
        perror("ERROR en socket: ") ;
        return -1 ;
    }

    // (2) obtener la dirección
    bzero((char *)&server_addr, sizeof(server_addr));
    memcpy (&(server_addr.sin_addr), hp->h_addr, hp->h_length);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(puerto);

    // (3) Solicitud de conexión (con socket remoto)
    // * si el socket local no tiene dirección asignada
    //   entonces se le asigna una automáticamente con puerto temporal
    ret = connect(sd, (struct sockaddr *) &server_addr, sizeof(server_addr)) ;
    if (ret < 0) {
        perror("ERROR en connect: ");
        return -1;
    }

    // Preparar el espacio para recepción del mensaje
    char buffer[1024] ;
    strcpy(buffer, "") ;

    // (4) transferir datos sobre sd
    size_t leidos = read_all(sd, buffer, sizeof(buffer)) ;
    if (leidos < 0) {
        printf("Error al leer buffer\n") ;
    }

    // Imprimir el mensaje recibido
    printf("mensaje del servidor: %s\n", buffer) ;

    // (5) Cerrar socket
    close(sd);

    return 0;
}
/*
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#define BUF_SIZE 500

int main(int argc, char *argv[]){
    int                      sfd, s;
    char                     buf[BUF_SIZE], *port = "3000", *port2 = "8000";
    ssize_t                  nread;
    socklen_t                peer_addrlen;
    struct addrinfo          hints;
    struct addrinfo          *result, *rp;
    struct sockaddr_storage  peer_addr;

    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;    // Allow IPv4 or IPv6
    hints.ai_socktype = SOCK_DGRAM; // Datagram socket        change to SOCK_STREAM
    hints.ai_flags = 0;
    hints.ai_protocol = 0;          // Any protocol

    if (s = getaddrinfo(port, port2, &hints, &result) != 0){
        printf("error con getaddrinfo: %s\n",gai_strerror(s));
        return -1;
    }
}*/