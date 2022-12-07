#ifndef AOC_2022_07_STACK_H_
#define AOC_2022_07_STACK_H_

#include "./tree.h"

struct stack_node
{
    struct node *stack;
    struct stack_node *next;
};

#endif
