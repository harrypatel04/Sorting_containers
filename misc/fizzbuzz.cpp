#include <iostream>
#include <string>


std::string fizz_buzzify( int n )
{
    bool fizz = n % 3 == 0;
    bool buzz = n % 5 == 0;
    std::string val = "";

    if ( fizz )
        val += "Fizz";
    if ( buzz )
        val += "Buzz";
    if ( !fizz && !buzz )
        val = std::to_string(n);

    return val;
}


int main(int argc, char const *argv[])
{
    for ( int i = 0; i <= 100; i++ )
    {
        std::cout << fizz_buzzify(i) << std::endl;
    }
    return 0;
}
