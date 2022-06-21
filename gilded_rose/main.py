# inspired by https://github.com/emilybache/GildedRose-Refactoring-Kata and simplified
from typing import List, Optional


class Item:
    """Item to be used by Gilded Rose"""

    def __init__(self, name: str, sell_in: int, quality: int):
        """Inits an item
        Args:
            name (str): the name of the item
            sell_in (int): the nb of days before the item quality degrades twice as fast
            quality (int): value between 0 and 50

        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """repr of the item"""
        return f"{self.name}, {self.sell_in}, {self.quality}"

    @property
    def sell_in(self):
        """sell in attribute as a property"""
        return self._sell_in

    @sell_in.setter
    def sell_in(self, new_value: int):
        """sell_in cant't be negative"""
        if new_value < 0:
            self._sell_in = 0

    @property
    def quality(self):
        """quality attribute as a property"""
        return self._quality

    @quality.setter
    def quality(self, new_value: int):
        """quality is between 0 and 50"""
        if new_value < 0:
            self._quality = 0
        if new_value > 50:
            self._quality = 50


class GildedRose:
    """Main Inventory. update_quality runs once a day"""

    def __init__(self, items: Optional[List[Item]] = None):
        self.items = items if items else []

    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            if item.name != "Sulfuras, Hand of Ragnaros":

                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:

                if item.name != "Aged Brie":

                    if item.name != "Backstage passes to a TAFKAL80ETC concert":

                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:

                    if item.quality < 50:
                        item.quality = item.quality + 1
