BIN_FILES = clave_test

CC = gcc

CPPFLAGS = -I$(INSTALL_PATH)/include -Wall

LDFLAGS = -L$(INSTALL_PATH)/lib/
#LDLIBS = -lpthread -lm


all: $(BIN_FILES)
.PHONY : all

clave_test: *.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^  -o $@

claves: claves.o
	$(CC) $(CFLAGS) $(LDFLAGS) $^  -o $@

%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $<

clean:
	rm -f $(BIN_FILES) *.o

.SUFFIXES:
.PHONY : clean