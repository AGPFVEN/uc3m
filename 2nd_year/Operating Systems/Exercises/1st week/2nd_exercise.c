#include<stdio.h>

int main(int argc, char *argv[]){
	char user_name[100]; //In the proposed solution the professor uses 32 characters instead of 100
	printf("Enter your name:\n");
	fgets(user_name, 100, stdin); /* In the proposed solution the professor uses scanf
	scanf("%s", user_name);	      <- like this*/

	printf("Hello %s", user_name);
}
