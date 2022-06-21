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
    def quality(self):
        """quality attribute as a property"""
        return self._quality

    @quality.setter
    def quality(self, new_value: int):

        """quality is between 0 and 50"""
        if new_value < 0:
            new_value = 0
        if new_value > 50:
            new_value = 50
        self._quality = new_value

    def standard_update(self):
        """Items without specific rules use this method to update with the default
        value"""
        if self.sell_in >= 0:
            self.quality = self.quality - 1
        else:
            self.quality = self.quality - 2

        self.sell_in = self.sell_in - 1

    def age_brie_update(self):
        """Update for age_brie. Quality always increase by one even after sell_in"""
        self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1

    def sulfuras_update(self):
        """update for sulfuras item. No update at all"""
        pass

    def backstage_update(self):
        """update for sulfuras item. No update at all"""

        if self.sell_in >= 11:
            self.quality = self.quality + 1
        elif self.sell_in >= 6:
            self.quality = self.quality + 2
        elif self.sell_in >= 1:
            self.quality = self.quality + 3
        else:
            self.quality = 0

        self.sell_in = self.sell_in - 1

    def update_quality(self):
        if self.name == "Aged Brie":
            self.age_brie_update()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.backstage_update()
        elif self.name == "Sulfuras, Hand of Ragnaros":
            self.sulfuras_update()
        else:
            self.standard_update()


class GildedRose:
    """Main Inventory. update_quality runs once a day"""

    def __init__(self, items: Optional[List[Item]] = None):
        self.items = items if items else []

    def update_quality(self):
        for item in self.items:
            item.update_quality()
