#include <iostream>
#include <fstream>
#include <string>
#include <vector>

long getModeVal(std::vector<long> const &comp, int pos, int mode)
{
    if(mode == 1)
        return pos;
    else
        return size_t(pos) < comp.size() ? comp[pos] : 0;
}

std::vector<long> compute(std::vector<long> &comp, long input = 0)
{
    std::vector<long> output;
    unsigned long i = 0;
    while ( i<comp.size() )
    {
        int opcode = comp[i] % 100;
        // 0 = address mode; 1 = immediate mode
        int mode1  = comp[i]/100   % 10;
        int mode2  = comp[i]/1000  % 10;
        int mode3  = comp[i]/10000 % 10;
        // what the parameters are based on the mode
        long p1    = i+1 < comp.size() ? getModeVal(comp, comp[i+1], mode1) : 0;
        long p2    = i+2 < comp.size() ? getModeVal(comp, comp[i+2], mode2) : 0;
        long p3    = i+3 < comp.size() ? getModeVal(comp, comp[i+3], mode3) : 0;
        // these are always address mode parameters
        long p1_s  = i+1 < comp.size() ? comp[i+1] : 0;
        long p2_s  = i+2 < comp.size() ? comp[i+2] : 0;
        long p3_s  = i+3 < comp.size() ? comp[i+3] : 0;
        switch( opcode )
        {
        case 1: // Addition: *p3 <- p1 + p2
            comp[ p3_s ] = p1 + p2;
            i += 4;
            break;
        case 2: // Multiplication: *p3 <- p1 * p2
            comp[ p3_s ] = p1 * p2;
            i += 4;
            break;
        case 3: // Store: *p1 <- input
            comp[ p1_s ] = input;
            i += 2;
            break;
        case 4: // Output: output p1
            output.push_back( p1 );
            i += 2;
            break;
        case 5: // Jump to p2 if p1 != 0
            i = p1 != 0 ? p2 : i+3;
            break;
        case 6: // Jump to p2 if p1 == 0
            i = p1 == 0 ? p2 : i+3;
            break;
        case 7: // Less-than: *p3 <- p1 < p2
            comp[ p3_s ] = p1 < p2;
            i += 4;
            break;
        case 8: // Equality: *p3 <- p1 == p2
            comp[ p3_s ] = p1 == p2;
            i += 4;
            break;
        case 99:  // Halt Program
            return output;
        }
    }
    return output;
}

void Part1(std::vector<long> input)
{
    std::vector<long> out = compute(input,1);

     std::cout << "Part 1:" << std::endl << "\t";
     std::cout << out.back() << std::endl << std::endl;
}

void Part2(std::vector<long> input)
{
    std::vector<long> out = compute(input,5);

     std::cout << "Part 2:" << std::endl << "\t";
     std::cout << out.back() << std::endl << std::endl;
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
