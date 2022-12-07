#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "./tree.h"

struct node *
node_new(size_t size, size_t len, char const *name)
{
    struct node *new = malloc(sizeof(struct node));

    if (new == NULL)
    {
        perror("Unable to allocate node.");
        return;
    }

    new->size   = size;
    new->len    = len;
    new->name   = strcpy(name);

    return new;
}
