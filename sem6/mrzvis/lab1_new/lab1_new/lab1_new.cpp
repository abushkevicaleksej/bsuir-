#include <iostream>
#include <vector>
#include <bitset>
#include <queue>
#include <string>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <fstream>

const int BIT_WIDTH = 6;


std::string toBinary(int num) {
    std::bitset<BIT_WIDTH> bits(num);
    std::string binStr = bits.to_string();
    return binStr.substr(0, 2) + " " + binStr.substr(2, 4);
}

std::pair<std::vector<int>, std::vector<int>> inputProcessing(const std::string& input_file)
{
    std::ifstream f(input_file);
    std::pair<std::vector<int>, std::vector<int>> output;

    if (!f.is_open())
    {
        throw std::runtime_error("Error while opening file!");
        return output;
    }

    std::string line;
    while (std::getline(f, line))
    {
        if (line.empty() || line.find_first_not_of(" \t\r\n") == std::string::npos)
            continue;

        std::istringstream iss(line);
        int first, second;

        if (!(iss >> first >> second))
        {
            f.close();
            throw std::runtime_error("Invalid format: each line should contain two integers!");
        }

        std::string remaining;
        if (iss >> remaining)
        {
            f.close();
            throw std::runtime_error("Too many numbers in line!");
        }

        output.first.push_back(first);
        output.second.push_back(second);
    }

    f.close();
    return output;
}

void pipelineCalculating(const std::vector<int>& A, const std::vector<int>& B) {
    for (size_t i = 0; i < A.size() && i < B.size(); ++i) {
        std::string multiplicand = toBinary(A[i]);
        std::string factor = toBinary(B[i]);

        multiplicand.erase(remove_if(multiplicand.begin(), multiplicand.end(), isspace), multiplicand.end());
        factor.erase(remove_if(factor.begin(), factor.end(), isspace), factor.end());

        int finalProduct = 0;
        std::vector<std::string> partialProducts(BIT_WIDTH, std::string(BIT_WIDTH * 2, '0'));

        std::cout << "Processing Pair: (" << A[i] << ", " << B[i] << ")\n";
        std::cout << "Multiplier:   " << factor << "\n";
        std::cout << "Multiplicand: " << multiplicand << "\n";
        

        for (int stage = 0; stage < BIT_WIDTH; ++stage) {
            if (multiplicand[BIT_WIDTH - 1 - stage] == '1') {
                int partialValue = (std::stoi(factor, nullptr, 2) << stage);
                partialProducts[stage] = std::bitset<BIT_WIDTH * 2>(partialValue).to_string();
                finalProduct += partialValue;
            }

            std::cout << "Stage " << stage + 1 << " Partial Product: " << partialProducts[stage] << "\n";
        }

        std::cout << "Final Product: " << std::bitset<BIT_WIDTH * 2>(finalProduct) << " (" << finalProduct << ")\n";
        std::cout << "------------------------------------\n";
    }
}


int main()
{
    const auto& input = inputProcessing("input.txt");
    pipelineCalculating(input.first, input.second);
	return 0;
}