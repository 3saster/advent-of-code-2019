#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<long> cycle(vector<long> digits)
{
    auto dSize = digits.size();
    vector<long> output;
    output.resize(dSize);
    for(unsigned long i = 1; i <= dSize; i++)
    {
        long sum = 0;
        for(unsigned long j = i-1; j < 2*i-1; j++)
        {
            for(unsigned long k = j; k < dSize; k += 4*i)
                sum += digits[k];
            for(unsigned long k = j + 2*i; k < dSize; k += 4*i)
                sum -= digits[k];
        }
        sum = abs(sum)%10;
        output[i-1] = sum;
    }
    return output;
}

void Part1( vector<long> input )
{
    vector<long> output( input );
    for(int i = 0; i < 100; i++)
        output = cycle(output);

    cout << "Part 1:\n\t";
    for(int i=0; i < 8; i++)
        cout << output[i];
    cout << endl << endl;
}

void Part2( vector<long> input )
{
    vector<long> output;
    for(int i = 0; i < 10000; i++)
        output.insert(output.end(), input.begin(), input.end());

    long offset = 1000000*output[0] + 100000*output[1] + 10000*output[2] + 1000*output[3] + 100*output[4] + 10*output[5] + 1*output[6];
    for(int i = 0; i < 100; i++)
    {
        long sum = 0;
        for(long k = output.size()-1; k >= offset; k--)
        {
            sum += output[k];
            sum %= 10;
            output[k] = sum;
        }
    }

    cout << "Part 2:\n\t";
    for(int i=0; i < 8; i++)
        cout << output[offset+i];
    cout << endl << endl;
}

int main(int argc, char *argv[])
{
    std::string filename = "input.txt";
    if(argc > 1)
        filename = argv[1];

    ifstream inputfile (filename);
    if (inputfile.is_open())
    {
        char value;
        vector<long> input;
        while( inputfile >> value )
        {
            input.push_back(long(value - '0'));
        }

        Part1(input);
        Part2(input);
        return 0;
    }
    return 0;
}
