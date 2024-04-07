
CC=gcc
CFLAGS=-g -Wall
LDFLAGS=lpthread


all :: cliente servidor

cliente: cliente.o  claves.o  operaciones.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@  $(LDFLAGS)

servidor: claves.o  servidor.o  operaciones.o
	$(CC) $(CFLAGS) $^ -o $@  $(LDFLAGS)

mount:
	mkdir -p /dev/mqueue
	mount -t mqueue none /dev/mqueue

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

