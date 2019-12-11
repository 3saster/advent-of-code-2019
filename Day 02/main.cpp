#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define P2_VAL 19690720

void compute(std::vector<long> &comp)
{
    unsigned long i = 0;
    while ( i<comp.size() )
    {
        switch( comp[i] )
        {
        case 1: // Addition: *p3 <- *p1 + *p2
            comp[ comp[i+3] ] = comp[ comp[i+1] ] + comp[ comp[i+2] ];
            i += 4;
            break;
        case 2: // Multiplication: *p3 <- *p1 * *p2
            comp[ comp[i+3] ] = comp[ comp[i+1] ] * comp[ comp[i+2] ];
            i += 4;
            break;
        case 99: // Halt Program
            return;
        }
    }
}

void Part1(std::vector<long> input)
{
    input[1] = 12;
    input[2] = 2;
    compute(input);
    std::cout << "Part 1:" << std::endl << "\t" << input[0] << std::endl << std::endl;
}

void Part2(std::vector<long> input)
{
    for(int noun = 0; noun <= 99; noun++)
    {
        for(int verb = 0; verb <= 99; verb++)
        {
            auto program = input;
            program[1] = noun;
            program[2] = verb;
            compute(program);
            if( program[0] == P2_VAL )
            {
                std::cout << "Part 2:" << std::endl
                          << "\tNoun = " << noun << std::endl
                          << "\tVerb = " << verb << std::endl << std::endl;
                return;
            }
        }
    }
    std::cout << "Part 2:" << std::endl << "\tNo corresponding noun and verb found" << std::endl << std::endl;
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
        char comma;
        std::vector<long> input;
        while( inputfile >> value )
        {
            input.push_back(value);
            inputfile >> comma;
        }

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
