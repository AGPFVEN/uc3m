
/*
 *  Copyright 2020-2024 Felix Garcia Carballeira, Alejandro Calderon Mateos,
 *
 *  This file is part of nanodt proyect.
 *
 *  nanodt is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  nanodt is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public License
 *  along with nanodt.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include "claves.h"
#include "mensajes.h"


int d_send_receive ( message_t *pr )
{
     int ret ;
     int sd_server ;
     struct sockaddr_in address;

     // open server sockets
     sd_server = socket(AF_INET, SOCK_STREAM, 0) ;
     if (sd_server <= 0) {
        perror("socket: ") ;
        exit(-1) ;
     }

     // connect
     address.sin_family = AF_INET ;
     address.sin_port   = htons(atoi(getenv("PORT_TUPLAS")));

     ret = inet_pton(AF_INET, getenv("IP_TUPLAS"), &address.sin_addr) ;
     if (ret <= 0) { 
         printf("\nInvalid address or address not supported\n") ;
	 close(sd_server) ;
         exit(-1);
     } 

     ret = connect(sd_server, (struct sockaddr *)&address, sizeof(address)) ;
     if (ret < 0) { 
         perror("connect: ");
	 close(sd_server) ;
         exit(-1);
     }

     // send request
     ret = write(sd_server, (char *)pr, sizeof(message_t)) ;
     if (ret < 0) {
	 perror("write: ") ;
	 close(sd_server) ;
         exit(-1);
     }

     // receive response
     ret = read(sd_server, (char *)pr, sizeof(struct message)) ;
     if (ret < 0) {
	 perror("read: ") ;
	 close(sd_server) ;
         exit(-1);
     }

     // close socket
     ret = close(sd_server) ;
     if (ret < 0) {
	 perror("close: ") ;
         exit(-1);
     }

     // return status
     return pr->status ;
}

int d_init ()
{
     message_t pr;

     // init message
     bzero(&pr, sizeof(struct message)) ;
     pr.op    = 1 ;

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}

int d_set_value (int key, char *value1, int N_value2, double *V_value2)
{
     message_t pr;

     // set message
     bzero(&pr, sizeof(struct message));
     pr.key = key;
     pr.op = 2;
     strcpy(pr.value1, value1);
     pr.N_value2 = N_value2; 
     for (int i = 0; i < N_value2; i++){
          pr.value2[i] = V_value2[i];
     }

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}

int d_get_value (int key, char *value1, int N_value2, double *V_value2)
{
     message_t pr;

     // get message
     bzero(&pr, sizeof(struct message));
     pr.op = 3;
     pr.key = key;
     pr.N_value2 = N_value2;

     // send request and receive response
     d_send_receive(&pr);
 
     // return value + status
     strcpy(value1, pr.value1);

     for (int i = 0; i < N_value2; i++){
          V_value2[i] = pr.value2[i];
     }

     return pr.status;
}

int d_modify_value(int key, char *value1, int N_value2, double *V_value2)
{
     message_t pr;

     // set message
     bzero(&pr, sizeof(message_t));
     pr.key = key;
     pr.op = 4;
     strcpy(pr.value1, value1);
     pr.N_value2 = N_value2; 
     for (int i = 0; i < N_value2; i++){
          pr.value2[i] = V_value2[i];
     }

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}

int d_delete_key(int key)
{
     message_t pr;

     // set message
     bzero(&pr, sizeof(struct message));
     pr.key = key;
     pr.op = 5;

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}

int d_exist(int key)
{
     message_t pr;

     // set message
     bzero(&pr, sizeof(struct message));
     pr.key = key;
     pr.op = 6;

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}