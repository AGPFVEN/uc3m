BIN_FILES =  servidor

CC = gcc

CPPFLAGS = -I$(INSTALL_PATH)/include -Wall

LDFLAGS = -L$(INSTALL_PATH)/lib/
#LDLIBS = -lpthread -lm


all: $(BIN_FILES)
.PHONY : all

: .o lib-client.o claves.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^  -o $@

servidor: lib-client.o servidor.o claves.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^  -o $@

#claves-build.o: main.o claves.o \
	$(CC) $(CFLAGS) $(LDFLAGS) $^  -o $@

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $<

clean:
	rm *.o

.SUFFIXES:
.PHONY : clean