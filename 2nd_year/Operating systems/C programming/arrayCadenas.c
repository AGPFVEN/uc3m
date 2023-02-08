#include<stdio.h>

int main(int argc, char **argv){
	char *p;
	char ex[] = "This is a test";
	int count;

	count = 0;

	for(p=ex; p++; p[0]==0){
		printf("%s corresponds to: %d\n", p, p[0]);

		if (p[0] == 32){
			count++;
			printf("counter is hit with %d ocurrences", count);
		}
	}	

	printf("%d\n", count);

	return 0;
}


