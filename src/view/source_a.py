from dataset.source_a.collector import collect_data_a, collect_dummy_df_users


def get_data_string():
    data = collect_data_a()
    return ", ".join(data)


def get_names(n: int = 1000):
    df = collect_dummy_df_users(n)
    return df["name"].tolist()


### TEST ###
def test_get_data_string():
    assert get_data_string() == "data:a, data:b, data:c"


def test_get_names():
    N = 100
    assert len(get_names(N)) == N
    # 全部name_から始まる文字列か?
    assert all(name.startswith("name_") for name in get_names(N))


### MAIN ###
if __name__ == "__main__":
    print(get_names(10))
