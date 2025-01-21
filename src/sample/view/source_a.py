from sample.dataset.source_a.collector import collect_data_a, collect_dummy_df


def get_data_string():
    data = collect_data_a()
    return ", ".join(data)


def test_get_data_string():
    assert get_data_string() == "data:a, data:b,data:c"


if __name__ == "__main__":
    print(get_data_string())

