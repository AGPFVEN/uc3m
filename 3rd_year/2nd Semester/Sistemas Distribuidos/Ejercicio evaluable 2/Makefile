
CC=gcc
CFLAGS=-g -Wall
LDFLAGS=


all :: app-d lib-server

app-d: app-d.o  lib-client.o  claves.o
	$(CC) $(CFLAGS) $(LDFLAGS) app-d.o claves.o lib-client.o -o $@  $(LDFLAGS)

lib-server: lib-client.o  lib-server.o  claves.o
	$(CC) $(CFLAGS) claves.o lib-client.o lib-server.o  -o $@  $(LDFLAGS)

mount:
	mkdir -p /dev/mqueue
	mount -t mqueue none /dev/mqueue

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o

