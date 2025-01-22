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


def collect_dummy_df_users(n: int = 10000):
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


def collect_dummy_df_product_transactions(n: int = 10000):
    """
    取引データのダミーデータをn件ランダムに生成する
        1: id: uuid
        2: price: int
        3: quantity: int
        4: created_at: datetime
        5: buyer_id: uuid
        6: seller_id: uuid
    """
    ids = [uuid4() for _ in range(n)]
    prices = [random.randint(100, 10000) for _ in range(n)]
    quantities = [random.randint(1, 1000) for _ in range(n)]
    base_date = datetime.now()
    created_ats = [
        base_date - pd.Timedelta(days=random.randint(0, 365))
        for _ in range(n)
    ]
    buyer_ids = [uuid4() for _ in range(n)]
    seller_ids = [uuid4() for _ in range(n)]
    return pd.DataFrame(
        {
            "id": ids,
            "price": prices,
            "quantity": quantities,
            "created_at": created_ats,
            "buyer_id": buyer_ids,
            "seller_id": seller_ids,
        }
    )


### TEST ###
def test_collect_data_a():
    assert collect_data_a() == ["data:a", "data:b", "data:c"]


def test_collect_dummy_df_users():
    N = 1000
    df = collect_dummy_df_users(n=N)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == N
    # 必要なカラムは揃ってる？
    assert "id" in df.columns
    assert "name" in df.columns
    assert "age" in df.columns
    assert "created_at" in df.columns
    assert "group" in df.columns


def test_collect_dummy_df_product_transactions():
    N = 1000
    df = collect_dummy_df_product_transactions(n=N)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == N
    # 必要なカラムは揃ってる？
    assert "id" in df.columns
    assert "price" in df.columns
    assert "quantity" in df.columns
    assert "created_at" in df.columns
    assert "buyer_id" in df.columns
    assert "seller_id" in df.columns


### MAIN ###
if __name__ == "__main__":
    print(collect_dummy_df_product_transactions())

