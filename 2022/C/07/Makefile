CC=gcc
CFLAGS=-g -Wall -Wextra
BINS=tree main

all: $(BINS)

%: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	$(RM) $(BINS)
