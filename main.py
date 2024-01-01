from datetime import datetime
from tabulate import tabulate
from pyfiglet import Figlet
import statistics
import sys
import csv


def Title():
    figlet = Figlet(font="puffy", )
    print("="*72, end="")
    print("\n", end="")
    print(figlet.renderText("Main Project"))
    print("="*72, end="")
    print("\n", end="")


def change_data(path):
    try:
        with open(path) as file:
            reader = csv.reader(file)
    except FileNotFoundError:
        sys.exit("ERROR: File has not been found")
    else:
        with open(path) as file:
            reader = csv.reader(file)
            changed_table = []
            for row in reader:
                tab_pom = []
                i = 0
                for element in row:
                    if i  < 4:
                        tab_pom.append(element.strip())
                        i += 1
                    else:
                        changed_table.append(tab_pom)
                        tab_pom = []
                        tab_pom.append(element.strip())
                        i = 1
                changed_table.append(tab_pom)
        
        return changed_table


def table_information(table):
    numeric_list = []
    alpha_list = []
    blank_list = []
    for row in table:
        for element in row[1:]:
            if str(element).isnumeric():
                numeric_list.append(element)
            elif str(element).isalpha():
                alpha_list.append(element)
            elif element == "":
                blank_list.append(element)
    print(f"Number of numerical data: {len(numeric_list)}")
    print(f"Number of alpha data: {len(alpha_list)}")
    print(f"Number of empty cells: {len(blank_list)}")
    sum_of_elements = len(numeric_list) + len(alpha_list) + len(blank_list)
    if sum_of_elements == len(table):
        print("Amount of elements is good")


def print_table(table):
    print(tabulate(table, tablefmt="rounded_grid", headers=["Lp.","Quarter I", "Quarter II", "Quarter III", "Quarter IV"]))


def add_indexes(table):
    lenght_table = len(table)
    for sub_table in range(lenght_table):
        table[sub_table].insert(0, sub_table+1)


def save_as_csv_file(table, path):
    with open(path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["Lp.","Quarter I", "Quarter II", "Quarter III", "Quarter IV"])
        writer.writeheader()
        for row in table:
            if len(row) == 5:
                writer.writerow({"Lp.": row[0], "Quarter I": row[1], "Quarter II": row[2], "Quarter III": row[3], "Quarter IV": row[4]})
            if len(row) == 4:
                writer.writerow({"Lp.": row[0], "Quarter I": row[1], "Quarter II": row[2], "Quarter III": row[3]})
            if len(row) == 3:
                writer.writerow({"Lp.": row[0], "Quarter I": row[1], "Quarter II": row[2]})
            if len(row) == 2:
                writer.writerow({"Lp.": row[0], "Quarter I": row[1]})
            
    
def visual_break():
    print("="*72, end="")
    print("\n", end="")


def supplemented_data_by_row(table):
    new_table = []
    for sub_table in table:
        alternative_row = create_alternative_row(sub_table)
        new_table.append(alternative_row)
    return new_table


def supplemented_data_by_column(table):
    sub_table = table[len(table)-1]
    amount_last_elements = len(sub_table)
    quarter_table = ["I", "II", "III", "IV"]
    for column in range(1,5):
        sum = 0
        amount = 0
        for sub_table_index in range(len(table)):
            if sub_table_index != len(table)-1:
                if str(table[sub_table_index][column]).isnumeric():
                    sum += int(table[sub_table_index][column])
                    amount += 1
            else:
                if column in range(1, amount_last_elements+1):
                    if str(table[len(table)-1][column]).isnumeric():
                        sum += int(table[len(table)-1][column])
                        amount += 1
        mean = round(sum/amount)
        for sub_table_index in range(len(table)):
            cell = table[sub_table_index][column]
            if cell == "" or str(cell).isnumeric() == False:
                table[sub_table_index][column] = mean
    return table

def create_alternative_row(sub_table):
    sum = 0
    amount = 0
    for element in range(1,len(sub_table)):
        if str(sub_table[element]).isnumeric():
            sum += int(sub_table[element])
            amount += 1
    mean = round(sum/amount)
    for element in range(1,len(sub_table)):
        if str(sub_table[element]).isalpha() or sub_table[element] == "":
            sub_table[sub_table.index(sub_table[element])] = mean
    return sub_table


def remove_zeros(table):
    for sub_table in table:
        for element in sub_table:
            sub_table[sub_table.index(element)] = int(element)
    return table


def extract_column(table, index):
    column = []
    for sub_table in table:
        element = sub_table[index]
        column.append(element)
    return column

def column_informations(column_as_table):
    max_value = max(column_as_table)
    min_value = min(column_as_table)
    mean = sum(column_as_table)/len(column_as_table)
    median = statistics.median(column_as_table)
    print(f"Max value: {max_value}")
    print(f"Min value: {min_value}")
    print(f"Mean of Quarter: {round(mean,2)}")
    print(f"Median of Quarter: {median}")


def column_invalid_informations(column_as_table):
    numerical_table = []
    for element in column_as_table:
        if str(element).isnumeric():
            numerical_table.append(int(element))
    max_value = max(numerical_table)
    min_value = min(numerical_table)
    mean = sum(numerical_table)/len(numerical_table)
    median = statistics.median(numerical_table)
    print(f"Max value: {max_value}")
    print(f"Min value: {min_value}")
    print(f"Mean: {round(mean,2)}")
    print(f"Median: {median}")
    

def table_of_row_sum(table):
    sum_of_row = []
    for sub_table in table:
        pom_table = []
        pom_table.append(sum(sub_table))
        sum_of_row.append(pom_table)

    return sum_of_row


def columns_informations(table):
    column_1 = extract_column(table, 1)
    column_2 = extract_column(table, 2)
    column_3 = extract_column(table, 3)
    column_4 = extract_column(table, 4)
    print("First quarter data".rjust(45))
    column_informations(column_1)
    visual_break()
    print("Second quarter data".rjust(45))
    column_informations(column_2)
    visual_break()
    print("Third quarter data".rjust(45))
    column_informations(column_3)
    visual_break()
    print("Fourth quarter data".rjust(45))
    column_informations(column_4)
    visual_break()


def columns_invalid_informations(table):
    column_1 = extract_column(table, 1)
    column_2 = extract_column(table, 2)
    column_3 = extract_column(table, 3)
    column_4 = extract_column(table, 4)
    print("First quarter data".rjust(45))
    column_invalid_informations(column_1)
    visual_break()
    print("Second quarter data".rjust(45))
    column_invalid_informations(column_2)
    visual_break()
    print("Third quarter data".rjust(45))
    column_invalid_informations(column_3)
    visual_break()
    print("Fourth quarter data".rjust(45))
    column_invalid_informations(column_4)
    visual_break()


def save_columns_as_csv_file(table):
    with open("sums_of_columns.txt", "w") as column_csv:
        writer = csv.DictWriter(column_csv, fieldnames=["Sum_of_row"])
        writer.writeheader()
        for sum in table:
            writer.writerow({"Sum_of_row": sum[0]})
    

def options():
    while True:
        try:
            print("1. Supplement data by row")
            print("2. Supplement data by row")
            choice = input("Choice the option: ")
        except ValueError:
            pass
        else:
            if choice == "2" or choice == "1":
                break
            elif choice == "0":
                sys.exit("System has been closed")
    return choice

def show_and_save_time():
    time = datetime.now()
    print(f"Done: {time.strftime("%X")} {time.strftime("%x")}")
    with open("correct_wages.txt", "a") as file:
        file.write(f"Done: {time.strftime("%X")} {time.strftime("%x")}")


def main():
    Title()
    user_choice = options()
    #print("Table contain input data")
    changed_input_table = change_data("wages.txt")
    add_indexes(changed_input_table)
    print_table(changed_input_table)
    save_as_csv_file(changed_input_table, "wages_1.txt")
    table_information(changed_input_table)
    visual_break()
    columns_invalid_informations(changed_input_table)
    print("Table with changed and completed data")
    if user_choice == "1":
        not_all_correct_table_values = supplemented_data_by_row(changed_input_table)
    else:
        not_all_correct_table_values = supplemented_data_by_column(changed_input_table)
    correct_table = remove_zeros(not_all_correct_table_values)
    print_table(correct_table)
    save_as_csv_file(correct_table, "correct_wages.txt")
    table_information(not_all_correct_table_values)
    visual_break()
    columns_informations(correct_table)
    rows_sums_table = table_of_row_sum(correct_table)
    save_columns_as_csv_file(rows_sums_table)
    show_and_save_time()
    

if __name__ == '__main__':
    main()