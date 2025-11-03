import typing
import multiprocessing

manager = multiprocessing.Manager()
print(type(manager))

class Hash_Table:
    """Hash table - dictionary implementation using separate chaining."""

    def __init__(self, size: int = 50) -> None:
        """
        Args:
            size: Number of buckets in the hash table
        """
        self.size = size

        # Creating a Manager for a shared state
        self.manager: multiprocessing.managers.SyncManager = multiprocessing.Manager()

        # Creating shared lists and locks
        self.buckets = self.manager.list([self.manager.list() for _ in range(size)])
        self.locks = self.manager.list([self.manager.Lock() for _ in range(size)])

    def _hash(self, key: typing.Any) -> int:
        """
        Args:
            key: Key to hash
        Returns:
            int: Hash code for the key
        """
        return hash(key) % self.size

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        """
        Args:
            key: Key to set
            value: Value to set
        """
        index = self._hash(key)

        with self.locks[index]:
            bucket = self.buckets[index]

            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return

            bucket.append((key, value))

    def __getitem__(self, key: typing.Any) -> typing.Any:
        """
        Args:
            key: Key to retrieve
        Returns:
            typing.Any: Value associated with the key
        Raises:
            KeyError: If key is not found
        """
        index = self._hash(key)

        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key: typing.Any) -> None:
        """
        Args:
            key: Key to delete
        Raises:
            KeyError: If key is not found
        """
        index = self._hash(key)

        with self.locks[index]:
            bucket = self.buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return
            raise KeyError(key)

    def __contains__(self, key: typing.Any) -> bool:
        """
        Args:
            key: Key to check
        Returns:
            bool: True if key exists, False otherwise
        """
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return True
        return False

    def __len__(self) -> int:
        """
        Returns:
            int: Number of key-value pairs in the hash table
        """
        count = 0
        for i in range(self.size):
            with self.locks[i]:
                count += len(self.buckets[i])
        return count

    def __iter__(self) -> typing.Iterator[typing.Any]:
        """
        Returns:
            typing.Iterator[typing.Any]: Iterator over keys
        """
        for i in range(self.size):
            with self.locks[i]:
                for k, v in self.buckets[i]:
                    yield k

    def __repr__(self) -> str:
        """
        Returns:
            str: String representation of the hash table
        """
        items = []
        for i in range(self.size):
            with self.locks[i]:
                for k, v in self.buckets[i]:
                    items.append(f"{k}: {v}")
        return "ThreadSafeHashTable({" + ", ".join(items) + "})"

    def keys(self) -> typing.Iterator[typing.Any]:
        """
        Returns:
            typing.Iterator[typing.Any]: Iterator over keys
        """
        return iter(self)

    def values(self) -> typing.Iterator[typing.Any]:
        """
        Returns:
            typing.Iterator[typing.Any]: Iterator over values
        """
        for i in range(self.size):
            with self.locks[i]:
                for k, v in self.buckets[i]:
                    yield v

    def items(self) -> typing.Iterator[tuple[typing.Any, typing.Any]]:
        """
        Returns:
            typing.Iterator[tuple]: Iterator over key-value pairs
        """
        for i in range(self.size):
            with self.locks[i]:
                for k, v in self.buckets[i]:
                    yield (k, v)

    def get(self, key: typing.Any, default: typing.Any = None) -> typing.Any:
        """
        Args:
            key: Key to retrieve
            default: Default value if key not found

        Returns:
            typing.Any: Value or default if key not found
        """
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key: typing.Any) -> typing.Any:
        """
        Args:
            key: Key to remove and return

        Returns:
            typing.Any: Value associated with the key

        Raises:
            KeyError: If key is not found
        """
        index = self._hash(key)

        with self.locks[index]:
            bucket = self.buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    return v
            raise KeyError(key)

    def clear(self) -> None:
        """Removes all key-value pairs from the hash table."""
        for i in range(self.size):
            with self.locks[i]:
                self.buckets[i][:] = []
