//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// 
// Вариант 7. Алгоритм вычисления произведения пары 6-разрядных чисел умножением с младших разрядов со сдвигом множимого влево.
// 
// Файл предназначен для реализации методов вычисления произведения
// 
// Дата создания: 01.02.2025


#include "calculation.h"
bool anyIncompleteStages(const std::queue<PipelineStage>& pipeline) {
    std::queue<PipelineStage> pipelineCopy = pipeline;
    while (!pipelineCopy.empty()) {
        if (pipelineCopy.front().step < BIT_WIDTH) {
            return true;
        }
        pipelineCopy.pop();
    }
    return false;
}

void pipelineMultiplication(const std::vector<int>& A, const std::vector<int>& B) {
    std::vector<std::pair<int, int>> remainingPairs;
    for (size_t i = 0; i < A.size(); ++i) {
        remainingPairs.emplace_back(A[i], B[i]);
    }

    printPairs(remainingPairs, "Входные пары");

    std::queue<PipelineStage> pipeline;
    std::vector<int> results(A.size(), 0);
    int cycle = 0;
    size_t processed = 0;
    size_t nextPairIndex = 0;

    while (!pipeline.empty() || nextPairIndex < A.size()) {
        cycle++;

        // Добавляем новую пару в конвейер
        if (nextPairIndex < A.size()) {
            pipeline.push({ 0, remainingPairs[0].first, remainingPairs[0].second, 0, 0, static_cast<int>(nextPairIndex + 1) });
            remainingPairs.erase(remainingPairs.begin());
            nextPairIndex++;
        }

        // Обрабатываем конвейер
        size_t size = pipeline.size();
        for (size_t i = 0; i < size; i++) {
            PipelineStage stage = pipeline.front();
            pipeline.pop();

            if (stage.step < BIT_WIDTH) {
                if (stage.b & (1 << stage.step)) {
                    stage.partialProduct += (stage.a << stage.step);
                }
                stage.step++;
                pipeline.push(stage);
            }
            else {
                results[stage.cycle - 1] = stage.partialProduct;
                processed++;
            }
        }


        if (!remainingPairs.empty()) {
            printPairs(remainingPairs, "Оставшиеся пары", nextPairIndex);
        }

        if (!pipeline.empty()) {
            std::cout << "Этап " << cycle << "\n";
            printPipelineState(pipeline);
        }

        if (pipeline.empty() && nextPairIndex >= A.size()) {

            break;
        }

        std::cin.get();
    }

    printResults(results);
}