#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void Part1(long bot, long top)
{
    long valids = 0;

    for(int pass=bot; pass <= top; pass++)
    {
        bool fail = false;

        string password = to_string(pass);
        //check alphabetical order
        for(unsigned int i=0; i < password.size()-1; i++)
        {
            if (password[i] > password[i+1])
            {
                fail = true;
                break;
            }
        }
        if(fail) continue;

        //check for duplicates
        for(unsigned int i=0; i < password.size()-1; i++)
        {
            if (password[i] == password[i+1])
            {
                valids++;
                break;
            }
        }
    }

    cout << "Part 1:" << endl << "\t" << valids << endl << endl;
}

void Part2(long bot, long top)
{
    long valids = 0;

    for(int pass=bot; pass <= top; pass++)
    {
        bool fail = false;

        string password = to_string(pass);
        //check alphabetical order
        for(unsigned int i=0; i < password.size()-1; i++)
        {
            if (password[i] > password[i+1])
            {
                fail = true;
                break;
            }
        }
        if(fail) continue;

        //check for duplicates that aren't larger
        unsigned int i = 0;
        while( i < password.size()-1 )
        {
            if (password[i] == password[i+1])
            {
                //if duplicate is longer than twice, skip ahead
                if( i+2 < password.size() && password[i+2] == password[i] )
                {
                    i = password.find_first_not_of(password[i],i);
                }
                else
                {
                    valids++;
                    break;
                }
            }
            else
            {
                i++;
            }
        }
    }

    cout << "Part 2:" << endl << "\t" << valids << endl << endl;
}

int main(int argc, char *argv[])
{
    std::string filename = "input.txt";
    if(argc > 1)
        filename = argv[1];

    std::ifstream inputfile (filename);
    if (inputfile.is_open())
    {
        char minus;
        long bot, top;

        inputfile >> bot;
        inputfile >> minus;
        inputfile >> top;

        Part1(bot, top);
        Part2(bot, top);
        return 0;
    }
    else
    {
        cerr << "Unable to open file " << filename << endl;
        return 1;
    }
}
