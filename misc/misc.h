#pragma once  // eliminates need for header guards. Supported by nearly all compilers
// Recommended reading: https://matt.sh/howto-c

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <inttypes.h>
#include <getopt.h>
#include <math.h>


bool strcmp_( char *s1, char *s2 );
int32_t atoi_( char *a );
void strcpy_( char *dest, char *src );
void strncpy_( char *dest, char *src, int32_t num_bytes );
int32_t strlen_( char *str );

void print_bits( size_t const size, void const * const ptr );
void reverse_bits( int32_t *n );

void parse_args( int32_t argc, const char **argv, uint32_t *size, int32_t *offset );
void prime_sieve( size_t size, bool nums[] );
