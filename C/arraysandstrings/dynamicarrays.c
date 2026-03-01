#include <stdio.h>
#include <stdlib.h>

int* total_number_of_books;
int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    
    total_number_of_books = calloc(total_number_of_shelves, sizeof(int));
    total_number_of_pages = malloc(total_number_of_shelves * sizeof(int*));
    int* capacity = calloc(total_number_of_shelves, sizeof(int));
    for(int i = 0; i < total_number_of_shelves; i++)
    {
        *(capacity + i) = 10;
        *(total_number_of_pages + i) = calloc(*(capacity + i), sizeof(int));
    }
    
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        
        if (type_of_query == 1) {
            int x, y;
            scanf("%d %d", &x, &y);
            int* pages = *(total_number_of_pages + x);
            int* books = total_number_of_books + x;
            if(*(capacity + x) <= *books)
            {
                *(capacity + x) *=2;
                pages = realloc(pages, (*(capacity + x)) * sizeof(int));
            }
            
            *(pages + *books) = y;
            *(total_number_of_pages + x) = pages;
            (*books)++;

        } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        free(total_number_of_books);
    }
    
    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            free(*(total_number_of_pages + i));
        }
    }
    
    if (total_number_of_pages) {
        free(total_number_of_pages);
    }
    
    return 0;
}