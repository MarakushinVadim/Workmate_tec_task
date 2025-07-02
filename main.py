from tabulate import tabulate
import argparse

from func import aggregate_list, where_list, read_csv

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--file",
)
parser.add_argument("-w", "--where")
parser.add_argument("-a", "--aggregate")
ps = parser.parse_args()

path = ps.file
where = ps.where
aggregate = ps.aggregate

data = read_csv(path)

if where:
    if data:
        data = where_list(where, data)


if aggregate:
    if data:
        data = aggregate_list(aggregate, data)

print(tabulate(data, headers="keys", tablefmt="grid"))
