//////////////////////////
// ������������ ������ �1 �� ���������� "������ ������� ����� � ���������������� ��������"
// ��������� ��������� ������ 221701 ����� ����������� �������� ���������������
// 
// ������� 7. �������� ���������� ������������ ���� 6-��������� ����� ���������� � ������� �������� �� ������� ��������� �����.
// 
// ���� ������������ ��� ���������� ������� ���������� ������������
// 
// ���� ��������: 01.02.2025


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

    printPairs(remainingPairs, "������� ����");

    std::queue<PipelineStage> pipeline;
    std::vector<int> results(A.size(), 0);
    int cycle = 0;
    size_t processed = 0;
    size_t nextPairIndex = 0;

    while (!pipeline.empty() || nextPairIndex < A.size()) {
        cycle++;

        // ��������� ����� ���� � ��������
        if (nextPairIndex < A.size()) {
            pipeline.push({ 0, remainingPairs[0].first, remainingPairs[0].second, 0, 0, static_cast<int>(nextPairIndex + 1) });
            remainingPairs.erase(remainingPairs.begin());
            nextPairIndex++;
        }

        // ������������ ��������
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
            printPairs(remainingPairs, "���������� ����", nextPairIndex);
        }

        if (!pipeline.empty()) {
            std::cout << "���� " << cycle << "\n";
            printPipelineState(pipeline);
        }

        if (pipeline.empty() && nextPairIndex >= A.size()) {

            break;
        }

        std::cin.get();
    }

    printResults(results);
}