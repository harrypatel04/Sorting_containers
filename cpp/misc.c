// misc implementations
#include "misc.h"

int32_t main(int32_t argc, char const **argv)
{
    char *hex1 = "0x32";  // 50
    char *hex2 = "0X32";
    char *hex3 = "0x0A";  // 10
    char *hex4 = "0x0a";

    char *bin1 = "0b10";  // 2
    char *bin2 = "0B10";
    char *bin3 = "0b001";  // 1

    char *int1 = "10";
    char *int2 = "01";
    char *int3 = "99";

    char *shex1 = "-0x32";
    char *sbin1 = "-0b10";
    char *sint1 = "-10";

    // printf("%s: %d\n", hex1, atoi_(hex1));
    // printf("%s: %d\n", hex2, atoi_(hex2));
    // printf("%s: %d\n", hex3, atoi_(hex3));
    // printf("%s: %d\n\n", hex4, atoi_(hex4));

    // printf("%s: %d\n", bin1, atoi_(bin1));
    // printf("%s: %d\n", bin2, atoi_(bin2));
    // printf("%s: %d\n\n", bin3, atoi_(bin3));

    // printf("%s: %d\n", int1, atoi_(int1));
    // printf("%s: %d\n", int2, atoi_(int2));
    // printf("%s: %d\n\n", int3, atoi_(int3));

    // printf("%s: %d\n", shex1, atoi_(shex1));
    // printf("%s: %d\n", sbin1, atoi_(sbin1));
    // printf("%s: %d\n", sint1, atoi_(sint1));

    int32_t n = 76812;
    int32_t m = -76812;

    print_bits( sizeof(n), &n );
    print_bits( sizeof(m), &m );
    reverse_bits( &n );
    reverse_bits( &m );
    print_bits( sizeof(n), &n );
    print_bits( sizeof(m), &m );

    return 0;
}


bool strcmp_( char *s1, char *s2 )
{
    while ( *s1 == *s2 )
    {
        if ( !*s1 )  // we've made it to the end of the null-terminated string
            return true;

        ++s1;
        ++s2;
    }

    return false;
}


// Handle signed decimal, hexadecimal, or binary values
// "-54" "12" "0x43216fd" "-0X4AbcD" "0b1001101" "0B1011"
// TODO: how to handle errors?
int32_t atoi_( char *str )
{
    int32_t sign = 1;
    int32_t value = 0;
    char c;

    if ( *str == '-' )
    {
        sign = -1;
        str++;
    }

    // hexadecimal
    if ( str[0] == '0' && (str[1] == 'x' || str[1] == 'X') )
    {
        str += 2;  // ignore the '0x'
        while ( 1 )
        {
            c = *str;
            str++;
            if ( c >= '0' && c <= '9' )
                value = value * 16 + c - '0';
            else if ( c >= 'a' && c <= 'f' )
                value = value * 16 + c - 'a' + 10;
            else if ( c >= 'A' && c <= 'F')
                value = value * 16 + c - 'A' + 10;
            else
                return value * sign;
        }
    }
    // binary
    else if ( str[0] == '0' && (str[1] == 'b' || str[1] == 'B') )
    {
        str += 2;  // ignore the '0b'
        while ( 1 )
        {
            c = *str;
            str++;
            if ( c >= '0' && c <= '1' )
                value = value * 2 + c - '0';
            else
                return value * sign;
        }
    }
    // decimal
    else
    {
        while ( 1 )
        {
            c = *str;
            str++;
            if ( c < '0' || c > '9')  // if the char is not a digit
                return sign * value;
            value = value * 10 + c - '0';  // '0' has int value of 48
        }
    }
}


void strcpy_( char *dest, char *src )
{
    while ( *src )  // assumes *src is null-terminated
    {
        *dest++ = *src++;  // assignment happens before increment
    }
    *dest = '\0';
}


// assumes pointers don't overlap
void strncpy_( char *dest, char *src, int32_t num_bytes )
{
    if ( num_bytes < 0 )
        return;

    while ( *src && num_bytes )
    {
        *dest++ = *src++;
        --num_bytes;
    }

    // fill in the rest with null characters
    while ( num_bytes )
    {
        *dest++ = '\0';
        --num_bytes;
    }
}


int32_t _strlen( char *str )
{
    int32_t count = 0;

    while ( str[count] )  // could also *str++
        ++count;

    return count;
}


// assumes little endian, prints the binary representation of
// the value at `ptr` with arbitrary `size`.
void print_bits( size_t const size, void const * const ptr )
{
    uint8_t *b = (uint8_t*) ptr;
    uint8_t byte;
    int32_t i, j;

    for ( i = size - 1; i >= 0; i-- )
    {
        for ( j = 7; j >= 0; j-- )
        {
            byte = b[i] & (1 << j);
            byte >>= j;
            printf("%u", byte);
        }
    }
    printf("\n");
}


// reverses a 32 bit word in place
void reverse_bits( int32_t *n )
{
    *n = ((*n >> 1) & 0x55555555) | ((*n << 1) & 0xaaaaaaaa);
    *n = ((*n >> 2) & 0x33333333) | ((*n << 2) & 0xcccccccc);
    *n = ((*n >> 4) & 0x0f0f0f0f) | ((*n << 4) & 0xf0f0f0f0);
    *n = ((*n >> 8) & 0x00ff00ff) | ((*n << 8) & 0xff00ff00);
    *n = ((*n >> 16) & 0x0000ffff) | ((*n << 16) & 0xffff0000);
}
