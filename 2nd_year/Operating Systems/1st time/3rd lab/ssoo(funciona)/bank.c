// OS-P3 2022-2023

#include "queue.h"
#include <fcntl.h>
#include <pthread.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define MAX_OPERATIONS 200

// all the global variables
char list_client_ops[MAX_OPERATIONS][50]; // two-dimensional array of characters
int **accounts;
int client_numop = 0;  // +1 each time an atm does something
int bank_numop = 0;    // +1 each time a worker does something
struct queue *circular_buffer;

pthread_mutex_t mutex;   // mutex for client_num_op
pthread_cond_t is_full;  // conditions to control when to access the buffer
pthread_cond_t is_empty;

/**
 * Entry point
 * @param argc
 * @param argv
 * @return
*/

void ATM() {
  while(client_numop<50){
    struct element inserts;

    if (pthread_mutex_lock(&mutex) != 0) {
      perror("Error lock mutex");
      exit(-1);
    }

    if (client_numop==50){

    }else{

      //If buffer empty wait
      while (queue_full(circular_buffer)==1){

        if (client_numop==50){

        if (pthread_mutex_unlock(&mutex) < 0) {
            perror("Error unlock mutex");
            exit(-1);
          }

          pthread_exit(NULL);
        }

			  pthread_cond_wait(&is_full, &mutex);
	    }

      //Last check (to avoid errors)
      if (client_numop==50){

       if (pthread_mutex_unlock(&mutex) < 0) {
          perror("Error unlock mutex");
          exit(-1);
        }

        pthread_exit(NULL);
      }

      //Increse client number of operations
      client_numop++;

      //General operations (allways done)
      char *token = strtok(list_client_ops[client_numop], " ");
      char first_letter = list_client_ops[client_numop][0];
      inserts.what = first_letter;
      token = strtok(NULL, " ");
      inserts.to_who = atoi(token);

      //Create
      if (first_letter == 'C') {
        inserts.by_who = 0;
        inserts.how_much = 0;
      }

      //Deposit
      else if (first_letter == 'D') {
        token = strtok(NULL, " ");
        inserts.how_much = atoi(token);
        token = strtok(NULL, " ");
        inserts.by_who = 0;
      }

      //Transfer
      else if (first_letter == 'T') {
        inserts.by_who=inserts.to_who;
        token = strtok(NULL, " ");
        inserts.to_who = atoi(token);
        token = strtok(NULL, " ");
        inserts.how_much = atoi(token);
      }

      //Withdrawal
      else if (first_letter == 'W') {
        token = strtok(NULL, " ");
        inserts.how_much = atoi(token);
        token = strtok(NULL, " ");
        inserts.by_who = 0;
      }

      //Balance
      else if (first_letter == 'B') {
        inserts.by_who = 0;
        inserts.how_much = 0;
      }

      //Enqueue
      int b = queue_put(circular_buffer, &inserts);
      if (b < 0) {
        perror("Error queue put");
        exit(-1);
      }

      //Buffer is not empty (Signal)
      if (pthread_cond_signal(&is_empty)!=0){
			  perror("Error activating on is_empty ");
        exit(-1);
      }
    }

    if (pthread_mutex_unlock(&mutex) < 0) {
      perror("Error unlock mutex");
      exit(-1);
    }
  }
}

void Worker(){

  while(bank_numop<50){

    //Lock mutex
    if (pthread_mutex_lock(&mutex) != 0) {
      perror("Error lock mutex");
      exit(-1);
    }

    if (bank_numop==50){

    }else{

      //Check if queue is empty
      while (queue_empty(circular_buffer)==1){

        //If queue is empty unlock and wait mutex
        if (bank_numop==50){
          if (pthread_mutex_unlock(&mutex) < 0) {
              perror("Error unlock mutex");
              exit(-1);
            }
          pthread_exit(NULL);
        }

        pthread_cond_wait(&is_empty, &mutex);
		  }

      //Last check
      if (bank_numop==50){

        if (pthread_mutex_unlock(&mutex) < 0) {
          perror("Error unlock mutex");
          exit(-1);
        }

        pthread_exit(NULL);
      }

      bank_numop++;
      struct element *worker_element = queue_get(circular_buffer);

      //Create
      if(worker_element->what == 'C'){
        accounts[worker_element->to_who][0] = worker_element->to_who;
        printf("%d CREATE %d BALANCE=%d TOTAL=%d\n", bank_numop, worker_element->to_who,accounts[worker_element->to_who][1], accounts[0][1]);
      }

      //Deposit
      else if (worker_element->what == 'D'){
        //global_balance = global_balance + worker_element->how_much;

        accounts[worker_element->to_who][1] = worker_element->how_much+accounts[worker_element->to_who][1];
        accounts[0][1] = worker_element->how_much+accounts[0][1];//this is the balance

        printf("%d DEPOSIT %d %d BALANCE=%d TOTAL=%d\n", bank_numop, accounts[worker_element->to_who][0],worker_element->how_much,accounts[worker_element->to_who][1], accounts[0][1]);
      }

      //Transfer
      else if (worker_element->what == 'T'){

        accounts[worker_element->to_who][1] = worker_element->how_much+accounts[worker_element->to_who][1];
        accounts[worker_element->by_who][1] =accounts[worker_element->by_who][1] - worker_element->how_much;

        printf("%d TRANSFER %d %d %d BALANCE=%d TOTAL=%d\n", bank_numop, worker_element->by_who ,worker_element->to_who,worker_element->how_much,accounts[worker_element->by_who][1], accounts[0][1]);
      }

      //Withdrawal
      else if (worker_element->what == 'W'){
        //global_balance = global_balance - worker_element->how_much;

        accounts[worker_element->to_who][1] =accounts[worker_element->to_who][1] - worker_element->how_much;
        accounts[0][1] = accounts[0][1] - worker_element->how_much;

        printf("%d WITHDRAW %d %d BALANCE=%d TOTAL=%d\n", bank_numop, worker_element->to_who,worker_element->how_much,accounts[worker_element->to_who][1], accounts[0][1]);
      }

      //Balance
      else if (worker_element->what == 'B'){
        printf("%d BALANCE %d BALANCE=%d TOTAL=%d\n", bank_numop, worker_element->to_who,accounts[worker_element->to_who][1], accounts[0][1]);
      }

      //Buffer is not empty
      if (pthread_cond_signal(&is_full)<0){
			  perror("Error activating on is_full ");
        exit(-1);
      }
    }

    if (pthread_mutex_unlock(&mutex) < 0) {
      perror("Error unlock mutex");
      exit(-1);
    }
  }
}

int main(int argc, const char *argv[]) {
  // Check if arguments number is correct
  if (argc != 6) {
    printf("Invalid number of arguments\n");
    return -1;
  }

  int num_ATMs;
  if (( num_ATMs = atoi(argv[2])) <= 0) {
    printf("Invalid number of ATM\n");
    return -1;
  }

  int num_workers;
  if ((num_workers = atoi(argv[3])) <= 0) {
    printf("Invalid number of workers\n");
    return -1;
  }

  int max_accounts;
  if ((max_accounts=atoi(argv[4])) <= 0) {
    printf("Invalid number of maximum accounts\n");
    return -1;
  }

  //Create queue
  circular_buffer = queue_init(atoi(argv[5]));

  //initialize size of the accounts array
  accounts = malloc((max_accounts+1) * sizeof(int *));//position 0 is for global balance
  for (int i = 0; i < max_accounts+1; i++) {
    accounts[i] = malloc(2 * sizeof(int));
  }

  //initialize to 0 all the accounts
  for (int i = 0; i < max_accounts+1; i++) {
      accounts[i][0] = 0;
      accounts[i][1] = 0;
  }

  // Open file with file descriptor
  int lines = 0;
  FILE *file;
  int numero1;
  char c;
  int row = 0;

  file = fopen(argv[1], "r");

  if (fscanf(file, "%d", &numero1) != 1) {
    printf("Error reading file.\n");
    return -1;
  }

  //process to check number of operations is the correct
  if (file) {
    while ((c = fgetc(file)) != EOF) {
      if (c == '\n') {
        lines++;
        list_client_ops[row][strlen(list_client_ops[row])] = c;
        row++; // move to the next row
      } else {
        list_client_ops[row][strlen(list_client_ops[row])] =
        c; // assign c to the current element of list_client_ops
      }
    }
    fclose(file);
    //printf("The file has %d lines.\n", lines + 1);
  } else {
    printf("Failed to open the file.\n");
  }

  if (numero1 != (lines - 1)) {
    printf("Incorrect number of operations\n");
    return -1;
  }

// initialize mutex
  if (pthread_mutex_init(&mutex, NULL)!=0){
		perror("error initializating mutex");
    		return -1;
	}

  if (pthread_cond_init(&is_full, NULL)!=0){
		perror("error initializing condition");
    		return -1;
	}

  if (pthread_cond_init(&is_empty, NULL)!=0){
		perror("error initializing condition");
    		return -1;
	}

//create all atms
pthread_t ATMs_working[num_ATMs];
  for (int i = 0; i < num_ATMs; i++){

    if(pthread_create(&ATMs_working[i], NULL, (void *)ATM,NULL)){
      			perror("Error creating thread");
      			return -1;
		}

  }

// create workers
  //printf("%d",num_workers);
  pthread_t workers_working[num_workers];
  for (int i = 0; i < num_workers; i++){

    if(pthread_create(&workers_working[i], NULL, (void *)Worker,NULL)){
      			perror("Error creating thread");
     			return -1;
		}

  }

  for (int i = 0; i < num_ATMs; i++){

    if(pthread_join(ATMs_working[i], NULL)){
      			perror("Error joining thread");
      			return -1;
		}

  }
    for (int i = 0; i < num_workers; i++){

    if(pthread_join(workers_working[i], NULL)){
      			perror("Error joining thread");
      			return -1;
		}

  }

//free all space used
queue_destroy(circular_buffer);
//free(list_client_ops);
free(accounts);

  if (pthread_mutex_destroy(&mutex)<0){
		perror("destroy mutex error");
    		return -1;
  }

  if (pthread_cond_destroy(&is_full)<0){
		perror("destroy condition error");
    		return -1;
	}
	if (pthread_cond_destroy(&is_empty)<0){
		perror("destroy condition error");
    		return -1;
	}
  return 0;
}
