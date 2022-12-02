#include <stdio.h>
#include <stdlib.h>

int
main(int argc, char **argv)
{
    FILE *data = fopen("input.txt", "r");

    int max[3] = {0};
    int kcal = 0;
    char line[10];

    while (fgets(line, 10, data))
    {
        if (line[0] == '\n' || line[0] == '\r')
        {
            if (kcal > max[0])
            {
                max[2] = max[1];
                max[1] = max[0];
                max[0] = kcal;
            }
            else if (kcal > max[1])
            {
                max[2] = max[1];
                max[1] = kcal;
            }
            else if (kcal > max[2])
                max[2] = kcal;

            kcal = 0;
        }
        else
            kcal += atoi(line);
    }

    printf("%d\n", max[0]);
    printf("%d\n", max[0] + max[1] + max[2]);

    return 0;
}
