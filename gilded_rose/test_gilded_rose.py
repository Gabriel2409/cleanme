from gilded_rose.main import GildedRose, Item


def test_sell_in_decrease():
    """basic test"""
    items = [
        Item("Aged Brie", 1, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 1, 0),
        Item("Sulfuras, Hand of Ragnaros", 1, 0),
        Item("Random", 1, 0),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == 0
    assert items[1].name == "Backstage passes to a TAFKAL80ETC concert"
    assert items[1].sell_in == 0
    assert items[2].name == "Sulfuras, Hand of Ragnaros"
    assert items[2].sell_in == 1
    assert items[3].name == "Random"
    assert items[3].sell_in == 0

    gilded_rose.update_quality()

    assert items[0].sell_in == -1
    assert items[1].sell_in == -1
    assert items[2].sell_in == 1
    assert items[3].sell_in == -1


def test_quality_change_random():
    """basic test"""
    items = [
        Item("Random", 1, -15),
        Item("Random", 1, 75),
    ]

    assert items[0].quality == 0
    assert items[1].quality == 50
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 0
    assert items[1].quality == 49

    gilded_rose.update_quality()
    assert items[0].quality == 0
    assert items[1].quality == 48

    gilded_rose.update_quality()
    assert items[0].quality == 0
    assert items[1].quality == 46


def test_quality_change_aged_brie():
    """basic test"""
    items = [
        Item("Aged Brie", 1, -15),
        Item("Aged Brie", 1, 75),
    ]

    assert items[0].quality == 0
    assert items[1].quality == 50
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 1
    assert items[1].quality == 50


def test_quality_change_sulfuras():
    """basic test"""
    items = [
        Item("Sulfuras", 1, -15),
        Item("Aged Brie", 1, 75),
    ]

    assert items[0].quality == 0
    assert items[1].quality == 50
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 0
    assert items[1].quality == 50


def test_quality_change_backstage():
    """basic test"""
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 40, 25),
        Item("Backstage passes to a TAFKAL80ETC concert", 8, 25),
        Item("Backstage passes to a TAFKAL80ETC concert", 4, 25),
        Item("Backstage passes to a TAFKAL80ETC concert", 0, 25),
    ]

    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()
    assert items[0].quality == 26
    assert items[1].quality == 27
    assert items[2].quality == 28
    assert items[3].quality == 0
