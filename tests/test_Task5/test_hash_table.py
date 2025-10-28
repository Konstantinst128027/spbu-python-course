import pytest
from project.Task5.hash_table import Hash_Table


class TestHashTable:
    def test_init(self):
        ht = Hash_Table()
        assert ht.size == 50
        assert len(ht.buckets) == 50

        ht_custom = Hash_Table(100)
        assert ht_custom.size == 100
        assert len(ht_custom.buckets) == 100

    def test_setitem_and_getitem(self):
        ht = Hash_Table()

        ht["apple"] = 5

        assert ht["apple"] == 5

    def test_setitem_update(self):
        ht = Hash_Table()

        ht["apple"] = 5
        assert ht["apple"] == 5

        ht["apple"] = 10
        assert ht["apple"] == 10

    def test_getitem_key_error(self):
        ht = Hash_Table()

        with pytest.raises(KeyError):
            apple = ht["apple"]

    def test_delitem(self):
        ht = Hash_Table()

        ht["apple"] = 5
        ht["banana"] = 3

        del ht["apple"]

        with pytest.raises(KeyError):
            apple = ht["apple"]

        assert ht["banana"] == 3

    def test_delitem_key_error(self):
        ht = Hash_Table()

        with pytest.raises(KeyError):
            del ht["nonexistent"]

    def test_contains(self):
        ht = Hash_Table()

        ht["apple"] = 5

        assert "apple" in ht
        assert "banana" not in ht

    def test_len(self):
        ht = Hash_Table()

        assert len(ht) == 0

        ht["apple"] = 5
        assert len(ht) == 1

    def test_iter_usable_in_for_loop(self):
        ht = Hash_Table()
        ht["apple"] = 5
        ht["banana"] = 3

        collected_keys = []
        collected_values = []

        for key in ht:
            collected_keys.append(key)
            collected_values.append(ht[key])

        assert len(collected_keys) == 2
        assert "apple" in collected_keys
        assert "banana" in collected_keys
        assert 5 in collected_values
        assert 3 in collected_values

    def test_multiple_collisions_same_bucket(self):
        """Test handling multiple collisions in one bucket"""
        ht = Hash_Table(1)

        keys_values = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]

        for key, value in keys_values:
            ht[key] = value

        for key, expected_value in keys_values:
            assert ht[key] == expected_value

        assert len(ht) == 4

    def test_keys(self):
        ht = Hash_Table()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        keys = list(ht.keys())
        assert sorted(keys) == ["a", "b", "c"]

    def test_values(self):
        ht = Hash_Table()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        values = list(ht.values())
        assert sorted(values) == [1, 2, 3]

    def test_items(self):
        ht = Hash_Table()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        items = list(ht.items())
        assert sorted(items) == [("a", 1), ("b", 2), ("c", 3)]

    def test_get_existing_key(self):
        ht = Hash_Table()
        ht["a"] = 1
        assert ht.get("a") == 1

    def test_get_non_existing_key(self):
        ht = Hash_Table()
        assert ht.get("nonexistent") is None

    def test_pop_existing_key(self):
        ht = Hash_Table()
        ht["a"] = 1
        value = ht.pop("a")
        assert value == 1
        assert "a" not in ht

    def test_pop_non_existing_key(self):
        ht = Hash_Table()
        with pytest.raises(KeyError):
            ht.pop("nonexistent")

    def test_clear(self):
        ht = Hash_Table()
        ht["a"] = 1
        ht["b"] = 2
        ht.clear()
        assert len(ht) == 0
        assert list(ht.items()) == []
