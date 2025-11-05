import pytest
from project.Task6.multiprocessing_hash_table import Hash_Table
import multiprocessing


def worker_add(ht, start, end):
    for i in range(start, end):
        ht[i] = f"value_{i}"


def worker_increment(ht, thread_id):
    for i in range(100):
        key = f"counter_{thread_id}"
        current = ht.get(key, 0)
        ht[key] = current + 1


class Test_Hash_Table:
    def test_all_original_methods(self):
        ht = Hash_Table()

        ht["a"] = 1
        ht["b"] = 2

        # get
        assert ht.get("a") == 1
        assert ht.get("c") is None
        assert ht.get("c", "default") == "default"

        # pop
        assert ht.pop("a") == 1
        assert "a" not in ht

        # keys, values, items
        keys = list(ht.keys())
        values = list(ht.values())
        items = list(ht.items())

        assert keys == ["b"]
        assert values == [2]
        assert items == [("b", 2)]

        # clear
        ht.clear()
        assert len(ht) == 0

        # repr
        ht["test"] = 123
        assert "test: 123" in repr(ht)

    def test_multiprocessing_no_data_loss(self):
        ht = Hash_Table()

        processes = []
        for i in range(4):
            p = multiprocessing.Process(
                target=worker_add, args=(ht, i * 25, (i + 1) * 25)
            )
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        assert len(ht) == 100
        for i in range(100):
            assert ht[i] == f"value_{i}"

    def test_multiprocessing_locks_work(self):
        ht = Hash_Table()

        processes = []
        for i in range(10):
            p = multiprocessing.Process(target=worker_increment, args=(ht, i))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        for i in range(10):
            assert ht[f"counter_{i}"] == 100


def print_apple_charlotte_recipe():
    recipe = """
    Ingredients
    Eggs - 4 pcs.
    Sugar - 1 cup (200 g)
    Flour - 1 cup (160 g)
    Apples - 4-5 pcs. (better sour varieties)
    Baking powder - 0.5 tsp.
    Vanilla sugar - 1 tsp.
    Butter - for greasing the form
    Step-by-step preparation
    1. Prepare the apples: wash, peel and remove the core. Cut the apples into thin slices or cubes. To prevent the apples from turning brown, sprinkle them with lemon juice.
    2. Beat the eggs with sugar using a mixer on high speed. The mixture should lighten in color, increase in volume, and become fluffy. This process should take 5-7 minutes.
    3. Add the dry ingredients: sift the flour with the baking powder. Gradually incorporate the flour into the egg mixture, gently mixing with a spatula from the bottom to the top.
    4. Combine the dough with the apples, reserving a few slices for decoration. Carefully mix the main part of the apples with the dough.
    5. Bake: grease the pan with butter and sprinkle with flour or semolina. Pour in the dough, spread it out, and decorate with the remaining apples. Bake at 180°C for 30-40 minutes. Check for doneness with a wooden skewer
    """
    print(recipe)


print_apple_charlotte_recipe()
