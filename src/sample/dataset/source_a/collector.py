import random
from datetime import datetime
from uuid import uuid4

import pandas as pd


def collect_data_a():
    return [
        "data:a",
        "data:b",
        "data:c",
    ]


def collect_dummy_df(n: int = 10000):
    """
    以下のユーザーデータをn件ランダムに生成する
        1: id: uuid
        2: name: str
        3: age: int
        4: created_at: datetime
        5. group: str (A, B, C)
    """
    ids = [uuid4() for _ in range(n)]
    names = [f"name_{i}" for i in range(n)]
    ages = [random.randint(5, 80) for _ in range(n)]
    base_date = datetime.now()
    created_ats = [
        base_date - pd.Timedelta(days=random.randint(0, 365))
        for _ in range(n)
    ]
    groups = [random.choice(["A", "B", "C"]) for _ in range(n)]
    return pd.DataFrame(
        {
            "id": ids,
            "name": names,
            "age": ages,
            "created_at": created_ats,
            "group": groups,
        }
    )


### TEST ###
def test_collect_data_a():
    assert collect_data_a() == ["data:a", "data:b", "data:c"]


def test_collect_dummy_df():
    N = 1000
    df = collect_dummy_df(n=N)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == N
    # 必要なカラムは揃ってる？
    assert "id" in df.columns
    assert "name" in df.columns
    assert "age" in df.columns
    assert "created_at" in df.columns
    assert "group" in df.columns


### MAIN ###
if __name__ == "__main__":
    print(collect_data_a())
