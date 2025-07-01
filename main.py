import csv
from tabulate import tabulate
import argparse

parser = argparse.ArgumentParser(description="Пример использования argparse")
parser.add_argument('-f', '--file')
parser.add_argument('-w', '--where')
parser.add_argument('-a', '--aggregate')
ps = parser.parse_args()
result = []

path = ps.file
where = ps.where
aggregate = ps.aggregate

with open(path, 'r') as file:
    dict_list = []
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        dict_list.append(row)
    result = dict_list

if where:
    where_list = []
    for item in dict_list:
        if '>' in where:
            key, value = where.split('>')[0], where.split('>')[1]
            if float(item[key]) > float(value):
                where_list.append(item)

        elif '<' in where:
            key, value = where.split('<')[0], where.split('<')[1]
            if float(item[key]) < float(value):
                where_list.append(item)

        elif '=' in where:
            key, value = where.split('=')[0], where.split('=')[1]
            if key in ('price', 'rating'):
                if float(item[key]) == float(value):
                    where_list.append(item)
            else:
                if item[key] == value:
                    where_list.append(item)

    if not where_list:
        print("По установленному фильтру ничего не найдено")
    else:
        dict_list = where_list
    result = where_list

if aggregate:
    agg_list = []
    result = []
    aggregate_dict = dict()
    key, value = aggregate.split('=')[0], aggregate.split('=')[1]
    if key in ('rating', 'price'):
        for item in dict_list:
            agg_list.append(float(item[key]))
        if value == 'min':
            aggregate_dict['min'] = min(agg_list)
            result.append(aggregate_dict)
        elif value == 'max':
            aggregate_dict['max'] = max(agg_list)
            result.append(aggregate_dict)
        elif value == 'avg':
            aggregate_dict['avg'] = sum(agg_list) / len(agg_list)
            result.append(aggregate_dict)
    else:
        raise TypeError("Обрабатываются только колонки rating и price!")

print(tabulate(result, headers='keys', tablefmt="grid"))
