from tabulate import tabulate
import argparse

from utils.func import aggregate_filter, where_filter, read_csv

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
        data = where_filter(where, data)


if aggregate:
    if data:
        data = aggregate_filter(aggregate, data)

print(tabulate(data, headers="keys", tablefmt="grid"))
