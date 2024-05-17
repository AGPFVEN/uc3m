#include <stddef.h> /* NULL */
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

// execute the program with args: cat t.txt
// to see the perfect demonstation

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define NUM_CHILDREN 4

/* Entry point for the child processes */
int child_main(int pipe_read_end) {
  pid_t my_pid = getpid();

  /* Read child pids from pipe */
  int child_pids[NUM_CHILDREN];
  unsigned int bytes_read = 0;
  while (bytes_read < sizeof(child_pids)) {
    ssize_t result = read(pipe_read_end, ((unsigned char *) child_pids) + bytes_read, sizeof(child_pids) - bytes_read);
    if (result < 0) {
      perror("error reading from pipe");
      return 1;
    } else if (result == 0) {
      fprintf(stderr, "unexpected end of file\n");
      return 1;
    } else {
      bytes_read += result;
    }
  }
  close(pipe_read_end);

  /* Do something useful with these child pids */
  for (int i = 0; i < NUM_CHILDREN; i++) {
    printf("Child %d received sibling pid %d\n", my_pid, child_pids[i]);
  }

  return 0;
}

/* Entry point for the parent process. */
int main() {
  int child_pids[NUM_CHILDREN];
  int pipe_write_ends[NUM_CHILDREN];
  for (int i = 0; i < NUM_CHILDREN; i++) {
    /* Create the pipe for child i */
    int pipefd[2];
    if (pipe(pipefd)) {
      perror("error creating pipe");
      return 1;
    }
    int pipe_read_end = pipefd[0];
    int pipe_write_end = pipefd[1];

    /* Fork child i */
    pid_t child_pid = fork();
    if (child_pid < 0) {
      perror("error forking");
      return 1;
    } else if (child_pid == 0) {
      printf("Child %d was forked\n", getpid());
      close(pipe_write_end);
      return child_main(pipe_read_end);
    } else {
      printf("Parent forked child %d\n", child_pid);
      close(pipe_read_end);
      pipe_write_ends[i] = pipe_write_end;
      child_pids[i] = child_pid;
    }
  }

  /* Send pids down the pipes for each child */
  for (int i = 0; i < NUM_CHILDREN; i++) {
    unsigned int bytes_written = 0;
    while (bytes_written < sizeof(child_pids)) {
      ssize_t result = write(pipe_write_ends[i], ((unsigned char *) child_pids) + bytes_written, sizeof(child_pids) - bytes_written);
      if (result < 0) {
        perror("error writing to pipe");
        return 1;
      } else {
        bytes_written += result;
      }
    }
    close(pipe_write_ends[i]);
  }

  /* Wait for children to exit */
  for (int i = 0; i < NUM_CHILDREN; i++) {
    if (waitpid(child_pids[i], 0, 0) < 0) {
      perror("error waiting for child");
      return 1;
    }
  }
  }

// int size, fd;
// if ((fd = open("1.txt", O_RDONLY)) == -1){
// perror("Error opening file in stardard input");
//}

// size = lseek(fd, 0L, SEEK_END);

// printf("%i\n", size);

// int pid;

// pid = fork();

// switch (pid)
//{
// case 0: //son
////File size
// struct stat st;
// stat(argv[1], &st);

// char *p;
// p = (char *) malloc(st.st_size);
// int fd;
// fd = open(argv[1], O_RDONLY);
// read(fd, p, st.st_size);
// close(fd);
// printf("%s\n", p);
// printf("%i soy hijo", pid);
// break;

// default:
// wait(0);
//}