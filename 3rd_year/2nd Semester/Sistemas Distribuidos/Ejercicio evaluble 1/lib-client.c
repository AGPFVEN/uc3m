#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <errno.h>

#include "lib-client.h"
#include "lib-mesg.h"


int d_send_receive ( struct message *pr ){
    int  ret ;
    char qr_name[1024] ;
    struct mq_attr attr;
    int qs, qr ;
    unsigned prio ;

    /* Initialize the queue attributes (attr) */
    bzero(&attr, sizeof(struct mq_attr)) ;
    attr.mq_flags   = 0 ;
    attr.mq_maxmsg  = 10 ;
    attr.mq_msgsize = 10 ;
    attr.mq_curmsgs = 0 ;

 // qs = mq_open("/SERVIDOR", O_WRONLY, 0700, &attr) ;
    qs = mq_open("/SERVIDOR", O_WRONLY) ;
    if (qs == -1) {
	    perror("mq_open: ") ;
	    return -1 ;
    }

    sprintf(qr_name, "%s%d", "/CLIENTE_", getpid()) ;
    qr = mq_open(qr_name, O_CREAT|O_RDONLY, 0664, &attr) ;
    if (qr == -1) {
	    perror("mq_open: ") ;
	    mq_close(qs) ;
	    return -1;
    }
    strcpy(pr->q_name, qr_name);
    printf("%s size = %ld\n", pr->q_name, sizeof(pr->q_name));

    // send request
    ret = mq_send(qs, (char *)pr, 10, 0) ;
    if (ret < 0) {
        printf("%ld\n", sizeof(qs));
	    perror("mq_send");
	    mq_close(qs);
	    mq_close(qr);
        mq_unlink(qr_name);
	    return -1;
    }

    // receive response
    ret = mq_receive(qr, (char *)pr, sizeof(struct message), &prio) ;
    if (ret < 0) {
	    perror("mq_receive: ") ;
	    mq_close(qs) ;
	    mq_close(qr) ;
        mq_unlink(qr_name) ;
	    return -1;
    }

    // close queues
    ret = mq_close(qs);
    if (ret < 0) {
	    perror("mq_close: ") ;
    }
    ret = mq_close(qr);
    if (ret < 0) {
	    perror("mq_close: ") ;
    }
    ret = mq_unlink(qr_name);
    if (ret < 0) {
	    perror("mq_unlink: ") ;
    }

    // return status
    return pr->status ;
}

int d_init ( char  *nombre,  int  N ){
    struct message pr;

    // init message
    bzero(&pr, sizeof(struct message)) ;
    pr.op    = 1 ;

    // send request and receive response
    d_send_receive(&pr) ;

    // return status
    return pr.status ;
}

int d_set (int key, char *value1, int N_value2, double *V_value2)
{
    struct message pr;

    // set message
    bzero(&pr, sizeof(struct message));
    pr.op     = 2;
    pr.name   = key;
    pr.value1 = value1;
    pr.i      = N_value2;
    pr.value2 = V_value2;

     // send request and receive response
     d_send_receive(&pr) ;

     // return status
     return pr.status ;
}

int d_get ( char *nombre, int i, int *valor )
{
     struct message pr;

     // get message
     bzero(&pr, sizeof(struct message)) ;
     pr.op    = 3 ;
     pr.i     = i ;

     // send request and receive response
     d_send_receive(&pr) ;

     // return value + status
     // *valor = pr.value ;
     return pr.status ;
}