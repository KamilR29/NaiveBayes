import random
import numpy as np


def read_data():
    file = open('car_evaluation.data')
    lines = file.readlines()
    file.close()
    return lines


def split_data(lines, number):
    file_name = "cars_evaluation_trn" + number + ".data"
    names = file_name
    file_trn = open(file_name, "w")
    file_name = "cars_evaluation_tst" + number + ".data"
    names = names + "," + file_name;
    file_tst = open(file_name, "w")

    random.shuffle(lines)

    total_lines = len(lines)
    lines_70 = int(total_lines * 0.7)

    for idx, line in enumerate(lines):
        if idx < lines_70:
            file_trn.write(line)
        else:
            file_tst.write(line)

    return names


def naive_bayes(trening_file, test_file):
    trn_file = open(trening_file)
    tst_file = open(test_file)

    trn_data = trn_file.readlines()
    tst_data = tst_file.readlines()

    # pętla tworząca słownik wyników dal danych treningowych
    trn_dict = {}
    for line in trn_data:
        array_data = line.split(',')
        last = array_data[-1].rstrip("\n")
        if last in trn_dict.keys():
            value = trn_dict[last]
            trn_dict[last] = value + 1
        else:
            trn_dict[last] = 1

    line_lenght = len(trn_data[0].split(",")) - 1
    # pętla tworząca słownik zliczająca wystąpienia poszczególnych danych w zależnoći od wyniku
    trn_values_dict = {}
    for index in range(line_lenght):
        i = str(index)
        trn_values_dict[i] = {}
        for line in trn_data:
            array_data = line.split(",")
            last = array_data[-1].strip("\n")
            if last in trn_values_dict[i]:
                if array_data[index] in trn_values_dict[i][last]:
                    value = trn_values_dict[i][last][array_data[index]]
                    trn_values_dict[i][last][array_data[index]] = value + 1
                else:
                    trn_values_dict[i][last][array_data[index]] = 1
            else:
                trn_values_dict[i][last] = {array_data[index]: 1}

    key_list = []
    for key in trn_dict.keys():
        key_list.append(key)
    # pętla obliczająca prawdopodaobieńśtwo przynależnoći do danej grupy
    final_list = []
    for line in tst_data:
        array_data = line.split(",")
        tmp_tab = []
        for value in trn_dict:
            final_value = 1

            for i in range(len(array_data) - 1):
                if (array_data[i] in trn_values_dict[str(i)][value]):
                    tmp = trn_values_dict[str(i)][value][array_data[i]]
                else:
                    tmp = 0

                final_value = final_value * (tmp / trn_dict[value])

            tmp_tab.append(final_value)
        max_value = max(tmp_tab)
        value_index = tmp_tab.index(max_value)

        final_list.append(key_list[value_index])

    iterator = 0
    sum_value = 0
    for line in tst_data:

        array_data = line.split(",")
        last = array_data[-1].strip("\n")

        if last == final_list[iterator]:
            sum_value = sum_value + 1
        iterator = iterator + 1

    accuracy = sum_value / len(final_list)

    return accuracy


def write_result(result):
    file = open("result_file", "w")
    file.write(result)


if __name__ == '__main__':

    accuracy_list = []
    final_string = ""

    for i in range(10):
        lines = read_data()
        names = split_data(lines, str(i))
        names_tab = names.split(",")

        accuracy = naive_bayes(names_tab[0], names_tab[1])
        accuracy_list.append(accuracy)
        final_string += ("Accuracy: " + str(accuracy) + "\n")
        print("Accuracy: " + str(accuracy))
    accuracy_sum = 0
    for value in accuracy_list:
        accuracy_sum = accuracy_sum + value
    mean_accuracy = accuracy_sum / len(accuracy_list)
    final_string += ("Mean accuracy: " + str(mean_accuracy) + "\n")

    print("Mean accuracy: " + str(mean_accuracy))

    standard_deviation = np.std(accuracy_list)
    final_string += ("Standard deviation: " + str(standard_deviation) + "\n")

    print("Standard deviation: " + str(standard_deviation))
    write_result(final_string)
