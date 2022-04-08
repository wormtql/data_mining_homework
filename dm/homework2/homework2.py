from typing import List, Set

from .load_data import load_transaction, load_fake_transaction
from dm.fp_tree.fp_tree import FPTree
from dm.fp_tree.transaction import Transactions
from dm.fp_tree.mining import get_frequent_set
from dm.fp_tree.rule import AssociationRule


def homework2():
    # transaction = load_fake_transaction()
    transaction = load_transaction()
    # tree = FPTree.from_transactions_unprocessed(transaction, 3)
    # prefix_t = tree.get_prefix("m")
    # print(prefix_t.ts)

    item_set = list(get_frequent_set(transaction, 2000))
    print(item_set)
    print(len(item_set))

    rule = AssociationRule(item_set[0], item_set[2])
    print(rule)

    sup = transaction.calc_support_of_association_rule(rule)
    print(sup)
    conf = transaction.calc_confidence_of_association_rule(rule)
    print(conf)

    # print(transaction.ts[10])
    # t2, _ = transaction.extract_frequent(500)
    # print(t2.ts[10])
    #
    # tree = FPTree()
    # tree.update_with_transactions(t2)

