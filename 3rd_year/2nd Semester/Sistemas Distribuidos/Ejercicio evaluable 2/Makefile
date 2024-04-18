
CC=gcc
CFLAGS=-g -Wall
LDFLAGS=-lpthread


all :: cliente cliente1 servidor

cliente: cliente.o  libclaves.so  operaciones.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@  $(LDFLAGS)

cliente1: cliente1.o  libclaves.so  operaciones.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@  $(LDFLAGS)

servidor: libclaves.so  servidor.o  operaciones.o
	$(CC) $(CFLAGS) $^ -o $@  $(LDFLAGS)

libclaves.so: claves.c
	$(CC) $(CFLAGS) -shared -o $@ -fpic $^
	export LD_LIBRARY_PATH=./$LD_LIBRARY_PATH

mount:
	mkdir -p /dev/mqueue
	mount -t mqueue none /dev/mqueue

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

