#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int ch = atoi(getenv("PORT_TUPLAS"));
    printf("%i\n", ch);
}