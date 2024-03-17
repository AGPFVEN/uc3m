#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>        /* For mode constants */
#include <mqueue.h>
#include <signal.h>

#include "claves.h"
#include "lib-mesg.h"


void tratar_peticion ( struct message * pr )
{
     int ret ;
     int qr ;

     switch (pr->op)
     {
         case 1: // INIT
                 pr->status = init() ;
		 printf(" %d = init();\n", pr->status) ;
                 break ;
         case 2: // SET
                 pr->status = set_value(pr->name, pr->value1, pr->i, pr->value2) ;
		 printf(" %d = set(%i, 0x%p, %i, %p);\n", pr->status ,pr->name, &(pr->value1), pr->i, &(pr->value2)) ;
                 break ;
         case 3: // GET
                 pr->status = get_value(pr->name, pr->value1, &(pr->i), pr->value2) ;
		 printf(" %d = get(%i, 0x%p, 0x%p, 0x%p);\n", pr->status, pr->name, &(pr->value1), &(pr->i), &(pr->value2)) ;
                 break ;
	 default:
		 printf(" unknown(%i);\n", pr->name) ;
                 break ;
     }

     qr = mq_open(pr->q_name, O_WRONLY) ;
     if (qr < 0) {
	 perror("mq_open: ") ;
         mq_close(qr);
	 return ;
     }

     ret = mq_send(qr, (char *)pr, 6, 0) ;
     if (ret < 0) {
	 perror("mq_send: ") ;
     }

     ret = mq_close(qr);
     if (ret < 0) {
	 perror("mq_close: ") ;
     }
}

char *q_name  = "/SERVIDOR" ;
int   do_exit = 0 ;

void sigHandler ( int signo )
{
     do_exit = 1 ;
}

int main ( int argc, char *argv[] )
{
     int ret ;
     struct message pr ;
     int qs ;
     struct mq_attr attr ;
     unsigned int prio ;
     struct sigaction new_action, old_action;

     // Initialize the queue attributes (attr)
     attr.mq_flags   = 0 ;
     attr.mq_maxmsg  = 10 ;
     attr.mq_msgsize = 3000;
     attr.mq_curmsgs = 0 ;

     // open server queue
     qs = mq_open(q_name, O_CREAT|O_RDONLY, 0664, &attr) ;
     if (qs < 0) {
	 perror("mq_open: ") ;
	 return -1 ;
     }

     // signal handler
     new_action.sa_handler = sigHandler ;
     sigemptyset (&new_action.sa_mask) ;
     new_action.sa_flags = 0 ;
     sigaction (SIGINT, NULL, &old_action) ;
     if (old_action.sa_handler != SIG_IGN) {
         sigaction (SIGINT, &new_action, NULL);
     }

     // receive and treat requests
     while (0 == do_exit)
     {
          ret = mq_receive(qs, (char *)&pr, 3000, &prio) ;
          if (ret < 0) {
	      perror("mq_receive: ") ;
	      continue;
          }

          tratar_peticion(&pr) ;
     }

     // end
     ret = mq_close(qs) ;
     if (ret < 0) {
	 perror("mq_close: ") ;
     }

     ret = mq_unlink(q_name);
     if (ret < 0) {
	 perror("mq_unlink: ") ;
     }

     printf("The End.\n") ;
     return 0 ;
}