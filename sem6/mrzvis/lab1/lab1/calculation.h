//////////////////////////
// Лабораторная работа №1 по дисциплине "Модели решения задач в интеллектуальных системах"
// Выполнена студентом группы 221701 БГУИР Абушкевичем Алексеем Александровичем
// 
// Файл предназначен для прототипирования методов вычисления произведения
// 
// 
// Дата создания: 01.02.2025
//

#pragma once
#include "output.h"

bool anyIncompleteStages(const std::queue<PipelineStage>& pipeline);

void pipelineMultiplication(const std::vector<int>& A, const std::vector<int>& B);