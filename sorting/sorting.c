#include "sorting.h"


int32_t main( int32_t argc, const char **argv )
{
    int32_t a[] = {4, 65, 2, -31, 0, 99, 2, 83, 782, 1};
    int32_t size = sizeof(a) / sizeof(a[0]);

    for ( int32_t i = 0; i < size; i++ )
        printf("%d%s", a[i], i == size - 1 ? "\n" : " ");
    // bubblesort( a, size );
    // selectionsort( a, size );
    // insertionsort( a, size );
    // quicksort( a, size );
    // mergesort( a, size );
    heapsort( a, size );
    for ( int32_t i = 0; i < size; i++ )
        printf("%d%s", a[i], i == size - 1 ? "\n" : " ");

    return 0;
}


void swap( int32_t *a, int32_t *b )
{
    int32_t tmp = *a;
    *a = *b;
    *b = tmp;
}


// merges two halves of a[] together, assuming each half is sorted
void merge ( int32_t *a, int32_t size, int32_t midpoint )
{
    int32_t i, j, k;
    // allocates zeroed memory. Has performance penalty for *huge* allocations
    int32_t *tmp = calloc( size, sizeof(int32_t) );
    if ( tmp == NULL )
        exit(1);

    for ( i = 0, j = midpoint, k = 0; k < size; k++ )
    {
        // tmp[k] = j == size ? a[i++]
        //        : i == midpoint ? a[j++]
        //        : a[j] < a[i] ? a[j++]
        //        : a[i++];
        if ( j == size )
            tmp[k] = a[i++];
        else if ( i == midpoint )
            tmp[k] = a[j++];
        else if ( a[j] < a[i] )
            tmp[k] = a[j++];
        else
            tmp[k] = a[i++];
    }

    for ( i = 0; i < size; i++ )
    {
        a[i] = tmp[i];
    }

    free(tmp);
}


void heapify( int32_t *a, int32_t size, int32_t root )
{
    int32_t largest = root;
    int32_t left = 2 * root + 1;
    int32_t right = 2 * root + 2;

    if ( left < size && a[left] > a[largest] )
        largest = left;
    if ( right < size && a[right] > a[largest] )
        largest = right;
    if ( largest != root )
    {
        swap( &a[root], &a[largest] );
        heapify( a, size, largest );
    }
}


void bubblesort( int32_t *a, size_t size )
{
    int32_t s = 1;

    while ( s )
    {
        s = 0;
        for ( int32_t i = 1; i < size; i++ )
        {
            if ( a[i] < a[i - 1])
            {
                swap( &a[i], &a[i - 1] );
                s = 1;
            }
        }
    }
}


void selectionsort( int32_t *a, size_t size )
{
    int32_t i, j, m;
    for ( i = 0; i < size; i++ )
    {
        for ( j = i, m = i; j < size; j++ )
        {
            if ( a[j] < a[m] )
            {
                m = j;
            }
        }
        swap( &a[i], &a[m] );
    }
}


void insertionsort( int32_t *a, size_t size )
{
    for ( int32_t i = 1; i < size; i++ )
    {
        int32_t key = a[i];
        int32_t j = i;

        while ( j > 0 && key < a[j - 1] )
        {
            a[j] = a[j - 1];
            --j;
        }
        a[j] = key;
    }
}


void quicksort( int32_t *a, size_t size )
{
    int32_t i, j;

    if ( size < 2 )
        return;

    int32_t pivot = a[size / 2];

    for ( i = 0, j = size - 1; ; i++, j-- )
    {
        while ( a[i] < pivot )
            i++;
        while ( pivot < a[j] )
            j--;
        if ( i >= j )
            break;

        swap( &a[i], &a[j] );
    }

    quicksort( a, i );
    quicksort( a+i, size-i );
}


void mergesort( int32_t *a, size_t size )
{
    if ( size < 2 )
        return;

    int32_t midpoint = size / 2;

    // sort left half
    mergesort( a, midpoint );
    // sort right half
    mergesort( a + midpoint, size - midpoint );
    // merge two sorted halves together
    merge( a, size, midpoint );
}


void heapsort( int32_t *a, size_t size )
{
    for ( int32_t root = size / 2 - 1; root >= 0; root-- )
        heapify( a, size, root );

    for ( int32_t root = size - 1; root >= 0; root-- )
    {
        swap( &a[0], &a[root] );
        heapify( a, root, 0 );
    }
}
