//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// 
// Файл предназначен для запуска программы
// 
// 
// Дата создания: 01.02.2025
//
#include "inputProcessing.h"
#include "calculation.h"
//сколько бит столько и этапов
int main() 
{
    try
    {
        setlocale(LC_ALL, "Russian");
        const auto& input = inputProcessing("input.txt");
        pipelineMultiplication(input.first, input.second);
        return 0;
    }
    catch (const std::string& err_message)
    {
        std::cout << err_message << std::endl;
    }
}
