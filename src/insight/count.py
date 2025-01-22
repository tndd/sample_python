from dataset.source_a.collector import collect_data_a


def count_data():
    data = collect_data_a()
    return len(data)

# Test
def test_count_data():
    assert count_data() == 3


if __name__ == "__main__":
    print(count_data())
