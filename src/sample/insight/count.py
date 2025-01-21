from sample.dataset.source_a.collector import collect_data_a


def count_data():
    data = collect_data_a()
    return len(data)


if __name__ == "__main__":
    print(count_data())
