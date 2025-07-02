import csv


def read_csv(path: str) -> list:
    """
    Функция для чтения csv файла
    :param path: принимает путь к файлу в формате str
    :return: список словарей с данными
    """
    data = []
    with open(path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def where_list(where: str, data_list: list) -> list:
    """
    Функция для фильтрации данных
    :param where:строка вида - название столбца=фильтр
    :param data_list: список словарей с данными
    :return: список словарей с отфильтрованными данными
    """
    data = []
    for item in data_list:
        if ">" in where:
            key, value = where.split(">")[0], where.split(">")[1]
            if key in ("price", "rating"):
                if float(item[key]) > float(value):
                    data.append(item)
                else:
                    print(
                        "Сравнения '>' и '<' доступны только для колонок 'price' и 'rating'"
                    )

        elif "<" in where:
            key, value = where.split("<")[0], where.split("<")[1]
            if key in ("price", "rating"):
                if float(item[key]) < float(value):
                    data.append(item)
                else:
                    print(
                        "Сравнения '>' и '<' доступны только для колонок 'price' и 'rating'"
                    )

        elif "=" in where:
            key, value = where.split("=")[0], where.split("=")[1]
            if key in ("price", "rating"):
                if float(item[key]) == float(value):
                    data.append(item)
            else:
                if item[key] == value:
                    data.append(item)
    return data


def aggregate_list(agg: str, data_list: list) -> list:
    """
    Функция агрегации
    :param agg: строка вида - название столбца=вид агрегации
    :param data_list: список словарей с данными
    :return: список словарей с агрегированными данными
    """
    agg_list = []
    data = []
    aggregate_dict = dict()
    key, value = agg.split("=")[0], agg.split("=")[1]
    if key in ("rating", "price"):
        for item in data_list:
            agg_list.append(float(item[key]))
        if value == "min":
            aggregate_dict["min"] = min(agg_list)
            data.append(aggregate_dict)
        elif value == "max":
            aggregate_dict["max"] = max(agg_list)
            data.append(aggregate_dict)
        elif value == "avg":
            aggregate_dict["avg"] = sum(agg_list) / len(agg_list)
            data.append(aggregate_dict)
        else:
            print("Поддерживаютя только операции min/max/avg!")
    else:
        print("Обрабатываются только колонки rating и price!")
    return data
