// misc implementations
#include "misc.h"

int32_t main()
{
    bool *nums;
    size_t size = 1000;
    nums = calloc(size, sizeof(bool));
    // usage: bool is_prime(n){return nums[n]};

    prime_sieve(size, nums);
    for ( uint32_t i = 0; i < size; i++ )
    {
        if ( nums[i] )
            printf("%d is prime\n", i);
    }

    return 0;
}


// Differs from STL implementation in that it returns a bool rather than int
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


int32_t strlen_( char *str )
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


// http://www.gnu.org/software/libc/manual/html_node/Parsing-Program-Arguments.html
void parse_args( int32_t argc, const char **argv, uint32_t *size, int32_t *offset )
{
    char ch;

    // --size 4 == -s4 == -s 4 == --size=4
    static struct option long_options[] =
    {
        {"size", required_argument, NULL, 's'},
        {"offset", required_argument, NULL, 'o'},
        {NULL, 0, NULL, 0}
    };

    while ( (ch = getopt_long(argc, (char * const *)argv, "s:o:", long_options, NULL)) != -1 )
    {
        switch ( ch )
        {
        case 's':
            *size = abs(atoi(optarg));  // size is supposed to be unsigned
            break;
        case 'o':
            *offset = atoi(optarg);
            break;
        case '?':
            break; // message already printed
        default:
            exit(1);
        }

    }
}


// Sieve of Atkin: https://en.wikipedia.org/wiki/Sieve_of_Atkin
void prime_sieve( size_t size, bool nums[] )
{
    uint32_t n;

    // Initialize array with false values
    for ( uint32_t i = 0; i < size; i++ )
        nums[i] = false;

    // mark nums[n] true if any of the following is true:
    // a) n = 4*x^2 + y^2 has an odd number of solution pairs AND n % 12 = 1 or n % 12 = 5
    // b) n = 3*x^2 + y^2 has an odd number of solutions pairs AND n % 12 = 7
    // c) n = 3*x^2 - y^2 has an odd number of solutions pairs AND x > y AND n % 12 = 11
    for ( uint32_t x = 1; x*x < size; x++ )
    {
        for ( uint32_t y = 1; y*y < size; y++ )
        {
            n = (4 * x * x) + (y * y);
            if (n <= size && (n % 12 == 1 || n % 12 == 5))
                nums[n] ^= true;

            n = (3 * x * x) + (y * y);
            if (n <= size && n % 12 == 7)
                nums[n] ^= true;

            n = (3 * x * x) - (y * y);
            if (x > y && n <= size && n % 12 == 11)
                nums[n] ^= true;
        }
    }

    for ( uint32_t i = 5; i < sqrt(size); i++)
    {
        if ( nums[i] )
        {
            for ( uint32_t j = i*i; j < size; j += i*i )
            {
                nums[i] = false;
            }
        }
    }

    // The above ignores single digit primes
    uint32_t first[4] = {2, 3, 5, 7};
    for ( uint32_t i = 0; i < size && i < 4; i++ )
        nums[first[i]] = true;
}
