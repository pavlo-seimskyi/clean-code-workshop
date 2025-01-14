# Gilded Rose Kata

![img](https://miro.medium.com/v2/resize:fit:1024/1*pyxAQpWdiVe8JO0fJYIPxw.jpeg)

Hi and welcome to team Gilded Rose. We are a small inn with a prime location in a prominent city. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

- All `items` have a `SellIn` value which denotes the number of days we have to sell the `items`.
- All `items` have a `Quality` value which denotes how valuable the item is.
- At the end of each day our system lowers both values for every item.

Pretty simple, right? Well this is where it gets interesting:

- Once the sell by date has passed, `Quality` degrades twice as fast.
- The `Quality` of an item is never negative.
- __"Aged Brie"__ actually increases in `Quality` the older it gets.
- The `Quality` of an item is never more than `50`.
- __"Sulfuras"__, being a legendary item, never has to be sold. It does not decrease in `Quality`.
- __"Backstage passes"__, like aged brie, increases in `Quality` as its `SellIn` value approaches;
	- `Quality` increases by `2` when there are `10` days or less and by `3` when there are `5` days or less but...
	- `Quality` drops to `0` after the concert.

Just for clarification, an item can never have its `Quality` increase above `50`, however __"Sulfuras"__ is a legendary item and as such its `Quality` is `80` and it never alters.

### Your task

We have recently signed a supplier of conjured items. This requires an update to our system:

Add a new __"Conjured"__ item. __"Conjured"__ items degrade in `Quality` twice as fast as normal items.

---
