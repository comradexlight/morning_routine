from typing import NamedTuple, Union, Literal
from PIL.PngImagePlugin import PngImageFile


class PriceItem(NamedTuple):
    title: str
    purchase_price: Union[int, None]
    large_wholesale_price: Union[int, None]
    medium_wholesale_price: Union[int, None]
    small_wholesale_price: Union[int, None]
    warehouse_price: Union[int, None] 
    shop_price: Union[int, None]
    quantity_warehouse: float
    quantity_shop1: float
    quantity_shop2: float
    quantity_shop3: float
    img: Union[PngImageFile,None]
    secret_warehouse: float


class WarehouseItem(NamedTuple):
    title: str
    warehouse_price: Union[int, str, None] 
    quantity_warehouse: Union[float, str]
    quantity_shop1: Union[float, str]
    quantity_shop2: Union[float, str]
    quantity_shop3: Union[float, str]
    img: Union[PngImageFile, str, None]


class ShopItem(NamedTuple):
    title: str
    shop_price: Union[int, None] 
    quantity_shop1: Union[float, str]
    quantity_warehouse: Union[float, str]
    quantity_shop2: Union[float, str]
    quantity_shop3: Union[float, str]
    img: Union[PngImageFile, str, None]


class SmallWholesaleItem(NamedTuple):
    title: str
    img: Union[PngImageFile, Literal['Картинка'], None]
    small_wholesale_price: Union[int, Literal['Цена склада'], None]
    order: Union[float, Literal['Заказ']]
    cost: Union[float, Literal['Стоимость'], None]


warehouse_title_line = WarehouseItem(
        title = 'Наименование',
        warehouse_price = 'Цена склада',
        quantity_warehouse = '01.Склад',
        quantity_shop1 = '02.ЦЧК',
        quantity_shop2 = '03.Дом Чая',
        quantity_shop3 = '04.Аллея',
        img = 'Картинка'
        )
        

shop_title_line = ShopItem(
        title = 'Наименование',
        shop_price = 'Розничная',
        quantity_shop1 = '02.ЦЧК',
        quantity_warehouse = '01.Склад',
        quantity_shop2 = '03.Дом Чая',
        quantity_shop3 = '04.Аллея',
        img = 'Картинка'
        )


small_wholesale_title_line = SmallWholesaleItem(
    title = 'Наименование',
    img = 'Картинка',
    small_wholesale_price = 'Цена склада',
    order = 'Заказ',
    cost = 'Стоимость'
)