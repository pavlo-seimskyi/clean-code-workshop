# Intro

Here is some legacy code that works but is hard to understand and modify.

Refactor it incrementally using these guidelines:
1. **Tests first**
2. **Express your intent**
3. **Avoid duplication**
4. **Use meaningful names**
    - Unique enough to be searchable
    - Follow conventions
    - Pronounceable
    - Verbs for functions, nouns for classes
5. **Functions**
    - Do one thing!
    - Have no side effects.
    - Are small. Ideally, up to 4 lines of code. Not exceeding 2 levels of indentation. Minimize the number of arguments.
6. **Classes**
    - Have one responsibility!
    - Few instance variables, but all of them used a lot.

# Gilded Rose Kata

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

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

We have recently signed a supplier of conjured items. This requires an update to our system:

- __"Conjured"__ items degrade in `Quality` twice as fast as normal items

Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the `UpdateQuality` method and Items property static if you like, we'll cover for you).

Just for clarification, an item can never have its `Quality` increase above `50`, however __"Sulfuras"__ is a legendary item and as such its `Quality` is `80` and it never alters.

---
