from sample.dataset.source_a.collector import collect_data_a


def get_data_string():
    data = collect_data_a()
    return "\n".join(data)


if __name__ == "__main__":
    print(get_data_string())
