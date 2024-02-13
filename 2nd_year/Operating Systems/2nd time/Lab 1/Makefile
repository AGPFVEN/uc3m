CC=gcc

CFLAGS=-Wall -Werror


%.o: %.c 
	$(CC) -c -o $@ $< $(CFLAGS)


all: wc ls ishere

	
wc:	mywc.o
	$(CC) $(CFLAGS) -o mywc  mywc.o 

ls: myls.o
	$(CC) $(CFLAGS)  -o myls myls.o

ishere:	myishere.o
	$(CC) $(CFLAGS)  -o myishere  myishere.o


clean:
	rm -f mywc myishere myls
	rm *.o
