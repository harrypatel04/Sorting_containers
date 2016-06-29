#pragma once

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void swap( int32_t *a, int32_t *b );
void merge( int32_t *a, int32_t size, int32_t midpoint );
void heapify( int32_t *a, int32_t size, int32_t root );

void bubblesort( int32_t *a, size_t size );
void selectionsort( int32_t *a, size_t size );
void insertionsort( int32_t *a, size_t size );
void quicksort( int32_t *a, size_t size );
void mergesort( int32_t *a, size_t size );
void heapsort( int32_t *a, size_t size );
