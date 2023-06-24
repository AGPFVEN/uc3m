#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<unistd.h>
#include<dirent.h>

int main(int argc, char* argv){
    DIR *dir;
    struct dirent *ent;

    //Open directory
    if ((dir = opendir(argv[1])) < 0){
        printf("Error at openning the directory");
        return (-1);
    }

    //Read directory and print result
    while ((ent = readdir(dir)) > 0){
        printf("%s\n", ent->d_name);
    }

    //Close directory
    closedir(dir);

    return 0;
}