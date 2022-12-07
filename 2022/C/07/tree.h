#ifndef AOC_2022_07_TREE_H_
#define AOC_2022_07_TREE_H_

#include <stdint.h>

/*
 * Files have a size, folders have children.
 * If a node has no children it's a file with a size.
 * If a node has children, it's a directory with no size.
 * Although folders don't have a size, you can find the total size of a directory:
 * sizeof *node + (node->size * sizeof *node)
 * 
 * A folder's size is its amount of children (up to a maximum of 16)
 * Name length was chosen arbitrarily, but also because it's a multiple of 8 (sizeof(void *))
 * Child amount of a node was also chosen arbitrarily based on what seemed to be enough.
 *
 * Traversal: O(n) time complexity
 * Search: 
 */
struct node
{
    size_t      size;
    size_t      len;
    char const  name[16];
    struct      node *children[16];
};

struct node *node_new();

#endif
