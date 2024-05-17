#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

#define BUFF_SIZE 512

int copyFile(char* copyfrom, char* copyto)
{
      int fd, fd1, ret;
      char buff[BUFF_SIZE];

      if ((fd = open(copyfrom, O_RDONLY)) == -1){
            printf("Error at opening file to read from\n");
            exit(-1);
      }

      if ((fd1 = open(copyto, O_WRONLY)) == -1){
            printf("Error at opening file to write from\n");
            close(fd);
            exit(-1);
      }

      while ((ret = read(fd, &buff, BUFF_SIZE)) > 0){
            if (write(fd1, &buff, ret) == -1){
                  close(fd);
                  close(fd1);
                  printf("Error at writing the file\n");
                  exit(-1);
            }
      }
      if (ret < 0){
            close(fd);
            close(fd1);
            printf("Error at reading file to read from\n");
            exit(-1);
      }

      close(fd);
      close(fd1);
}

int main(int argc, char* argv[])
{
      copyFile("1.txt", "2.txt"); 
}