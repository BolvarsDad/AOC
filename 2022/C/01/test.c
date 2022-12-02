#include <stdio.h>
#include <stdlib.h>

int
main(int argc, char **argv)
{
    char const *s = "Hello world";
    char const *n = "12345";

    printf("%d\n", atoi(s));
    printf("%d\n", atoi(n));

    return 0;
}
