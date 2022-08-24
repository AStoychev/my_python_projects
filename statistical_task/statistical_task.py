from math import  ceil
import pandas as pd

# Condition:
# The app finds the average age and average profit by group.
# Mean(median) age and mean earnings for each group.
# Minimum and maximum age for each group.
# If the .csv file lacks information about the profit of some id. The application must fill in the gaps with the
# following information relative to the group:
# Group A: 3200
# Group B: 6500
# Group C: 23000
# Group D: 37000

# Instruction for trying out the code:
# 1. First you have to install pandas module. In terminal, you have to running: pip install pandas;
# 2. In df you need to put the path to the file with the extension.csv. For example: data.csv

df = pd.read_csv(r"")

def average_by_group(person):
    result = round(sum(person) / len(person))
    return result


def mean(current_list):
    if len(current_list) % 2 == 0:
        first = int(len(current_list) / 2)
        second = int(first - 1)
        final = (current_list[first] + current_list[second]) / 2
    else:
        final = current_list[int(len(current_list) / 2)]

    return ceil(final)

age_A = []
age_B = []
age_C = []
age_D = []

profit_A = []
profit_B = []
profit_C = []
profit_D = []
is_null = pd.isnull(df.Profit)

for i in range(len(df.Group)):
    if df.Group[i] == "A":
        if is_null[i]:
            df.Profit[i] = 3200
        age_A.append(df.age[i])
        profit_A.append(df.Profit[i])
    elif df.Group[i] == "B":
        if is_null[i]:
            df.Profit[i] = 6500
        age_B.append(df.age[i])
        profit_B.append((df.Profit[i]))
    elif df.Group[i] == "C":
        if is_null[i]:
            df.Profit[i] = 23000
        age_C.append(df.age[i])
        profit_C.append(df.Profit[i])
    elif df.Group[i] == "D":
        if is_null[i]:
            df.Profit[i] = 37000
        age_D.append(df.age[i])
        profit_D.append(df.Profit[i])

avg_age_group_A = average_by_group(age_A)
avg_age_group_B = average_by_group(age_B)
avg_age_group_C = average_by_group(age_C)
avg_age_group_D = average_by_group(age_D)

avg_profit_group_A = average_by_group(profit_A)
avg_profit_group_B = average_by_group(profit_B)
avg_profit_group_C = average_by_group(profit_C)
avg_profit_group_D = average_by_group(profit_D)

sorted_age_A = sorted(age_A)
sorted_age_B = sorted(age_B)
sorted_age_C = sorted(age_C)
sorted_age_D = sorted(age_D)

sorted_profit_A = sorted(profit_A)
sorted_profit_B = sorted(profit_B)
sorted_profit_C = sorted(profit_C)
sorted_profit_D = sorted(profit_D)

final_avg_age = [avg_age_group_A, avg_age_group_B, avg_age_group_C, avg_age_group_D]
final_avg_profit = [avg_profit_group_A, avg_profit_group_B, avg_profit_group_C, avg_profit_group_D]
final_sorted_age = [sorted_age_A, sorted_age_B, sorted_age_C, sorted_age_D]
final_sorted_profit = [sorted_profit_A, sorted_profit_B, sorted_profit_C, sorted_profit_D]
group = ["A", "B", "C", "D"]

for i in range(len(group)):
    print(f"Average age {group[i]}: {final_avg_age[i]}")
    print(f"Average profit {group[i]}: {final_avg_profit[i]}")
    print(f"Min age group {group[i]}: {min(final_sorted_age[i])}")
    print(f"Max age group {group[i]}: {max(final_sorted_age[i])}")
    print(f"Mean age group {group[i]}: {mean(final_sorted_age[i])}")
    print(f"Mean profit group {group[i]}: {mean(final_sorted_profit[i])}")