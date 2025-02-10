//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// 
// Файл предназначен для прототипирования методов вывода стадий в интерфейс коммандной строки
// 
// 
// Дата создания: 01.02.2025
//
#pragma once
#include <string>
#include <bitset>
#include <iomanip>
#include <queue>
#include <thread>
#include <chrono>
#include <iostream>
const int BIT_WIDTH = 6;
const int TACT_DELAY = 1;

struct PipelineStage {
    int step;
    int a, b;
    int partialProduct;
    int shift;
    int cycle;
};

std::string toBinary(int num);

void printPairs(const std::vector<std::pair<int, int>>& pairs, const std::string& label, size_t processedCount = 0);

void printPipelineState(const std::queue<PipelineStage>& pipeline);

void printResults(const std::vector<int>& results);