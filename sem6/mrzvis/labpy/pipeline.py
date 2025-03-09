# Лабораторная работа 1
# по дисциплине Модели решения задач в интеллектуальных системах
# выполнил студент гр. 221701 БГУИР Абушкевич Алексей Александрович
# Вариант 7: алгоритм вычисления произведения пары 6-разрядных чисел умножением с младших разрядов со сдвигом множимого влево

# Файл, отвечающий за реализацию конвейера.

# Дата 21.02.2025
# Источники: Ивашенко, В. П. Модели решения задач в интеллектуальных системах : учеб.-метод. пособие : в 2 ч. Ч. 1

from file_reader import FileReader
from utils import Utils
from pair import Pair
from constants import *
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class Conveyor():
    def __init__(self):
        self.pairs = []
        self.utils = Utils()

    def load_from_file(self, filename):
        file_reader = FileReader(filename)
        self.pairs = file_reader.read_file()
        if self.pairs is None:
            self.pairs = []

    def write_pairs(self):
        for pair in self.pairs:
            print(f"Пара {pair.pair_num + 1}: {int(pair.x1, 2)} = {pair.x1}, {int(pair.x2, 2)} = {pair.x2}")

    def write_tacts(self):
        self.write_pairs()
        for i in range(ALL_BITS):
            str1 = f"Этап {i + 1} "
            str2 = ""
            for pair in self.pairs:
                if pair.index == i + 1:
                    str1 += f"Пара {pair.pair_num + 1}"
                    str2 += f"Частичная сумма: {pair.current_sum} = {int(pair.current_sum, 2)}, Частичное произведение: {pair.current_mult} = {int(pair.current_mult, 2)}"
                    break
            print(str1)
            print(str2)

    def write_results(self):
        for j in range(len(self.pairs)):
            if self.pairs[j].result != "" and self.pairs[j].index != ALL_BITS:
                print(f"Результат {j + 1}: {self.pairs[j].result} = {int(self.pairs[j].result, 2)}")

    def algorithm(self):
        for i in range(ALL_BITS + len(self.pairs) - 1):
            clear_terminal()
            for pair in self.pairs:
                if pair.pair_num <= i and pair.index <= ALL_BITS:
                    pair.part_sum()
            print(f"Такт {i + 1}")
            self.write_tacts()
            self.write_results()
            input()
        clear_terminal()
        self.write_pairs()
        for j in range(len(self.pairs)):
            print(f"Результат {j + 1}: {self.pairs[j].result} = {int(self.pairs[j].result, 2)}")
