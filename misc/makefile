#find any .c file in src/
#SRC = $(wildcard src/*.c)
SRC = misc.c
#make an object file for every .c file
OBJ = $(SRC:.c=.o)

CC = gcc
LINK = gcc

#-Werror turns warnings into errors
CFLAGS = -O2 -Wall -Wpedantic -Wextra -std=c11

CXXFLAGS = $(CFLAGS)

TARGET = main

all: $(TARGET)

$(TARGET): $(OBJ)
	$(LINK) -o $@ $^ $(CFLAGS)
	rm -rf $(OBJ)

.c:
	$(CC) -o $@ $@.c

clean:
	rm -rf $(TARGET) *.o
