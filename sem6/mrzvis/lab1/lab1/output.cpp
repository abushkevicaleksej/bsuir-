//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// 
// Файл предназначен для реализации методов вывода стадий в интерфейс коммандной строки
// 
// 
// Дата создания: 01.02.2025
//

#include "output.h"

std::string toBinary(int num) {
    std::bitset<BIT_WIDTH> bits(num);
    std::string binStr = bits.to_string();
    return binStr.substr(0, 2) + " " + binStr.substr(2, 4);
}

void printPairs(const std::vector<std::pair<int, int>>& pairs, const std::string& label, size_t processedCount) {
    std::cout << label << ":\n";
    for (size_t i = 0; i < pairs.size(); i++) {
        std::cout << "Пара " << (i + 1 + processedCount) << ": " << pairs[i].first << " x " << pairs[i].second << std::endl;
    }
    std::cout << std::endl;
}

void printPipelineState(const std::queue<PipelineStage>& pipeline) {
    std::cout << "Текущее состояние конвейера:\n";
    std::queue<PipelineStage> pipelineCopy = pipeline;
    while (!pipelineCopy.empty()) {
        auto stage = pipelineCopy.front();
        pipelineCopy.pop();
        std::cout << "Пара " << stage.cycle << ": "
            << toBinary(stage.a) << " x " << toBinary(stage.b)
            << " | Промежуточный результат: " << toBinary(stage.partialProduct) << "\n";
    }
    std::cout << std::endl;
}

void printResults(const std::vector<int>& results) {
    std::cout << "Результат:\n";
    for (size_t i = 0; i < results.size(); i++) {
        std::cout << "Пара " << i + 1 << ": " << results[i] << " (" << toBinary(results[i]) << ")\n";
    }
}