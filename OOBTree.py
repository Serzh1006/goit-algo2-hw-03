from BTrees.OOBTree import OOBTree
import csv
import timeit

tree_storage = OOBTree()
dict_storage = {}


def add_item_to_tree(item):
    price_id = float(item["Price"])
    tree_storage.update({
        price_id: {
                "ID": item["ID"],
                "Name": item["Name"],
                "Category": item["Category"],
                "Price": item["Price"],
            }
    })

def add_item_to_dict(item):
    tree_id = int(item["ID"])
    dict_storage[tree_id] = {
                "Name": item["Name"],
                "Category": item["Category"],
                "Price": item["Price"],
            }


def load_data_from_file(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_item_to_tree(row)
            add_item_to_dict(row)

def range_query_tree(min, max):
    result = []
    data = tree_storage.items(min,max)
    for _, value in data:
        result.append(value)
    return result

def range_query_dict(min, max):
    result = []
    for value in dict_storage.values():
        if float(value["Price"]) >= float(min) and float(value["Price"]) <= float(max):
            result.append(value)
    return result


if __name__ == "__main__":
    load_data_from_file("generated_items_data.csv")
    time_tree = timeit.timeit(lambda: range_query_tree(50, 150), number = 100)
    print(f"Total range_query time for OOBTree: {time_tree:.4f} секунд")
    time_dict = timeit.timeit(lambda: range_query_dict(50, 150), number = 100)
    print(f"Total range_query time for Dict: {time_dict:.4f} секунд")
