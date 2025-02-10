
#include "inputProcessing.h"
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
        // Пропускаем пустые строки
        if (line.empty() || line.find_first_not_of(" \t\r\n") == std::string::npos)
            continue;

        std::istringstream iss(line);
        int first, second;

        if (!(iss >> first >> second))
        {
            f.close();
            throw std::runtime_error("Invalid format: each line should contain two integers!");
        }

        // Проверяем, что в строке больше нет чисел
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