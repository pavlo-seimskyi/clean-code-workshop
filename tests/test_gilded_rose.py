from src.gilded_rose import GildedRose, Item


def test_dexterity_vest():
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 9
    assert gilded_rose.items[0].quality == 19


def test_aged_brie():
    items = [Item(name="Aged Brie", sell_in=2, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 1
    assert gilded_rose.items[0].quality == 1


def test_elixir_of_the_mongoose():
    items = [Item(name="Elixir of the Mongoose", sell_in=5, quality=7)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 4
    assert gilded_rose.items[0].quality == 6


def test_sulfuras_hand_of_ragnaros():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 0
    assert gilded_rose.items[0].quality == 80


def test_sulfuras_hand_of_ragnaros_negative_sell_in():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == -1
    assert gilded_rose.items[0].quality == 80


def test_backstage_passes_long_before_concert():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 14
    assert gilded_rose.items[0].quality == 21


def test_backstage_passes_medium_before_concert():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 9
    assert gilded_rose.items[0].quality == 50


def test_backstage_passes_short_before_concert():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 4
    assert gilded_rose.items[0].quality == 50
