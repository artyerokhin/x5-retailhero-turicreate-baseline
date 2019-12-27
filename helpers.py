import pandas as pd
import turicreate as tc


def parse_data(query_data):
    client = query_data.get("client_id", None)
    history = query_data.get("transaction_history", None)
    products = []

    if not client:
        return None, None

    if history:
        for session in history:
            session_products = session.get("products", None)
            if session_products:
                for product in session_products:
                    products.append([client, product["product_id"]])
        return client, tc.SFrame(pd.DataFrame(products, columns=["client_id", "product_id"]))
    else:
        return None, None


def sort_by_dict(lst, dct):
    counts = []

    for element in lst:
        counts.append((element, dct.get(element, 0)))

    return [count[0] for count in sorted(counts, key=lambda x: x[1], reverse=True)]
