from typing import NamedTuple

class DataRow(NamedTuple):
    title: str
    warehouse_price: float
    store_price: float
    quantity_warehouse: float
    quantity_shop1: float
    quantity_shop2: float
    quantity_shop3: float
    quantity_secret: float
    # img: str
