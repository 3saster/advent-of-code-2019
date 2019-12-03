#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

typedef std::pair<long,long> coord;

// Returns null if no intersection found
coord getIntersection(coord A1, coord A2, coord B1, coord B2)
{
    coord nullcoord(0,0);

    // If these corners are not straight, exit
    if(A1.first != A2.first && A1.second != A2.second) return nullcoord;
    if(B1.first != B2.first && B1.second != B2.second) return nullcoord;

    // If lines are parallel, exit
    if( A1.first  == A2.first   && B1.first  == B2.first)  return nullcoord;
    if( A1.second == A2.second  && B1.second == B2.second) return nullcoord;

    long x = A1.first  == A2.first  ? A1.first  : B1.first;
    long y = A1.second == A2.second ? A1.second : B1.second;

    // Check that x lies between
    if( x == A1.first )
    {
        if( !( B1.first <= x && x <= B2.first ) && !( B2.first <= x && x <= B1.first ) )
            return nullcoord;
    }
    else
    {
        if( !( A1.first <= x && x <= A2.first ) && !( A2.first <= x && x <= A1.first ) )
            return nullcoord;
    }

    // Check that y lies between
    if( y == A1.second )
    {
        if( !( B1.second <= y && y <= B2.second ) && !( B2.second <= y && y <= B1.second ) )
            return nullcoord;
    }
    else
    {
        if( !( A1.second <= y && y <= A2.second ) && !( A2.second <= y && y <= A1.second ) )
            return nullcoord;
    }

    return coord(x,y);
}

void Part1(std::vector<std::string> wire1, std::vector<std::string> wire2)
{
    std::vector<coord> corners1, corners2;
    long x = 0, y = 0;
    // push in starting coordinates
    corners1.push_back(coord(x,y));
    corners2.push_back(coord(x,y));

    // get wire1 corners
    for( auto str : wire1)
    {
        char dir = str[0];
        long dist = atoi(str.substr(1).c_str());
        if(dir == 'U')
            y += dist;
        if(dir == 'D')
            y -= dist;
        if(dir == 'R')
            x += dist;
        if(dir == 'L')
            x -= dist;
        corners1.push_back(coord(x,y));
    }

    // get wire2 corners
    x = 0, y = 0;
    for( auto str : wire2)
    {
        char dir = str[0];
        long dist = atoi(str.substr(1).c_str());
        if(dir == 'U')
            y += dist;
        if(dir == 'D')
            y -= dist;
        if(dir == 'R')
            x += dist;
        if(dir == 'L')
            x -= dist;
        corners2.push_back(coord(x,y));
    }

    std::vector<long> distances;
    for(unsigned int i1 = 0; i1 < corners1.size()-1; i1++)
    {
        for(unsigned int i2 = 0; i2 < corners2.size()-1; i2++)
        {
            auto inter = getIntersection( corners1[i1], corners1[i1+1], corners2[i2], corners2[i2+1] );
            if( inter != coord(0,0) )
            {
                distances.push_back(abs(inter.first) + abs(inter.second));
                //std::cout << inter.first << "," << inter.second << std::endl;
            }
        }
    }

    auto mindist = std::min_element(std::begin(distances), std::end(distances));
    if(!distances.empty())
    {
        std::cout << "Part 1:" << std::endl << "\t" << *mindist << std::endl << std::endl;
    }
}

void Part2(std::vector<std::string> wire1, std::vector<std::string> wire2)
{

}

int main(int argc, char *argv[])
{
    std::string filename = "input.txt";
    if(argc > 1)
        filename = argv[1];

    std::ifstream inputfile (filename);
    if (inputfile.is_open())
    {
        std::vector<std::string> input1;
        std::vector<std::string> input2;

        std::string str1;
        if (std::getline(inputfile, str1))
        {
            std::stringstream ss(str1);
            std::string value;
            while(std::getline(ss, value, ','))
                input1.push_back(value);
        }
        std::string str2;
        if (std::getline(inputfile, str2))
        {
            std::stringstream ss(str2);
            std::string value;
            while(std::getline(ss, value, ','))
                input2.push_back(value);
        }

        Part1(input1, input2);
        Part2(input1, input2);
        return 0;
    }
    else
    {
        std::cerr << "Unable to open file " << filename << std::endl;
        return 1;
    }
}
