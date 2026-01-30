int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int size, i, ch;
    char *s = (char *)malloc(1000 * sizeof(char));

    scanf("%s", s);
    size = strlen(s);
    s = (char *)realloc(s, size + 1);
    
    int nums[10] = {0};
    for (i = 0;i <= size;i++) {
        ch = *(s + i);
        switch (ch) {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            nums[ch - 48] += 1;
        }
    }
    
    i = 0;
    while (i < 10)
        printf("%d ", nums[i++]);

    free(s);
    return 0;
}