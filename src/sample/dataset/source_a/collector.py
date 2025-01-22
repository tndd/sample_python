import random
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

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
        1: id: int
        2: name: str
        3: age: int
        4: created_at: datetime
        5. group: str (A, B, C)
    """
    ids = [i for i in range(n)]
    names = [f"name_{i}" for i in range(n)]
    ages = [random.randint(18, 80) for _ in range(n)]
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
        1: transaction_id: int
        2: price: int
        3: quantity: int
        4: created_at: datetime
        5: buyer_id: int
        6: seller_id: int
    """
    ids = [i for i in range(n)]
    prices = [random.randint(100, 10000) for _ in range(n)]
    quantities = [random.randint(1, 1000) for _ in range(n)]
    base_date = datetime.now()
    created_ats = [
        base_date - pd.Timedelta(days=random.randint(0, 365))
        for _ in range(n)
    ]
    buyer_ids = [random.randint(0, n-1) for _ in range(n)]
    seller_ids = [random.randint(0, n-1) for _ in range(n)]
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


def get_dummy_dfs_users_transactions(n: int = 10000):
    """
    並列でユーザーデータと取引データを取得
    """
    with ThreadPoolExecutor() as executor:
        future_users = executor.submit(collect_dummy_df_users, n)
        future_transactions = executor.submit(collect_dummy_df_product_transactions, n)
        df_users = future_users.result()
        df_transactions = future_transactions.result()
    return df_users, df_transactions


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


def test_get_dummy_dfs_users_transactions():
    N = 100000
    df_users, df_transactions = get_dummy_dfs_users_transactions(n=N)
    assert isinstance(df_users, pd.DataFrame)
    assert isinstance(df_transactions, pd.DataFrame)
    assert len(df_users) == N
    assert len(df_transactions) == N


### MAIN ###
if __name__ == "__main__":
    print(collect_dummy_df_product_transactions())

