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
