from typing import List, Set
from itertools import combinations

from .item_set import ItemSet
from .transaction import Transactions
from .fp_tree import FPTree


def enum_list(li: List[str]):
    # print("enum list")
    # print(li)
    result = set()
    li = sorted(li)
    for i in range(len(li) + 1):
        for comb in combinations(li, i):
            item_set = ItemSet(comb)
            result.add(item_set)

    # print(result)
    return result


def get_frequent_set(t: Transactions, support: int) -> Set[ItemSet]:
    if len(t.ts) == 1:
        # single path prefix
        names = t.ts[0][0]
        return enum_list(names)

    result = set()
    tree = FPTree.from_transactions_unprocessed(t, support)
    for header in reversed(tree.headers):
        name = header.name
        prefix_t = tree.get_prefix(name)
        # print(prefix_t.ts)

        prefix_set = get_frequent_set(prefix_t, support)
        for prefix_set_item in prefix_set:
            prefix_set_item.insert(name)
            result.add(prefix_set_item)
    return result
