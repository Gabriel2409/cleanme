from gilded_rose.main import GildedRose, Item


def test_foo():
    """basic test"""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
