import csv
from tabulate import tabulate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', )
parser.add_argument('-w', '--where')
parser.add_argument('-a', '--aggregate')
ps = parser.parse_args()
result = []

path = ps.file
where = ps.where
aggregate = ps.aggregate

with open(path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        result.append(row)

if where:
    where_list = []
    for item in result:
        if '>' in where:
            key, value = where.split('>')[0], where.split('>')[1]
            if key in ('price', 'rating'):
                if float(item[key]) > float(value):
                    where_list.append(item)
                else:
                    print("Сравнения '>' и '<' доступны только для колонок 'price' и 'rating'")

        elif '<' in where:
            key, value = where.split('<')[0], where.split('<')[1]
            if key in ('price', 'rating'):
                if float(item[key]) < float(value):
                    where_list.append(item)
                else:
                    print("Сравнения '>' и '<' доступны только для колонок 'price' и 'rating'")

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
    result = where_list

if aggregate:
    agg_list = []
    agg_dict_list = []
    aggregate_dict = dict()
    key, value = aggregate.split('=')[0], aggregate.split('=')[1]
    if key in ('rating', 'price'):
        for item in result:
            agg_list.append(float(item[key]))
        if value == 'min':
            aggregate_dict['min'] = min(agg_list)
            agg_dict_list.append(aggregate_dict)
        elif value == 'max':
            aggregate_dict['max'] = max(agg_list)
            agg_dict_list.append(aggregate_dict)
        elif value == 'avg':
            aggregate_dict['avg'] = sum(agg_list) / len(agg_list)
            agg_dict_list.append(aggregate_dict)
        else:
            print("Поддерживаютя только операции min/max/avg!")
        result = agg_dict_list
    else:
        print("Обрабатываются только колонки rating и price!")

print(tabulate(result, headers='keys', tablefmt="grid"))
