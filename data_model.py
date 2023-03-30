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
    warehouse_price: Union[int, Literal['Цена склада'], None] 
    quantity_warehouse: Union[float, Literal['01.Склад']]
    quantity_shop1: Union[float, Literal['02.ЦЧК']]
    quantity_shop2: Union[float, Literal['03.Дом Чая']]
    quantity_shop3: Union[float, Literal['04.Аллея']]
    img: Union[PngImageFile, Literal['Картинка'], None]


class ShopItem(NamedTuple):
    title: str
    shop_price: Union[int, None] 
    quantity_shop1: Union[float, Literal['02.ЦЧК']]
    quantity_warehouse: Union[float, Literal['01.Склад']]
    quantity_shop2: Union[float, Literal['03.Дом Чая']]
    quantity_shop3: Union[float, Literal['04.Аллея']]
    img: Union[PngImageFile, Literal['Картинка']]


class SmallWholesaleItem(NamedTuple):
    title: str
    img: Union[PngImageFile, Literal['Картинка'], None]
    small_wholesale_price: Union[int, Literal['Мелкий опт'], None]
    order: Union[float, Literal['Заказ']]
    cost: Union[float, Literal['Стоимость'], None]


class MediumWholesaleItem(NamedTuple):
    title: str
    img: Union[PngImageFile, Literal['Картинка'], None]
    medium_wholesale_price: Union[int, Literal['Средний опт'], None]
    order: Union[float, Literal['Заказ']]
    cost: Union[float, Literal['Стоимость'], None]


class LargeWholesaleItem(NamedTuple):
    title: str
    img: Union[PngImageFile, Literal['Картинка'], None]
    large_wholesale_price: Union[int, Literal['Крупный опт'], None]
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
    small_wholesale_price = 'Мелкий опт',
    order = 'Заказ',
    cost = 'Стоимость'
)

medium_wholesale_title_line = MediumWholesaleItem(
    title = 'Наименование',
    img = 'Картинка',
    medium_wholesale_price = 'Средний опт',
    order = 'Заказ',
    cost = 'Стоимость'
)

large_wholesale_title_line = LargeWholesaleItem(
    title = 'Наименование',
    img = 'Картинка',
    large_wholesale_price = 'Крупный опт',
    order = 'Заказ',
    cost = 'Стоимость'
)