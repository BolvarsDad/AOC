// External header files used here are part of bradenlib, a header library for
// general purpose C code written by Braden Best. Link to his GitLab and library here:
// https://gitlab.com/bradenbest/bradenlib

#include <stdio.h>
#include <stdlib.h>

#include "/home/bolvarsdad/Code/C/bradenlib/headers/strntol.h"
#include "/home/bolvarsdad/Code/C/bradenlib/headers/for_each_line.h"

long totals[500];
size_t totals_len = 0;

// Descending order.
int
qsort_fn(const void *a, const void *b)
{
    return (*(long *)b - *(long *)a);
}

// Function that's used as for_each_line_fn, read the well-written documentaton
// inside of for_each_line.h and the test file tfor_each_line.c found in the library.
void
add_line(char const *line, size_t len)
{
    long value = strntol(line, len, 10);

    totals[totals_len] += value;
}

int
main(int argc, char **argv)
{
    char buffer[4096];
    FILE *file = fopen("input.txt", "r");

    while (for_each_line(buffer, 4096, file, add_line))
            ++totals_len;

    // bugfix
    ++totals_len;

    qsort(totals, totals_len, sizeof(long), qsort_fn);

    printf("Part one: %lu\n", totals[0]);
    printf("Part two: %lu\n", totals[0] + totals[1] + totals[2]);

    return 0;
}
