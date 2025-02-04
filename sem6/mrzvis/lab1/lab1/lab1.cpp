//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// Файл предназначен для ...
// Дата создания: 01.02.2025
//
// 

#include <iostream>
#include <vector>
#include <bitset>
#include <iomanip>
#include <queue>
#include <thread>
#include <chrono>

using namespace std;

const int BIT_WIDTH = 6;
const int TACT_DELAY = 1;

string toBinary(int num) {
    bitset<BIT_WIDTH> bits(num);
    string binStr = bits.to_string();
    return binStr.substr(0, 2) + " " + binStr.substr(2, 4);
}


void printPairs(const vector<int>& A, const vector<int>& B, const string& label) {
    cout << label << ":\n";
    for (size_t i = 0; i < min(A.size(), (size_t)5); i++) {
        cout << "Пара " << i + 1 << ": " << A[i] << " x " << B[i] << endl;
    }
    cout << endl;
}
struct PipelineStage {
    int step;
    int a, b;
    int partialProduct;
    int shift;
    int cycle;
};

void pipelineMultiplication(const vector<int>& A, const vector<int>& B) {
    printPairs(A, B, "Входная пара");
    queue<PipelineStage> pipeline;
    vector<int> results(A.size(), 0);
    int cycle = 0;
    size_t processed = 0;

    while (processed < A.size() || !pipeline.empty()) {
        cycle++;

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

        if (cycle <= A.size()) {
            pipeline.push({ 0, A[cycle - 1], B[cycle - 1], 0, 0, cycle });
        }

        cout << "Такт " << cycle << "\n";
        cout << "----------------------\n";
        queue<PipelineStage> pipelineCopy = pipeline;
        while (!pipelineCopy.empty()) {
            auto stage = pipelineCopy.front();
            pipelineCopy.pop();
            cout << "Пара " << stage.cycle << ": "
                << toBinary(stage.a) << " x " << toBinary(stage.b)
                << " | Промежуточный результат: " << toBinary(stage.partialProduct) << "\n";
        }
        cout << endl;

        cout << "   ";
        cin.get();
    }


    cout << "Результат:\n";
    for (size_t i = 0; i < min(results.size(), (size_t)5); i++) {
        cout << "Пара " << i + 1 << ": " << results[i] << " (" << toBinary(results[i]) << ")\n";
    }
}

int main() {
    setlocale(LC_ALL, "Russian");
    vector<int> A = { 48, 23, 12};
    vector<int> B = { 48, 11, 11};

    pipelineMultiplication(A, B);
    return 0;
}

//todo: пофиксить вводы всех случаев пар (когда одно число, когда две пары, когда одна пара и тд)
//todo: чтение из файла сделать
//todo: поделить на модули
//todo: добавить авторство