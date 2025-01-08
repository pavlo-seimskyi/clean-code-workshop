from src.gilded_rose import Item, GildedRose


def test_that_is_broken():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "fixme"
