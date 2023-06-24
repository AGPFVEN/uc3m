#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#define TEST_STRING1 "test string 1"
#define TEST_STRING2 "test string 2"

/*
    This exercise is in order to check what happens if
    we use lseek further than possible
    see result with cat test.txt
*/
int main(int argc, char* argv){
    int fd;

    //Open file
    if((fd = creat("test.txt", O_RDWR | 0664)) < 0){
        printf("Error at creating the file\n");
        return (-1);
    }

    //Write on file
    if (write(fd, TEST_STRING1, sizeof(TEST_STRING1)) < 0){
        printf("Error at writting on the file\n");
        return (-3);
    }

    //Jump 100 spaces
    if (lseek(fd, 100, 0) < 0){
        printf("Error at moving the file descriptor\n");
        return (-2);
    }

    //Write again in the file
    if (write(fd, TEST_STRING2, sizeof(TEST_STRING2)) < 0){
        printf("Error at writting on the file\n");
        return (-3);
    }

    return 0;
}