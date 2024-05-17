//P2-SSOO-23/24

//  MSH main file
// Write your msh source code here

//#include "parser.h"
#include <stddef.h>			/* NULL */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>

#define MAX_COMMANDS 8


// files in case of redirection
char filev[3][64];

//to store the execvp second parameter
char *argv_execvp[8];

void siginthandler(int param)
{
	printf("****  Exiting MSH **** \n");
	//signal(SIGINT, siginthandler);
	exit(0);
}

/* myhistory */

/* myhistory */

struct command
{
  // Store the number of commands in argvv
  int num_commands;
  // Store the number of arguments of each command
  int *args;
  // Store the commands
  char ***argvv;
  // Store the I/O redirection
  char filev[3][64];
  // Store if the command is executed in background or foreground
  int in_background;
};

int history_size = 20;
struct command * history;
int head = 0;
int tail = 0;
int n_elem = 0;

void free_command(struct command *cmd)
{
    if((*cmd).argvv != NULL)
    {
        char **argv;
        for (; (*cmd).argvv && *(*cmd).argvv; (*cmd).argvv++)
        {
            for (argv = *(*cmd).argvv; argv && *argv; argv++)
            {
                if(*argv){
                    free(*argv);
                    *argv = NULL;
                }
            }
        }
    }
    free((*cmd).args);
}

void store_command(char ***argvv, char filev[3][64], int in_background, struct command* cmd)
{
    int num_commands = 0;
    while(argvv[num_commands] != NULL){
        num_commands++;
    }

    for(int f=0;f < 3; f++)
    {
        if(strcmp(filev[f], "0") != 0)
        {
            strcpy((*cmd).filev[f], filev[f]);
        }
        else{
            strcpy((*cmd).filev[f], "0");
        }
    }

    (*cmd).in_background = in_background;
    (*cmd).num_commands = num_commands-1;
    (*cmd).argvv = (char ***) calloc((num_commands) ,sizeof(char **));
    (*cmd).args = (int*) calloc(num_commands , sizeof(int));

    for( int i = 0; i < num_commands; i++)
    {
        int args= 0;
        while( argvv[i][args] != NULL ){
            args++;
        }
        (*cmd).args[i] = args;
        (*cmd).argvv[i] = (char **) calloc((args+1) ,sizeof(char *));
        int j;
        for (j=0; j<args; j++)
        {
            (*cmd).argvv[i][j] = (char *)calloc(strlen(argvv[i][j]),sizeof(char));
            strcpy((*cmd).argvv[i][j], argvv[i][j] );
        }
    }
}


/**
 * Get the command with its parameters for execvp
 * Execute this instruction before run an execvp to obtain the complete command
 * @param argvv
 * @param num_command
 * @return
 */
void getCompleteCommand(char*** argvv, int num_command) {
	//reset first
	for(int j = 0; j < 8; j++)
		argv_execvp[j] = NULL;

	int i = 0;
	for ( i = 0; argvv[num_command][i] != NULL; i++)
		argv_execvp[i] = argvv[num_command][i];
}


/**
 * Main sheell  Loop  
 */
int main(int argc, char* argv[])
{
    //My variables

	/**** Do not delete this code.****/
	int end = 0; 
	int executed_cmd_lines = -1;
	char *cmd_line = NULL;
	char *cmd_lines[10];

	if (!isatty(STDIN_FILENO)) {
		cmd_line = (char*)malloc(100);
		while (scanf(" %[^\n]", cmd_line) != EOF){
			if(strlen(cmd_line) <= 0) return 0;
			cmd_lines[end] = (char*)malloc(strlen(cmd_line)+1);
			strcpy(cmd_lines[end], cmd_line);
			end++;
			fflush (stdin);
			fflush(stdout);
		}
	}

	/*********************************/

	char ***argvv = NULL;
	int num_commands;

	history = (struct command*) malloc(history_size *sizeof(struct command));
	int run_history = 0;

	while (1) 
	{
		int status = 0;
		int command_counter = 0;
		int in_background = 0;
		signal(SIGINT, siginthandler);

		if (run_history)
        {
            run_history=0;
        }
        else{
            // Prompt 
            write(STDERR_FILENO, "MSH>>", strlen("MSH>>"));

            // Get command
            //********** DO NOT MODIFY THIS PART. IT DISTINGUISH BETWEEN NORMAL/CORRECTION MODE***************
            executed_cmd_lines++;
            if( end != 0 && executed_cmd_lines < end) {
                command_counter = read_command_correction(&argvv, filev, &in_background, cmd_lines[executed_cmd_lines]);
            }
            else if( end != 0 && executed_cmd_lines == end)
                return 0;
            else
                command_counter = read_command(&argvv, filev, &in_background); //NORMAL MODE
        }
		//************************************************************************************************
		/************************ STUDENTS CODE ********************************/
	    if (command_counter > 0) {
			if (command_counter > MAX_COMMANDS){
				printf("Error: Maximum number of commands is %d \n", MAX_COMMANDS);
			} else {
				// Print command
				print_command(argvv, filev, in_background);
                
                //history management
                struct command cmd;
                run_history++;
                if (run_history > 20){
                    free_command(&history[19]);
                }
				store_command(argvv, filev, in_background, &cmd);

                if (strcmp(argvv[0][0], "myhistory") == 0) {
                    if (argvv[0][1] == NULL){
                        //for (int i = 0; i < run_history; i++){
                            //int num_args_in_command = 0;
                            //while(history[i].argvv[] != NULL){

                            //}
                            //printf("%i ", i);
                        //}
                    } else {
                        int num_in_history = atoi(argvv[0][1]);
                        if ((num_in_history > run_history) || (num_in_history < 0)){
                            printf("ERROR: command not found\n");
                        } else {
                            argvv = history[num_in_history].argvv;
                            for (int i=0; i<3; i++){
                                strcpy(filev[i], history[num_in_history].filev[i]);
                            }
                            in_background = history[num_in_history].in_background;
                        }
                    }

                }

                if (strcmp(argvv[0][0], "exit") == 0) {
                    printf("exiting...\n");
                    while (1) {
                        exit(0);
                    }
                }
                
                if (strcmp(argvv[0][0], "mycalc") == 0) {
                    // Command execution
                    if ((argvv[0][1] == NULL) || (argvv[0][2] == NULL) || (argvv[0][3] == NULL) ||
                        (argvv[0][4] != NULL)) {
                        fprintf(stderr, "[ERROR] The structure of the command is mycalc <operand_1> <add/mul/div> <operand_2>\n");
                    } else {
                        // 1. Get the first number
                        long first_number = atol(argvv[0][1]);
                        // 2. Get the second number
                        long second_number = atol(argvv[0][3]);
                        // 3. Get the operator + result + print
                        char operator_str[3];
                        strcpy(operator_str, argvv[0][2]);

                        if (strcmp(operator_str, "add") == 0) {
                            long int acc_local_int;
                            long int result = first_number + second_number;
                            char acc_local[25];
                            strcpy(acc_local, getenv("Acc"));
                                acc_local_int = atoi(acc_local);
                                acc_local_int += result;
                                sprintf(acc_local, "%li", acc_local_int);
                                setenv("Acc", acc_local, 1);
                                fprintf(stderr, "[OK] %li + %li = %li; Acc %li\n", first_number, second_number, result, acc_local_int);

                        } else if (strcmp(operator_str, "mul") == 0) { // Multiplication
                            long result = first_number * second_number;
                            fprintf(stderr, "[OK] %li * %li = %li\n", first_number, second_number, result);

                        } else if (strcmp(operator_str, "div") == 0) { // Division
                            long result = first_number / second_number;
                            fprintf(stderr, "[OK] %li / %li = %li; Remainder %d\n", first_number, second_number, result,
                                   (int) first_number % (int) second_number);

                        } else {
                            printf("[ERROR] The structure of the command is mycalc <operand_1> <add/mul/div> <operand_2>\n");
                        }
                    }
                }

                //Buscar formas de mejorar---------------------------------------------------------
                int proceses_pipes[command_counter - 1][2];
                int fd_open;

                if (command_counter > 1){
                    for (int i = 0; i < command_counter; i++){
                        if ((pipe(proceses_pipes[i])) == -1){
                            perror("Error creating pipes");
                            exit(EXIT_FAILURE);
                        }
                    }
                }

                if (command_counter == 2){
                    // Deletes father but accomplishes the task
                    int fd[2];
                    pipe(fd);
                    if (fork()!=0) { /* código del parent */
                        // handle output redirection if exists
                        if (filev[1][0] != '0')
                        {
                            // open file
                            if ((fd_open = open(filev[1], O_WRONLY | O_CREAT)) == -1 ){
                                perror("Error opening file at redirection output");
                                exit(EXIT_FAILURE);
                            }

                            // pipe handling
                            close(STDOUT_FILENO);
                            dup(fd_open);
                            close(fd_open);
                        }

                        close(STDIN_FILENO);
                        dup(fd[STDIN_FILENO]);
                        close(fd[STDIN_FILENO]);
                        close(fd[STDOUT_FILENO]);
                        execvp(argvv[1][0], argvv[1]);

                    } else { /* código del child */
                        // handle input redirection if exists
                        if (filev[0][0] != '0')
                        {
                            // open file
                            int fd_open;
                            if ((fd_open = open(filev[0], O_RDONLY)) == -1 ){
                                perror("Error opening file at redirection input");
                                exit(EXIT_FAILURE);
                            }

                            // pipe handling
                            close(STDIN_FILENO);
                            dup(fd_open);
                            close(fd_open);
                        }

                        close(STDOUT_FILENO);
                        dup(fd[STDOUT_FILENO]);
                        close(fd[STDOUT_FILENO]);
                        close(fd[STDIN_FILENO]);
                        execvp(argvv[0][0], argvv[0]);
                    }
                } else{

                    for (int i = 0; i < command_counter; i++){
                        int pid = fork();
                        switch(pid){
                            case -1: // ------------------ need more specidics 
                                perror("Error at creating new process");
                                exit(EXIT_FAILURE);

                            case 0: // Son process

                                // first command process
                                if (i == 0)
                                {
                                
                                    // handle input redirection if exists
                                    if (filev[0][0] != '0')
                                    {
                                        // open file
                                        int fd_open;
                                        if ((fd_open = open(filev[0], O_RDONLY)) == -1 ){
                                            perror("Error opening file at redirection input");
                                            exit(EXIT_FAILURE);
                                        }

                                        // pipe handling
                                        close(STDIN_FILENO);
                                        dup(fd_open);
                                        close(fd_open);
                                    }
                                } else {
                                    //dup2(proceses_pipes[i - 1][0], STDIN_FILENO);
                                    close(STDIN_FILENO);
                                    dup(proceses_pipes[i - 1][0]);
                                    close(proceses_pipes[i - 1][0]);
                                    close(proceses_pipes[i - 1][1]);
                                }

                                // last process
                                if (i == command_counter - 1)
                                {
                                    // handle output redirection if exists
                                    if (filev[1][0] != '0')
                                    {
                                        // open file
                                        if ((fd_open = open(filev[1], O_WRONLY | O_CREAT)) == -1 ){
                                            perror("Error opening file at redirection output");
                                            exit(EXIT_FAILURE);
                                        }

                                        // pipe handling
                                        close(STDOUT_FILENO);
                                        dup(fd_open);
                                        close(fd_open);
                                    }
                                } else {
                                    //dup2(proceses_pipes[i][1], STDOUT_FILENO);
                                    close(STDOUT_FILENO);
                                    dup(proceses_pipes[i][1]);
                                    close(proceses_pipes[i][1]);
                                    close(proceses_pipes[i][0]);
                                }

                                // handle error redirection if exists
                                if (filev[2][0] != '0')
                                {
                                    // open file
                                    int fd_open;
                                    if ((fd_open = open(filev[2], O_WRONLY | O_CREAT)) == -1 ){
                                        perror("Error opening file at redirection error");
                                        exit(EXIT_FAILURE);
                                    }

                                    // pipe handling
                                    close(STDERR_FILENO);
                                    dup(fd_open);
                                    close(fd_open);
                                }

                                execvp(argvv[i][0], argvv[i]);  //execute command

                                // in case of error (because the process image change and the next code will not be executed)
                                exit(-1);
                            default:
                                if (in_background == 0){
                                    waitpid(pid, &status, 0);
                                } else {
                                    printf("%d\n", pid);
                                }
                    }   }
                }  
                
            }
		}
	}	
	
	return 0;
}
