#include <iostream>
#include <fstream>
#include <string>
#include <vector>

long getFuel(long mass)
{
    return int(mass/3)-2;
}

void Part1(std::vector<long> input)
{
    long totalMass = 0;
    for( auto v : input)
    {
        totalMass += getFuel(v);
    }
    std::cout << "Part 1:" << std::endl << "\t" << totalMass << std::endl << std::endl;
}

void Part2(std::vector<long> input)
{
    long totalMass = 0;
    for( auto v : input)
    {
        long fuel = getFuel(v);
        while(fuel > 0)
        {
            totalMass += fuel;
            fuel = getFuel(fuel);
        }
    }
    std::cout << "Part 2:" << std::endl << "\t" << totalMass << std::endl << std::endl;
}

int main(int argc, char *argv[])
{
    std::string filename = "input.txt";
    if(argc > 1)
        filename = argv[1];

    std::ifstream inputfile (filename);
    if (inputfile.is_open())
    {
        long value;
        std::vector<long> input;
        while( inputfile >> value )
            input.push_back(value);

        Part1(input);
        Part2(input);
        return 0;
    }
    else
    {
        std::cerr << "Unable to open file " << filename << std::endl;
        return 1;
    }
}
