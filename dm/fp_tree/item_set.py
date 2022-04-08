from __future__ import annotations
from typing import Tuple


class ItemSet:
    def __hash__(self):
        return self.hash

    def __init__(self, li: Tuple[str]):
        self.li = sorted(li)
        self._update_hash()

    def __repr__(self):
        return "{" + ",".join(self.li) + "}"

    def _update_hash(self):
        self.hash = hash(tuple(self.li))

    def insert(self, item: str):
        self.li.insert(0, item)
        self.li.sort()
        self._update_hash()

    def union(self, other: ItemSet) -> ItemSet:
        s = set()
        for item in self.li:
            s.add(item)
        for item in other.li:
            s.add(item)
        li = tuple(s)

        result = ItemSet(li)
        return result
