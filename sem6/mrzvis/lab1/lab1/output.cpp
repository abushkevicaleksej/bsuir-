//////////////////////////
// ������������ ������ �1 �� ���������� "������ ������� ����� � ���������������� ��������"
// ��������� ��������� ������ 221701 ����� ����������� �������� ���������������
// 
// ���� ������������ ��� ���������� ������� ������ ������ � ��������� ���������� ������
// 
// 
// ���� ��������: 01.02.2025
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
        std::cout << "���� " << (i + 1 + processedCount) << ": " << pairs[i].first << " x " << pairs[i].second << std::endl;
    }
    std::cout << std::endl;
}

void printPipelineState(const std::queue<PipelineStage>& pipeline) {
    std::cout << "������� ��������� ���������:\n";
    std::queue<PipelineStage> pipelineCopy = pipeline;
    while (!pipelineCopy.empty()) {
        auto stage = pipelineCopy.front();
        pipelineCopy.pop();
        std::cout << "���� " << stage.cycle << ": "
            << toBinary(stage.a) << " x " << toBinary(stage.b)
            << " | ������������� ���������: " << toBinary(stage.partialProduct) << "\n";
    }
    std::cout << std::endl;
}

void printResults(const std::vector<int>& results) {
    std::cout << "���������:\n";
    for (size_t i = 0; i < results.size(); i++) {
        std::cout << "���� " << i + 1 << ": " << results[i] << " (" << toBinary(results[i]) << ")\n";
    }
}