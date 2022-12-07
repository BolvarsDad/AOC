/*
 * Author: Sinan Pasic (@BolvarsDad)
 * Advet of Code 2022: Day 7 - No Space Left on Device.
 * General purpose code from bradenlib: https://gitlab.com/bradenbest/bradenlib/
 */

#include <stdio.h>
#include <stdlib.h>

#include "./tree.h"
#include "/home/bolvarsdad/Code/C/bradenlib/headers/for_each_line.h"
#include "/home/bolvarsdad/Code/C/bradenlib/headers/get_line.h"

void
stack_push(int stack[], struct node *current)
{

    stack[-1] = current;
}

void
stack_pop(int stack[], struct node *current)
{
    stack[-1] = current;

    free(current);
}

int
main(int argc, char **argv)
{
    int stack[1024] = {NULL};
    size_t stacklen = 0;

    return 0;
}
