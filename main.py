"""! @brief Данная программа предназначена для удаления повторяющихся строк в тексте. Строки могут быть восприняты
повторяющимися в нескольких случаях:
1. Строки абсолютно совпадают\n
2. Указан флаг -distance и значение расстояние Левенштейна меджу строками меньше указаного\n
3. Указан флаг -natural и для человека строки выглядят одинкого, несмотря на то, что состояит из разных символов
4. Указан флаг -case, означающий, что сравнение строк идёт без учёта регистров
."""

##
# @mainpage Удалитель повторяющихся строк
#
# @section description_main Описание
# Данная программа предназначена для удаления повторяющихся строк в тексте.\n
# Строки могут быть восприняты повторяющимися в нескольких случаях:
# 1. Строки абсолютно совпадают\n
# 2. Указан флаг -distance и значение расстояние Левенштейна меджу строками меньше указаного\n
# 3. Указан флаг -natural и для человека строки выглядят одинкого, несмотря на то, что состояит из разных символов
# 4. Указан флаг -case, означающий, что сравнение строк идёт без учёта регистров
#
# @section flags Флаги программы
# Программа имеет 4 флага:
# 1. -distance <число> - Если расстояние Левенштейна между строками меньше или равно указаного числа,
# то строки будут считаться одинаковыми
# 2. -natural - если для человека строки выглядят одинкого, несмотря на то, что состояит из разных символов,
# они буду считаться одинаковыми
# 3. -case - если при приведение к одному регистру строки одинаковы, то они будут считать одинаковыми
# 4. -timeit - будет произведёт расчёт времени выполнения основных функций програмы
# (чтение, удаление повторяющихся строк, запись)
#
# @section call_prog Вызов программы
# Для самого простого вызова программы нужно написать в консоли следующее\n
# main.py имя_входного_файла\n
# В этом случае весь вывод программы будет произведёт в косоль флаги будут поставлены в сначения False,
# а расстояние Левенштейна будет равно 0
# @section examples Примеры вызова программы
# Пример 1\n
# main.py имя_входного_файла имя_выходного_файла\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги будут поставлены в сначения False, а расстояние Левенштейна будет равно 0
#
# Пример 2\n
# main.py имя_входного_файла имя_выходного_файла -distance 5\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги будут поставлены в сначения False, а расстояние Левенштейна будет равно 5
#
# Пример 3\n
# main.py имя_входного_файла имя_выходного_файла -distance 4 -case\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги кроме case будут поставлены в сначения False, а расстояние Левенштейна будет равно 4
#
# Пример 4\n
# main.py имя_входного_файла имя_выходного_файла -distance 3 -case -timeit\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги кроме case и timeit будут поставлены в сначения False, а расстояние Левенштейна будет равно 5
# Пример 5\n
#
# main.py имя_входного_файла имя_выходного_файла -distance 2 -case -timeit natural\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги будут поставлены в сначения True, а расстояние Левенштейна будет равно 5
#
# Пример 6\n
# main.py имя_входного_файла имя_выходного_файла -distance\n
# Из входного файла будут прочитаны данные, уникальные строки будут записаны в выходной,
# все флаги будут поставлены в сначения False, а расстояние Левенштейна будет равно 0,
# поскольку не было передано значение
#
# @section notes_main Заметки
# - Заметок пока что нет
#
# @section author_doxygen_example Автор
# - Толочек Юрий 11/11/2020.
#  2020 Толочек Юрий.


##
# @file main.py
#
# @brief Удалитель повторяющихся строк.
#
# @section DuplicateRemover Описание
# Файл main.py является главным и единственным файлом программы, здесь размещён единственный клас DuplicateRemover
#
# @section libraries_main Библиотеки/Модули
# - sys Стандартная библиотека (https://docs.python.org/3/library/sys.html)
#   - Доступ к аргументам вызова из командной строки
# - time Стандартная библиотека (https://docs.python.org/3/library/time.html)
#   - Расчёт скорости работы функций программы
# - Levenshtein модуль python-Levenshtein 0.12.0 (https://github.com/ztane/python-Levenshtein)
#   - Предоставляет доступ к функции расчёта расстояния Левенштейна между строками
#
# @section notes Заметки
# - Пока нет
#
# @section todo_list TODO
# - None.
#
# @section author Автор
# - Толочек Юрий 11/11/2020.


# Imports
import sys
import time
import Levenshtein as lev

# Global Constants
## Строка с текстом для команды -help
help_me = '-help пришёл на помощь' \
          '\nПараметры для запуска программы' \
          '\n•	путь к входному файлу (первый позиционный параметр);(обязательно)' \
          '\n•	путь к выходному файлу (второй позиционный параметр), если не задан – результат выводится на консоль;' \
          '\n•	тип сравнения. По умолчанию одинаковыми считаются строго совпадающие строки. Но если задан параметр ' \
          '–distance с числом, то cтроки считаются одинаковыми, если расстояние Ливенштейна для них меньше заданного ' \
          'числа.' \
          '\n•	приведение к общему регистру (-case), если задан – большие и маленькие буквы считаются одинаковыми' \
          '\n•	флаг -natural – при указании этого флага строки будут считаться одинаковыми, если они выглядят ' \
          'одинаково для человека (учитывать, что есть символы, выглядящие одинквово) '


class DuplicateRemover:
    ## Конструктор класса.
    #
    # Не делает ничего
    def __init__(self):
        pass

    ## Функция замены похожих букв
    # @param[in] self указатель на объект
    # @param[in] line строка в которой будут заменены символов
    # @exception TypeError Ошибка появляется в случае передачи в line не строки
    # @return Входную строку с заменёнными символами

    ## Код фукнции
    # @code
    #       def replace_natural(self, line: str) -> str:
    #         if not isinstance(line, str):
    #             raise TypeError("Неверный тип данных, должна быть строк")
    #
    #         en_letters = ['Y', 'y', 'E', 'e', 'H', 'r', '3', 'X', 'x', 'B', 'A',
    #                       'a', 'n', 'p', 'o', '0', 'C', 'c', 'U', 'u', 'T', 'k']
    #         ru_letters = ['У', 'у', 'Е', 'е', 'н', 'г', 'з', 'Х', 'х', 'В', 'А',
    #                       'а', 'п', 'р', 'о', 'о', 'С', 'с', 'И', 'и', 'Т', 'к']
    #
    #         for i in range(0, len(en_letters)):
    #             line = line.replace(en_letters[i], ru_letters[i])
    #         return line
    # @endcode


    ## Пример использования функции
    # @code
    #   >>> from main import DuplicateRemover
    #   >>> remover = DuplicateRemover()
    #   >>> someline = "Cтp0ка с поxожыми буквами"
    #   >>> natural_line = remover.replace_natural(someline)
    #   >>> natural_line
    # 'Строка с похожыми буквами'
    # @endcode
    def replace_natural(self, line: str) -> str:
        if not isinstance(line, str):
            raise TypeError("Неверный тип данных, должна быть строк")

        en_letters = ['Y', 'y', 'E', 'e', 'H', 'r', '3', 'X', 'x', 'B', 'A',
                      'a', 'n', 'p', 'o', '0', 'C', 'c', 'U', 'u', 'T', 'k']
        ru_letters = ['У', 'у', 'Е', 'е', 'н', 'г', 'з', 'Х', 'х', 'В', 'А',
                      'а', 'п', 'р', 'о', 'о', 'С', 'с', 'И', 'и', 'Т', 'к']

        for i in range(0, len(en_letters)):
            line = line.replace(en_letters[i], ru_letters[i])
        return line

    ## Проверка наличия файла с указаным именем.
    # @param[in] self указатель на объект
    # @param[in] filename строка с именем файла
    # @exception FileNotFoundError Ошибка появляется в случае несуществования файла с указнным именем
    # @return строку с именем файла

    ## Код функции
    # @code
    #       def check_input_name(self, filename: str) -> str:
    #         file = open(filename, 'r')  # пытаемся открыть файл и считать с него данные
    #         file.readlines()
    #         file.close()
    #         return filename
    # @endcode

    ## Примери использования функции
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> filename = 'file.txt'
    # >>> remover.check_input_name(filename)
    # 'file.txt'
    # @endcode
    def check_input_name(self, filename: str) -> str:
        file = open(filename, 'r')  # пытаемся открыть файл и считать с него данные
        file.readlines()
        file.close()
        return filename

    ## Проверка передал ли пользователь вторым аргументом имя, а не флаг
    # @param[in] self указатель на объект
    # @param[in] filename строка с именем файла
    # @exception TypeError Ошибка появляется в случае передачи в filename не строки
    # @return Имя выходного файла, если входная строка не является флагом, пустую строку в обратном случае

    ## Код функции
    # @code
    #       def check_output_name(self, filename: str) -> str:
    #         if not isinstance(filename, str):
    #             raise TypeError("Неверный тип данных, должна быть строк")
    #         if filename == '':
    #             return '.txt'
    #         # Если строка не является флагом, значит пользователь задал имя выходному файлу
    #         if filename != '-distance' and filename != '-natural' and filename != '-case' and filename != '-timeit':
    #             return filename
    #         else:
    #             return ''
    # @endcode

    ## Пример использования функции c именем содержащим флаг
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> filename = '-distance'
    # >>> remover.check_output_name(filename)
    # ''
    # @endcode

    ## Пример использования функции c именет без флага
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> filename = 'file.txt'
    # >>> remover.check_input_name(filename)
    # 'file.txt'
    # @endcode
    def check_output_name(self, filename: str) -> str:
        if not isinstance(filename, str):
            raise TypeError("Неверный тип данных, должна быть строк")
        if filename == '':
            return '.txt'
        # Если строка не является флагом, значит пользователь задал имя выходному файлу
        if filename != '-distance' and filename != '-natural' and filename != '-case' and filename != '-timeit':
            return filename
        else:
            return ''

    ## Проверяет наличие флагов в переданном листе
    # @param[in] self указатель на объект
    # @param[in] params список параметров
    # @exception TypeError Ошибка появляется в случае передачи в params не строки
    # @return Четыре флага levenshtein_distance, case_matter, natural, time_it типов int, bool, bool,
    # bool соответственно
    #

    ## Код фукнции
    # @code
    #     def check_flags(self, params: list) -> (int, bool, bool, bool):
    #         if not isinstance(params, list):
    #             raise TypeError
    #
    #         case_matter = False if '-case' in params else True  # если среди параметров есть -case
    #         natural = True if '-natural' in params else False  # если среди параметров есть -natural
    #         time_it = True if '-timeit' in params else False  # если среди параметров есть -timeit
    #         levenshtein_distance = 0
    #         if '-distance' in params:
    #             dist_index = params.index('-distance')
    #             if len(params) > dist_index + 1:
    #                 levenshtein_distance = params[dist_index + 1]
    #                 if levenshtein_distance.isdigit():  # проверка на число
    #                     levenshtein_distance = int(levenshtein_distance)
    #
    #                 else:
    #                     print('Ошибка. После параметра -distance должно идти значение расстояния. '
    #                           'Значение расстояния будет установлено в 0')
    #                     levenshtein_distance = 0
    #         return levenshtein_distance, case_matter, natural, time_it
    # @endcode

    ## Пример использования функции
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> list = ['-natural', '-distance', '5', '-timeit', '-case']
    # >>> remover.check_flags(list)
    # (5, False, True, True)
    # @endcode
    def check_flags(self, params: list) -> (int, bool, bool, bool):
        if not isinstance(params, list):
            raise TypeError

        case_matter = False if '-case' in params else True  # если среди параметров есть -case
        natural = True if '-natural' in params else False  # если среди параметров есть -natural
        time_it = True if '-timeit' in params else False  # если среди параметров есть -timeit
        levenshtein_distance = 0
        if '-distance' in params:
            dist_index = params.index('-distance')
            if len(params) > dist_index + 1:
                levenshtein_distance = params[dist_index + 1]
                if levenshtein_distance.isdigit():  # проверка на число
                    levenshtein_distance = int(levenshtein_distance)
                else:
                    print('Ошибка. После параметра -distance должно идти значение расстояния. '
                          'Значение расстояния будет установлено в 0')
                    levenshtein_distance = 0
        return levenshtein_distance, case_matter, natural, time_it

    ## Возвращает строку в нужном регистре в зависимости флага
    # @param[in] self указатель на объект
    # @param[in] line строка
    # @param[in] case_matter флаг, в каком регистре вернуть строку
    # (True - вернуть строку без изменений, False - перевести в нижний)
    # @return Строку в нужном регистре

    ## Код функции
    # @code
    #       def get_line_case(self, line: str, case_matter: bool) -> str:
    #         if case_matter:  # если регистр имеет значение
    #             return line
    #         else:  # если не имеет, то приводим строки к нижнему регистру
    #             return line.lower()
    # @endcode

    ## Пример использования функции
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> line = "A b C d"
    # >>> remover.get_line_case(line, True)
    # 'A b C d'
    # >>> remover.get_line_case(line, False)
    # 'a b c d'
    # @endcode
    def get_line_case(self, line: str, case_matter: bool) -> str:
        if case_matter:  # если регистр имеет значение
            return line
        else:  # если не имеет, то приводим строки к нижнему регистру
            return line.lower()

    ## Возвращает строку в натуральном либо оригинальном виде зависимости флага
    # @param[in] self указатель на объект
    # @param[in] line строка
    # @param[in] natural флаг, в каком виде вернуть строку
    # (True - земенить в строке похожие английские буквы на русские, False - вернуть бе изменений)
    # @return Строку в нужном виде

    ## Код функции
    # @code
    #     def get_line_natural(self, line: str, natural: bool) -> str:
    #         if natural:  # если стоит флаг на одинаковость строк для человека
    #             return self.replace_natural(line)
    #         else:
    #             return line
    # @endcode

    ## Пример использования функции
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> someline = "Cтp0ка с поxожыми буквами"
    # >>> remover.get_line_natural(someline, True)
    # 'Строка с похожыми буквами'
    # >>> remover.get_line_natural(someline, False)
    # 'Cтp0ка с поxожыми буквами'
    # @endcode
    def get_line_natural(self, line: str, natural: bool) -> str:
        if natural:  # если стоит флаг на одинаковость строк для человека
            return self.replace_natural(line)
        else:
            return line

    ## Удаляет из списка списка line_list dct повторяющиеся элементы. Элементы будут считаться повторяющимися
    # @param[in] self указатель на объект
    # в зависимости от остальных аргументов
    # @param[in] line_list Cписок строк, среди которых будет производиться поиск
    # @param[in] levenshtein_distance Расстояние Левенштейна, если больше нуля, то при поиске одинаковых строк
    # будет производиться рассчёт их расстояния
    # @param[in] case_matter - Флаг, указывающий имеет ли значение регистр при сравнении строк(True - имеет значение)
    # @param[in] natural Флаг, указывающий считать ли строки одинаковыми, если они одинакого выглядят (True - считать)
    # @return Список уникальных строк из входного списка

    ## Код функции
    # @code
    #     def get_unique_lines(self, line_list: list, levenshtein_distance=0, case_matter=True, natural=False) -> list:
    #         if len(line_list) > 0:  # проверка на пустоту входного списка
    #             dict = {}
    #             list_copy = line_list.copy()
    #             list_copy.reverse()  # разворачиваем список, чтобы начать искать с конца
    #             for line in list_copy:  # проходимся по каждой строке в листе
    #                 line_to_add = self.get_line_case(line, case_matter)
    #                 line_to_add = self.get_line_natural(line_to_add, natural)
    #                 dict[line_to_add] = line
    #
    #             if levenshtein_distance == 0:  # если не задано расстояние Левенштейни
    #                 resault_list = list(dict.values())
    #                 resault_list.reverse()
    #                 return resault_list
    #
    #             list_keys = list(dict.keys())
    #             list_keys.reverse()
    #             unique_lines = [list_keys[0]]
    #             for i in range(1, len(list_keys)):
    #                 key = list_keys[i]
    #                 for unique in unique_lines:
    #                     dist = lev.distance(key, unique)
    #                     if dist <= levenshtein_distance:
    #                         break
    #                 else:
    #                     unique_lines.append(dict[list_keys[i]])
    #             return unique_lines
    #         else:
    #             return []  # вернуть пустой лист
    # @endcode

    ## Пример использования функции
    # @code
    # >>> from main import DuplicateRemover
    # >>> remover = DuplicateRemover()
    # >>> line_list = ['aa', 'aA', 'aa', 'aA']
    # >>> remover.get_unique_lines(line_list)
    # ['aa', 'aA']
    # >>> remover.get_unique_lines(line_list, 1)
    # ['aa']
    # >>> remover.get_unique_lines(line_list, 0, False)
    # ['aa']
    # >>> line_list = ['aaa', 'aAA', 'aaA', 'AaA']
    # >>> remover.get_unique_lines(line_list)
    # ['aaa', 'aAA', 'aaA', 'AaA']
    # >>> remover.get_unique_lines(line_list, 1)
    # ['aaa', 'aAA', 'AaA']
    # >>> remover.get_unique_lines(line_list, 0, False)
    # ['aaa']
    # @endcode
    def get_unique_lines(self, line_list: list, levenshtein_distance=0, case_matter=True, natural=False) -> list:
        if len(line_list) > 0:  # проверка на пустоту входного списка
            dict = {}
            list_copy = line_list.copy()
            list_copy.reverse()  # разворачиваем список, чтобы начать искать с конца
            for line in list_copy:  # проходимся по каждой строке в листе
                line_to_add = self.get_line_case(line, case_matter)
                line_to_add = self.get_line_natural(line_to_add, natural)
                dict[line_to_add] = line

            if levenshtein_distance == 0:  # если не задано расстояние Левенштейни
                resault_list = list(dict.values())
                resault_list.reverse()
                return resault_list

            list_keys = list(dict.keys())
            list_keys.reverse()
            unique_lines = [list_keys[0]]
            for i in range(1, len(list_keys)):
                key = list_keys[i]
                for unique in unique_lines:
                    dist = lev.distance(key, unique)
                    if dist <= levenshtein_distance:
                        break
                else:
                    unique_lines.append(dict[list_keys[i]])
            return unique_lines
        else:
            return []  # вернуть пустой лист

## Основная функция программы
    ## Код фукнции
    # @code
    # def main():
#     params = sys.argv[1:]  # Входные параметры программы
#     params_count = len(params)  # число входных параметров
#     unique_line_list = []  # Лист с сохранёнными строками
#     input_file_name = ''  # имя входного файла
#     output_file_name = ''  # имя выходного файла
#     levenshtein_distance = 0  # расстояние Левенштейна
#     case_matter = True  # имеет ли значение регистр
#     natural = False  # имеет ли значение похожесть букв
#     time_it = False  # нужно ли считать время выполнения
#
#     time_to_read = 0
#     time_to_find = 0
#     time_to_write = 0
#
#     if params_count == 0:  # Если программу запустили без параметров, выдать -help
#         print(help_me)
#     elif '-help' in sys.argv or '-h' in sys.argv:  # Если запросили -help
#         print(help_me)
#     elif params_count > 0:  # если пользователь передал параметры
#         input_file_name = DuplicateRemover.check_input_name(DuplicateRemover(),
#                                                             params[0])  # проверить имя входного файла
#         if params_count > 1:  # если больше одного параметра
#             output_file_name = DuplicateRemover.check_output_name(DuplicateRemover(),
#                                                                   params[1])  # проверить наличие имени выходного файла
#             if output_file_name == '':  # если нет имени выходного файла
#                 levenshtein_distance, case_matter, natural, time_it \
#                     = DuplicateRemover.check_flags(DuplicateRemover(), params[1:])
#                 # проверить # флаги
#             else:  # если имя есть, то проверить флаги со следующего элемента
#                 levenshtein_distance, case_matter, natural, time_it = DuplicateRemover.check_flags(DuplicateRemover(),
#                                                                                                    params[2:])  #
#
#     input_file = open(input_file_name, 'r')  # открыть файл
#
#     start_time = time.perf_counter()
#     input_lines = input_file.read().split('\n')  # считываем с него данные
#     end_time = time.perf_counter()
#     time_to_read = end_time - start_time  # фиксируем время чтения
#
#     input_file.close()  # закрываем файл
#
#     # выполняем поиск уникальных строк
#     start_time = time.perf_counter()
#     unique_line_list = DuplicateRemover.get_unique_lines(DuplicateRemover(), input_lines, levenshtein_distance,
#                                                          case_matter, natural)
#     end_time = time.perf_counter()
#     time_to_find = end_time - start_time  # фиксируем время выполнения алгоритма
#
#     start_time = time.perf_counter()
#     if output_file_name != '':  # если пользователь указал имя файла
#         output_file = open(output_file_name, 'w')
#         output_file.writelines(unique_line_list)
#     else:
#         for line in unique_line_list:  # иначе вывод на консоль
#             print(line)
#     end_time = time.perf_counter()
#     time_to_write = end_time - start_time  # фиксируем время записи
#
#     if time_it:
#         print('Время чтения файла: {0};\n'
#               'Время выполнения функции поиска: {1};\n'
#               'Время записи результата: {2}'
#               .format(time_to_read, time_to_find, time_to_write))
    # @endcode
def main():
    params = sys.argv[1:]  # Входные параметры программы
    params_count = len(params)  # число входных параметров
    unique_line_list = []  # Лист с сохранёнными строками
    input_file_name = ''  # имя входного файла
    output_file_name = ''  # имя выходного файла
    levenshtein_distance = 0  # расстояние Левенштейна
    case_matter = True  # имеет ли значение регистр
    natural = False  # имеет ли значение похожесть букв
    time_it = False  # нужно ли считать время выполнения

    time_to_read = 0
    time_to_find = 0
    time_to_write = 0

    if params_count == 0:  # Если программу запустили без параметров, выдать -help
        print(help_me)
    elif '-help' in sys.argv or '-h' in sys.argv:  # Если запросили -help
        print(help_me)
    elif params_count > 0:  # если пользователь передал параметры
        input_file_name = DuplicateRemover.check_input_name(DuplicateRemover(),
                                                            params[0])  # проверить имя входного файла
        if params_count > 1:  # если больше одного параметра
            output_file_name = DuplicateRemover.check_output_name(DuplicateRemover(),
                                                                  params[1])  # проверить наличие имени выходного файла
            if output_file_name == '':  # если нет имени выходного файла
                levenshtein_distance, case_matter, natural, time_it \
                    = DuplicateRemover.check_flags(DuplicateRemover(), params[1:])
                # проверить # флаги
            else:  # если имя есть, то проверить флаги со следующего элемента
                levenshtein_distance, case_matter, natural, time_it = DuplicateRemover.check_flags(DuplicateRemover(),
                                                                                                   params[2:])  #

    input_file = open(input_file_name, 'r')  # открыть файл

    start_time = time.perf_counter()
    input_lines = input_file.read().split('\n')  # считываем с него данные
    end_time = time.perf_counter()
    time_to_read = end_time - start_time  # фиксируем время чтения

    input_file.close()  # закрываем файл

    # выполняем поиск уникальных строк
    start_time = time.perf_counter()
    unique_line_list = DuplicateRemover.get_unique_lines(DuplicateRemover(), input_lines, levenshtein_distance,
                                                         case_matter, natural)
    end_time = time.perf_counter()
    time_to_find = end_time - start_time  # фиксируем время выполнения алгоритма

    start_time = time.perf_counter()
    if output_file_name != '':  # если пользователь указал имя файла
        output_file = open(output_file_name, 'w')
        output_file.writelines(unique_line_list)
    else:
        for line in unique_line_list:  # иначе вывод на консоль
            print(line)
    end_time = time.perf_counter()
    time_to_write = end_time - start_time  # фиксируем время записи

    if time_it:
        print('Время чтения файла: {0};\n'
              'Время выполнения функции поиска: {1};\n'
              'Время записи результата: {2}'
              .format(time_to_read, time_to_find, time_to_write))


if __name__ == '__main__':
    main()
