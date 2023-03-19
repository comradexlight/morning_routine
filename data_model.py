from typing import NamedTuple, Union
from PIL.PngImagePlugin import PngImageFile


class DataRow(NamedTuple):
    title: str
    warehouse_price: Union[int, None] 
    store_price: Union[int, None]
    quantity_warehouse: float
    quantity_shop1: float
    quantity_shop2: float
    quantity_shop3: float
    img: Union[PngImageFile,None]
